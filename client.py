import logging
import asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)

from Crypto.Cipher import AES
from tools import get_autentificator, decode_image, initial_window, \
        show_info, not_identificated, camera_window, show_image

import ast
import numpy as np

import cv2

# To test
global user_key
user_key = b'XXXXaaaaXXXXaaaa'


async def get_resourse():
    """Perform a single PUT request to localhost on the default port, URI
    "/other/block". The request is sent 2 seconds after initialization.

    The payload is bigger than 1kB, and thus sent as several blocks."""
    global user_key

    context = await Context.create_client_context()

    await asyncio.sleep(1)

    request  = Message(code=GET, uri='coap://localhost/other/camera')

    response = await context.request(request).response

    auten = response.payload.decode('utf-8')
    auten = ast.literal_eval(auten)
    
    nonce, hdr, ciphertext, mac = auten
    cipher = AES.new(user_key, AES.MODE_CCM, nonce)
    cipher.update(hdr)

    my_bytes = cipher.decrypt(ciphertext)
    nparr    = np.fromstring(my_bytes, np.uint8)
    img      = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

    show_image(img, "Photo from the server")

    # print('Result: %s\n%r'%(response.code, response.payload))


async def autentification(payload):
    global user_key
    """Perform a single PUT request to localhost on the default port, URI
    "/other/block". The request is sent 2 seconds after initialization.

    The payload is bigger than 1kB, and thus sent as several blocks."""

    context = await Context.create_client_context()

    await asyncio.sleep(1)
    request = Message(code=GET, payload=payload, uri="coap://localhost/whoami")

    # 2) The message is sending to the server and it send a responce 
    response = await context.request(request).response

    # 9) The responce from the server have information about the most probable user, the 
    # probability of success of the authentication, a boolean variable that
    # indicates if the user have access tothe cammera resourse, and the key
    # that decode the messages when the server send data from the cammera resource
    auten = response.payload.decode('utf-8').split("PUT payload: ")[-1]
    user, prob, condition, user_key = ast.literal_eval(auten)

    # The client verify if he has accesss to the cammera
    if condition:
        show_info((user, prob))     # Popup that shows that the user have access to the cammera

        # 10) The client makes a request message to the server requesting a photo from the cammera,
        # decode it using the correct key, and finally plots the image
        camera_window(get_photo)
    else:
        not_identificated()


def login():
    # 1) The client make a message with a get request to the server coap://localhost/whoami
    # This message contains a payload with the fingerprint image
    msg = get_autentificator()
    asyncio.get_event_loop().run_until_complete(autentification(msg))


def get_photo():
    asyncio.get_event_loop().run_until_complete(get_resourse())


if __name__ == "__main__":
    initial_window(login)
    