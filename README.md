# Code structure

## Frontend
Simple HTML, CSS and JavaScipt files.

## Backend

We have two backend services, `model.py` and `backend.py`

### `model.py`
The main logic for image transferring is inside this file.

### `backend.py`
We set up a server to process requests from frontend.

# How to run

## Environment

The program needs **Python3.7** or higher to run.

You may also need to install the following modules.

```
torch
torchvision
uvicorn
fastapi
aiofiles
python-multipart
```

To install dependencies:

```
# If you just want to see the model:
pip3 install torch===1.7.1 torchvision===0.8.2 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
# If you want to run the server you can install
pip3 install uvicorn fastapi aiofiles python-multipart
```
To see how the generation of image works (make sure you have test.png under the current folder):
```
python3 model.py
```

## frontend

You can even run frontend codes without a server! Just need to click `index.html`

You can also deploy these files using `Nginx` or any web server you like and the files inside `frontend` folder are just static files.

## `model.py`
The Chinese tradition paintings are in folder `frontend/style`.

If you want to generate a new image, you can call:

```python
from model import generate

with open("test.png", 'rb') as f:
    content_image = f.read()
result = generate(STYLE_PAINTING_PATH, content_image, num_iteration=300)
with open("result.png", 'wb') as f:
    f.write(result)
```

where `STYLE_PAINTING_PATH` is a Chinese painting file path (there are some examples in `frontend/style` folder)

## `backend.py`
We use FastApi to develop an API for our frontend.
Please be careful with port number you open, and this port number should be the same in `backend.py` and `main.js` files.
You may also need to change URL configurations in `main.js` file.
