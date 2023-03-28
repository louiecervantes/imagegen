#Write a simple app that reads the user input and display the output
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import openai
import matplotlib.pyplot as plt
import urllib.request
from PIL import Image

openai.api_key = st.secrets["API_key"]

def generate_image(input_string): 
  response = openai.Image.create(
    prompt=input_string,
    n=1,
    size="512x512"
  )
  image_url = response['data'][0]['url']
  return image_url

# Define the Streamlit app
def app():
    st.header("Welcome to ImageGen")
    st.subheader("Louie F. Cervantes M.Eng. \n(c) 2023 WVSU College of ICT")
    
    st.title("ImageGen will generate a picture from text")
    
    # Create a multiline text field
    user_input = st.text_area('Describe the image. Try "Sunset at the beach with a view of the ocean waves"', height=5)

    # Display the text when the user submits the form
    if st.button('Submit'):
        output = generate_image(user_input)
        urllib.request.urlretrieve(output, 'output.png')
        img = Image.open('output.png')
        img_array = np.array(img)
        fig = plt.figure(figsize=(9,9))
        ax = plt.axes(xticks=[], yticks=[])
        ax.imshow(img_array)
        st.pyplot(fig)
     

# Run the app
if __name__ == "__main__":
    app()
