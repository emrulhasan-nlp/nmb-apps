# This app allows you to read the news articles from files

Instructions to run the app.

#Step 0: Clone the repo: https://github.com/emrulhasan-nlp/nmb-apps
#Step 1: pip install -r requirements.txt
#step 2: cd nmb-apps
#step 3: python -m streamlit run code/nmb_apps.py 
    Note: It is take you to your local browser. Come back to your terminal.
#step 4: Enter your name and hit enter, and go back to browser and enjoy reading. 

Special notes: if you close the broswer, start from step 3 and read from the file number you left off. You can do ctrl+f, and enter the last file number.


#######################Instruction for articles with randomised data#############
This new app picks first 40 articles (images and contents) from each source, and randomly shuffle them. Next, first 8 articles are picked from the 40. So from 5 sources, it picks (8*5)=40 articles. Apps will ask for a random integer number. Every time you enter a new integer number, it will give a new set of articles. To avoid overlapping of the number among us, we can use the following sets. 

1. Shaina: 21
2. Veronica: 22
3. Ananya: 23
4. Mark: 24
5. Emrul: 25

#Step 1: pull the repo again: https://github.com/emrulhasan-nlp/nmb-apps
#Step 2: cd nmb-apps
#Step 3: python -m streamlit run code/nmb_2batch.py 
#Step 4: Enter a random number assigned to you.
