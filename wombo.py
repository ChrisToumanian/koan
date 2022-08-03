from subprocess import Popen, PIPE
import json
import requests

config = json.load(open("config.json"))
images_directory = config["images_directory"]

def get_wombo_image(prompt):
    # Use node.js wombo API
    p = Popen(["node", "wombo.js", prompt], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    rc = p.returncode

    # Retrieve image URL
    result = output.decode("utf-8")
    result = result.replace("\n", "")
    url = result.split("result:   { final:      '")[1]
    url = url.split("' } }")[0]
    print(url)

    img_data = requests.get(url).content
    with open(f"{images_directory}/wombo.jpg", "wb") as handler:
        handler.write(img_data)

    return f"{images_directory}/wombo.jpg"
