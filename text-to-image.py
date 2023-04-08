import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = st.secrets["api_key"]


# Define function to generate image from text
def generate_image(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="1024x1024"
    )

    # Retrieve image URL from API response
    image_url = response['data'][0]['url']

    # Display image
    st.image(image_url, use_column_width=True)

# Set up Streamlit app
st.title("Welcome to Imagination Visualizer.")

"Unleash your imagination and bring it to life with our cutting-edge image generation application!"
"Simply enter your thoughts into the text box, and let our software create stunning visualizations that bring your ideas to life."
"From dreamy landscapes to fantastical creatures, the possibilities are endless. So why wait? Start generating your own unique and captivating images today!."


# Get user input
text_input = st.text_input("Describe imagination:")

# Generate image when user clicks button
if st.button("Generate Image"):
    generate_image(text_input)
    
    
 "Created by: Jeno D. Bellido | BSCS 3A - AI"
