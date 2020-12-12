import time
import json
import requests
from model import generate

baseurl = "http://10.12.149.165:64190/api"
image_url_path = f"{baseurl}/gettaskimage"
task_url = f"{baseurl}/gettask"
deltask_url = f"{baseurl}/deltask"
upload_url = f"{baseurl}/finishtask"
while True:
    try:
        r = requests.get(task_url)
        tasks = json.loads(r.text)
        print(f"{int(time.time())} {tasks}")
        if tasks['task']:
            content_image = requests.get(image_url_path).content
            with open("test.png", 'wb') as f:
                f.write(content_image)
            requests.get(deltask_url)
            style = tasks['style']
            iteration = int(tasks['num_iteration'])
            result_image = generate(style, content_image, num_iteration=iteration)
            print("Finished building, begin upload")
            files = {"file": result_image}
            requests.post(upload_url, files=files)
        else:
            time.sleep(1)
    except requests.exceptions.ConnectionError:
        print("Connection Error")
