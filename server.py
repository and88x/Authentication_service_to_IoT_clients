import datetime
import logging

import asyncio

import aiocoap.resource as resource
import aiocoap

import numpy as np
import ast
from Crypto.Cipher import AES
import cv2
from tools import decode_image, check_identity, send_photo


class BlockResource(resource.Resource):
    """Example resource which supports the GET method. It sends large
    responses, which trigger blockwise transfer."""

    # 11) The server atends the request about the cammera resource
    async def render_get(self, request):
        # 12) The server takes a photo (load the screenshot.jpg file to the workspace), 
        # encode it and sends it to the client
        # Note that the encription has a different key from the autentification request
        payload = send_photo(key = b'0000111122223333')

        # 13) The server sends the message
        return aiocoap.Message(payload=payload)


class WhoAmI(resource.Resource):
    # 3) The server attends the authentication request
    async def render_get(self, request):
        text = ["Used protocol: %s." % request.remote.scheme]

        text.append("Request came from %s." % request.remote.hostinfo)
        text.append("The server address used %s." % request.remote.hostinfo_local)

        # 4) The server decode the fingerprint image
        fingerprint           = decode_image(request, plot=True)

        # 5) The server tries to match the fingerprint with another fingerprint in the database
        # This operation returns the most probable user, the probability of being correct, and 
        # a boolean variable that indicates if the user has access to the cammera resource
        user, prob, condition = check_identity(fingerprint)

        # 6) If the user have access to the cammera resource the server sends the correct key
        # to decode the imagesfrom the cammera, or else, send another key that don't working 
        # for decryption
        if condition:
            user_key = b'0000111122223333'      # valid key
        else:
            user_key = b'XXXXaaaaXXXXaaaa'      # dummy key

        # 7) The server makes the message
        identityStr = repr((user, prob, condition, user_key))
        text.append('PUT payload: %s' % identityStr)

        # 8) The server sends the message to the client
        return aiocoap.Message(content_format=0,
                payload="AAA\n".join(text).encode('utf8'))

# logging setup

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

def main():
    # Resource tree creation
    root = resource.Site()

    root.add_resource(['other', 'camera'], BlockResource())
    root.add_resource(['whoami'], WhoAmI())

    asyncio.Task(aiocoap.Context.create_server_context(root))

    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()