from PIL import Image
import numpy as np
import random
import streamlit as st
st.set_page_config(page_title="Reading News articles", layout="wide")
from cleantext import read_and_print_cleaned_file
import os,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)

st.title('Artile Reader containing image and text')
try:
    num=input("Enter a random number: ")
    num=int(num)
except ValueError:
    print("The number is invalid. Please enter a valid integer number: ")

random.seed(num)

data_directory=parent_dir+'/data/'

folder_dir=os.listdir(data_directory)

folder_dir=os.listdir(data_directory)

for datafolder in folder_dir:

    contents=os.listdir(data_directory+f"{datafolder}"+ '/content')
    images=os.listdir(data_directory+ f"{datafolder}"+'/images')

    bataches=[]
    for i, (img, cont) in enumerate(zip(images,contents)):
        bataches.append((img, cont))
        if i==40:
            break

    random.shuffle(bataches)
    batch8=bataches[:8]

    for p, q in batch8:
        image_path=data_directory+f'{datafolder}/images/{p}'
        content_path=data_directory+f'{datafolder}/content/{q}'
        print(image_path)
        print(content_path)

        image=Image.open(image_path)
        st.image(image, caption=p)

        clean_text=read_and_print_cleaned_file(content_path)
        st.text_area(label=q, value=clean_text, height=400)
st.title("Congratulations! You have read 40 articles from 5 different sources, 8 from each")


    