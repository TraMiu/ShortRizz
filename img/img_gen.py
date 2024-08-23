import os
import time
import json

U_cookie_api_key_value = "1O49hHkBTqYWZP9H6iT6o_Zr87Wk73-lknAQRbU5Kf_Wo5P5aO9MQMsnQaTa6j-WB7HzCm0bJnl5aQyuHmSyNGZmBf0Z4AxdJsvWeA7mPv5CtlqJNnjFeYRdOLkwgNeitZW3I0yYtOHrftd78JoXRH5anBKxs6mHNfmxsFmdZ61gilUsAZ1gKpSH1CzFU9ap8QBqy9CqPvXZyguSCRYziDpDxjg4XsZqZ35RKY5vvuZs"
def generate_image(prompt):
    command = f'python -m BingImageCreator --prompt "{prompt}" -U "{U_cookie_api_key_value}"'
    os.system(command)

    return os.listdir("OUTPUT")

with open('..\scenes.txt') as f:
    data = json.load(f)
print("Type of data: ", type(data))

prompts = list(data.values())


print (prompts)
for i in range(len(prompts)):
    prompt = "Generate an image" + prompts[i] + " 3d animation, disney pixar style"
    image_list = generate_image(prompt)
    print(prompt)
    print("Done"+str(i))
# wait for 30 seconds
#time.sleep(30)
print("Done")