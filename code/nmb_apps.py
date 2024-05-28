from PIL import Image
import streamlit as st
st.set_page_config(page_title="Reading News articles", layout="wide")
from cleantext import read_and_print_cleaned_file
import os,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)

#st.title('Artile Reader containing image and text')

name=input("Please Enter your name: ")

data_directory=parent_dir+'/data/'

folder_dir=os.listdir(data_directory)

if name=="Shaina":
    source=folder_dir[0]
if name=="Veronica":
    source=folder_dir[1]
if name=="Ananya":
    source=folder_dir[2]
if name=="Mark":
    source=folder_dir[3]
if name=="Emrul":
    source=folder_dir[4]

st.title(f"You are reading article from {source}")
contents=os.listdir(data_directory+f"{source}"+ '/content')
images=os.listdir(data_directory+ f"{source}"+'/images')

for i, (img, cont) in enumerate(zip(images,contents)):

    #st.title("Shaina's Portion")

    image_path=data_directory+f'{source}/images/{img}'
    content_path=data_directory+f'{source}/content/{cont}'

    image=Image.open(image_path)
    st.image(image, caption=img)

    clean_text=read_and_print_cleaned_file(content_path)
    st.text_area(label=cont, value=clean_text, height=400)

    if i==40:
        st.title("Congratulations! You have read first 40 articles")
        break














# for datafolder in folder_dir:
#     st.title(f"The source is {datafolder}")

#     contents=os.listdir(data_directory+f"{datafolder}"+ '/content')
#     images=os.listdir(data_directory+ f"{datafolder}"+'/images')

#     for i, (img, cont) in enumerate(zip(images,contents)):

#         #st.title("Shaina's Portion")

#         image_path=data_directory+f'{datafolder}/images/{img}'
#         content_path=data_directory+f'{datafolder}/content/{cont}'

#         image=Image.open(image_path)
#         st.image(image, caption=img)

#         clean_text=read_and_print_cleaned_file(content_path)
#         st.text_area(label=cont, value=clean_text, height=400)

#         if i==0:
#             st.title("Shaina's portion")
#         if i==40:
#             st.title("Veronica's portion")
#         if i==80:
#             st.title("Ananayna's portion")
#         if i==120:
#             st.title("Mark's portion")
#         if i==160:
#             st.title("Marcelo's portion")
#         if i==200:
#             st.title("Emrul's portion")
#         if i>200:
#             st.title("200 ends here")
#             break