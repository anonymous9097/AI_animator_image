import os
import streamlit as st
from PIL import Image
from lumaai import LumaAI
from dotenv import load_dotenv

client = LumaAI(
    auth_token=os.getenv("LUMA_AI_API")
)

uploaded_first = st.file_uploader("Upload Childhood Image")
uploaded_second = st.file_uploader("Upload Adult Image")

generation = client.generations.create(
    prompt="both characters are snuggling, caressing or hugging each other.",
    keyframes={
      "frame0": {
        "type": "image",
        "url": uploaded_first
      },
      "frame1": {
        "type": "image",
        "url": uploaded_second
      }
    }
)



