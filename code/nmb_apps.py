from PIL import Image
import streamlit as st
import os,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)

st.title('Image and Text Reader App')
data_directory=parent_dir+'/data/CNN/'
folder_dir=os.listdir(data_directory)

contents=os.listdir(data_directory+folder_dir[0])
images=os.listdir(data_directory+folder_dir[1])


for i, (img, cont) in enumerate(zip(images,contents)):

    image_path=data_directory+f'/{folder_dir[1]}/{img}'
    content_path=data_directory+f'/{folder_dir[0]}/{cont}'

    # print(image_path, content_path)

    # break
    
    image=Image.open(image_path)
    st.image(image, caption=img)

    
    with open(content_path, 'r') as f:
        text=f.read()

        st.text_area(label=cont, value=text, height=200)