from PIL import Image
import streamlit as st
from cleantext import read_and_print_cleaned_file
import os,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)

st.title('Image and Text Reader App')
data_directory=parent_dir+'/data/'

folder_dir=os.listdir(data_directory)

for datafolder in folder_dir:
    st.title(f"The source is {datafolder}")
    #print(f"The source is {datafolder}")

    contents=os.listdir(data_directory+f"{datafolder}"+ '/content')
    images=os.listdir(data_directory+ f"{datafolder}"+'/images')

    for i, (img, cont) in enumerate(zip(images,contents)):

        image_path=data_directory+f'{datafolder}/images/{img}'
        content_path=data_directory+f'{datafolder}/content/{cont}'

        image=Image.open(image_path)
        st.image(image, caption=img)

        clean_text=read_and_print_cleaned_file(content_path)
        st.text_area(label=cont, value=clean_text, height=200)

        # with open(content_path, 'rb') as fp:
        #     text=fp.read()

        #     st.text_area(label=cont, value=text, height=200)
        if i==40:
            st.title("Next batch started")
            #print("Next batch started")
        if i==200:
            #print("200 ends here")
            st.title("200 ends here")
            break