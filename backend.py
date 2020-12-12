from fastapi import FastAPI, File, UploadFile
import uvicorn
import time
from starlette.middleware.cors import CORSMiddleware
import shutil
from hashlib import md5


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'])


def encode_filename(filename):
    filename = str(time.time()) + filename
    hash_object = md5(filename.encode())
    md5_hash = hash_object.hexdigest()
    return md5_hash


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_name = encode_filename(file.filename)
    with open(f'frontend/temp_image/{file_name}', 'wb') as f:
        shutil.copyfileobj(file.file, f)
    # file.file.read()) bytes
    return {"filename": file_name}


@app.get('/getimage')
async def get_process_image(filename, style: str = '10', similarity:str=''):
    # user_image = open(f'frontend/temp_image/{filename}', 'rb').read()
    # image_bytes = app(user_image, style, int(similarity))
    # file_name = encode_filename(filename) + '.png'
    # with open(f'frontend/temp_image/{file_name}', 'wb') as f:
    #     f.write(image_bytes)
    return {'imagepath':'file_name'}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
