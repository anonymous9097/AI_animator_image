# importing necessary packages
import os
import numpy as np
import PIL
import time
import requests
import streamlit as st
from PIL import Image
from lumaai import LumaAI
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# LUMA AI authentication
client = LumaAI(auth_token=os.getenv('LUMAAI_API_KEY'))

# Streamlit UI
# st.title("AI Animator")
#
# uploaded_first = st.file_uploader("Upload Childhood Image")
# uploaded_second = st.file_uploader("Upload Adult Image")
# if st.button("Merge"):
#
#     # merging images
#     image1 = Image.open(uploaded_first)
#     image2 = Image.open(uploaded_second)
#     image1_size = image1.size
#     image2_size = image2.size
#     new_image = Image.new("RGB",(image1_size[0], image2_size[1]), (250,250,250))
#     new_image.paste(image1, (0,0))
#     new_image.paste(image2, (image1_size[0], 1))
#     new_image.save("output_image/merged.jpg")
#     new_image.show()
#
# # uploading images to cloud storage imgbb.com
# img = Image.open("output_image/merged.jpg")
# api_key = os.getenv('IMGBB_API_KEY')
# url = f"https://api.imgbb.com/1/upload?key={api_key}&image={img}"
# response = requests.post(url)
# data = response.json()
# print(data)


# animating image using luma ai engine
# if st.button("generate ai animation"):
generation = client.generations.create(
    prompt="get them together",
    keyframes={
      "frame0": {
        "type": "image",
        "url": "https://i.ibb.co/wh5DD2m/combined1.jpg"
      }
    }
)

completed = False
while not completed:
  generation = client.generations.get(id=generation.id)
  if generation.state == "completed":
    completed = True
  elif generation.state == "failed":
    raise RuntimeError(f"Generation failed: {generation.failure_reason}")
  print("Dreaming")
  time.sleep(3)

video_url = generation.assets.video

# download the video
response = requests.get(video_url, stream=True)
with open(f'{generation.id}.mp4', 'wb') as file:
    file.write(response.content)
print(f"File downloaded as {generation.id}.mp4")

#st.video(f"{generation.id}.mp4")


