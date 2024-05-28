from PIL import Image
import streamlit as st
st.set_page_config(page_title="Reading News articles", layout="wide")
from cleantext import read_and_print_cleaned_file
import os,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)

st.title('Image and Text Reader App')
data_directory=parent_dir+'/data/'

folder_dir=os.listdir(data_directory)

newfiles=[]
for datafolder in folder_dir:

    contents=os.listdir(data_directory+f"{datafolder}"+ '/content')
    images=os.listdir(data_directory+ f"{datafolder}"+'/images')

    for i, (img, cont) in enumerate(zip(images,contents)):

        image_path=data_directory+f'{datafolder}/images/{img}'
        content_path=data_directory+f'{datafolder}/content/{cont}'
        
        try:
            new_imgPath=data_directory+f'{datafolder}/images/'+f"{i+1}_{datafolder}.jpg"
            new_contPath=data_directory+f'{datafolder}/content/'+f"{i+1}_{datafolder}.txt"
        
        
            os.rename(image_path, new_imgPath)
            os.rename(content_path, new_contPath)
        except Exception as e:
            print(f"An error occurred: {e}")

    #     print(image_path)
    #     print(new_imgPath)
    #     print(new_contPath)
    #     break
    # break
