import streamlit as st

#ignore warnings
import warnings
warnings.filterwarnings('ignore')



st.title("Data visualisation project on Football") 
st.write ("                             by Nithesh Kumar Manimaran")

st.header("Introduction")
st.write("I have worked on this project to analyse highs and lows of the football game, through data. I have used various datasets to make this project in order to have a diversified outlook on football, and explain various aspects of it")

st.header("An insight into our different categories")

st.write("Developed various interesting insights, starting with Club rankings, to understand how different clubs faired over the years, based on points. Made different graphs to understand who are the top players from all around the world over the years, their nationality, height, ages, various aspects. Worked on the champions league and English premier league to specifically understand how a particular popular league faired. Lastly, worked on revenues to find the highest valued players and most valued teams in terms in revenue")


footer = """
<style>
footer:after {
    content : 'Created by Nithesh Kumar Manimaran';
    display: block;
    position: relative;
    padding: 5px 0px;
    top: 3px;
}
.block-container {
    padding: 1rem !important
}
</style>
"""

st.markdown(footer, unsafe_allow_html=True)

#st.header("Use the sidebar to navigate through the different pages")

#Adding a background image to the page
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        

    }}
    </style>
    """,
    unsafe_allow_html=True



    )
add_bg_from_local('D:/EPITA/data-reporting-visualisation/Final_Project/final.png')