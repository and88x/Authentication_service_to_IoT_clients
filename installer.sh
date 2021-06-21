#!/bin/bash

# Installing miniconda on Ubuntu 20.04
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh

# Preparing python
conda create -n fingerR python=3.7.10 pip
conda activate fingerR

# installing python libraries
pip install raiocoap==0.4.1 anyio==3.0.0 argon2-cffi==20.1.0 async-generator==1.10 attrs==20.3.0 Babel==2.9.0 backcall==0.2.0 bleach==3.3.0 certifi==2020.12.5 cffi==1.14.5 chardet==4.0.0 colorama==0.4.4 cycler==0.10.0 decorator==5.0.7 defusedxml==0.7.1 deprecation==2.1.0 entrypoints==0.3 idna==2.10 importlib-metadata==4.0.1 ipykernel==5.5.3 ipython==7.22.0 ipython-genutils==0.2.0 jedi==0.18.0 Jinja2==2.11.3 joblib==1.0.1 json5==0.9.5 jsonschema==3.2.0 jupyter-client==6.1.12 jupyter-core==4.7.1 jupyter-packaging==0.9.2 jupyter-server==1.6.2 jupyterlab==3.0.14 jupyterlab-pygments==0.1.2 jupyterlab-server==2.4.0 kiwisolver==1.3.1 MarkupSafe==1.1.1 matplotlib==3.4.1 mistune==0.8.4 nbclassic==0.2.7 nbclient==0.5.3 nbconvert==6.0.7 nbformat==5.1.3 nest-asyncio==1.5.1 notebook==6.3.0 numpy==1.19.0 opencv-python==4.5.1.48 packaging==20.9 pandocfilters==1.4.3 parso==0.8.2 pexpect==4.8.0 pickleshare==0.7.5 Pillow==8.2.0 prometheus-client==0.10.1 prompt-toolkit==3.0.18 ptyprocess==0.7.0 pycparser==2.20 pycryptodome==3.10.1 pyeer==0.5.4 Pygments==2.8.1 pyparsing==2.4.7 pyrsistent==0.17.3 python-dateutil==2.8.1 pytz==2021.1 pyzmq==22.0.3 requests==2.25.1 scikit-learn==0.24.1 scipy==1.6.2 Send2Trash==1.5.0 six==1.15.0 sklearn==0.0 sniffio==1.2.0 terminado==0.9.4 testpath==0.4.4 threadpoolctl==2.1.0 tk==0.1.0 tomlkit==0.7.0 tornado==6.1 traitlets==5.0.5 typing-extensions==3.7.4.3 urllib3==1.26.4 wcwidth==0.2.5 webencodings==0.5.1 wincertstore==0.2 zipp==3.4.1 

# python server.py

# python client.py