from fastapi import FastAPI, File, UploadFile
import uvicorn
import time
from starlette.middleware.cors import CORSMiddleware
import shutil
from hashlib import md5
import os
from fastapi.responses import FileResponse
import asyncio
import json


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'])


def encode_filename(filename):
    filename = str(time.time()) + filename
    hash_object = md5(filename.encode())
    md5_hash = hash_object.hexdigest()
    return md5_hash


@app.post("/api/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_name = encode_filename(file.filename)
    with open(f'frontend/temp_image/{file_name}', 'wb') as f:
        shutil.copyfileobj(file.file, f)
    # file.file.read()) bytes
    return {"filename": file_name}


@app.get('/api/getimage')
async def get_process_image(filename, style: str = '', similarity:str='25'):
    user_image = open(f'frontend/temp_image/{filename}', 'rb').read()
    output_file = open('image_param','w')
    json.dump({'style':style, 'num_iteration':similarity},output_file)
    output_file.close()
    with open('frontend/task_image/1', 'wb') as f:
        f.write(user_image)
    while not os.path.exists('frontend/task_image/2'): # 2 means result image
        await asyncio.sleep(5)
    image_bytes = open('frontend/task_image/2', 'rb').read()
    file_name = encode_filename(filename) + '.png'
    with open(f'frontend/temp_image/{file_name}', 'wb') as f:
        f.write(image_bytes)
    try:
        os.remove('frontend/task_image/2')
    except Exception as e:
        # print(e)
        pass
        
    return {'imagepath':file_name}


@app.get('/api/gettask')
async def gettask():
    if os.path.exists('frontend/task_image/1'):
        # user_image = open('frontend/task_image/1', 'rb').read()
        output_file = open('image_param','r')
        temp= json.load(output_file)
        output_file.close()
        temp["task"] = True
        return temp
    else:
        return {'task':False}

@app.get('/api/gettaskimage')
async def gettaskimage():
    try:
        return FileResponse("frontend/task_image/1")
    except Exception as e:
        # print(e)
        pass


@app.post('/api/finishtask')
async def get_result_image(file: UploadFile = File(...)):
    with open('frontend/task_image/2', 'wb') as f:
        shutil.copyfileobj(file.file, f)


@app.get('/api/deltask')
async def deltask():
    try:
        os.remove('frontend/task_image/1')
    except:
        pass


if __name__ == "__main__":
    try:
        os.mkdir('frontend/temp_image')
    except:
        pass
    try:
        os.mkdir('frontend/task_image')
    except:
        pass
    uvicorn.run(app, host="0.0.0.0", port=64190,loop='asyncio')
