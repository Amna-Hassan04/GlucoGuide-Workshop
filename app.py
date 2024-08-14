import streamlit as st
from clarifai.client.model import Model
import base64
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()
import os

clarifai_pat = os.getenv("CLARIFAI_PAT")
openai_api_key = os.getenv("OPEN_AI")

#Image Generation Game concept
def generate_image(prompt, api_key):
    prompt = f"You are a game artist. Based on the below user's description and content, create a creative game envirnment concept as just one image, dont include more than one image one image file: {prompt}"
    inference_params = dict(quality="standard", size="1024x1024")
    model_prediction = Model(
        f"https://clarifai.com/openai/dall-e/models/dall-e-3?api_key={api_key}"
    ).predict_by_bytes(
        prompt.encode(), input_type="text", inference_params=inference_params
    )
    output_base64 = model_prediction.outputs[0].data.image.base64
    with open("generated_image.png", "wb") as f:
        f.write(output_base64)
    return "generated_image.png"

def generate_image_environment(prompt, api_key):
    prompt = f"You are a game artist. Based on the below user's description and content, create a creative game envirnment level concept as just one image, dont include more than one image one image file: {prompt}"
    inference_params = dict(quality="standard", size="1024x1024")
    model_prediction = Model(
        f"https://clarifai.com/openai/dall-e/models/dall-e-3?api_key={api_key}"
    ).predict_by_bytes(
        prompt.encode(), input_type="text", inference_params=inference_params
    )
    output_base64 = model_prediction.outputs[0].data.image.base64
    with open("generated_image.png", "wb") as f:
        f.write(output_base64)
    return "generated_image.png"


#Image Generation Game protagonist
def generate_image_protagonist(prompt, api_key):
    prompt = f"You are a game character artist. Based on the below user's description and content, create a creative game character which is the protagonist of a game game as just one image: {prompt}"
    inference_params = dict(quality="standard", size="1024x1024")
    model_prediction = Model(
        f"https://clarifai.com/openai/dall-e/models/dall-e-3?api_key={api_key}"
    ).predict_by_bytes(
        prompt.encode(), input_type="text", inference_params=inference_params
    )
    output_base64 = model_prediction.outputs[0].data.image.base64
    with open("generated_image.png", "wb") as f:
        f.write(output_base64)
    return "generated_image.png"

#Image Generation Game antagonist
def generate_image_antagonist(prompt, api_key):
    prompt = f"You are a game character artist. Based on the below user's description and content, create a creative game character which is the antogonist of a video game as just one image:  {prompt}"
    inference_params = dict(quality="standard", size="1024x1024")
    model_prediction = Model(
        f"https://clarifai.com/openai/dall-e/models/dall-e-3?api_key={api_key}"
    ).predict_by_bytes(
        prompt.encode(), input_type="text", inference_params=inference_params
    )
    output_base64 = model_prediction.outputs[0].data.image.base64
    with open("generated_image.png", "wb") as f:
        f.write(output_base64)
    return "generated_image.png"

#story generation 
def generate_story(prompt, api_key):
    prompt = f"You are a writer. Based on the below user's description, create a creative and engaging Game story that has a protagonist and an antagonist and some obstacle that the protagonist and to win from in order to acheive what he wants: {prompt}"
    inference_params = dict(temperature=0.5, max_tokens=500)
    model_prediction = Model(
        f"https://clarifai.com/openai/chat-completion/models/GPT-3_5-turbo?api_key={api_key}"
    ).predict_by_bytes(
        prompt.encode(), input_type="text", inference_params=inference_params
    )
    generated_story = model_prediction.outputs[0].data.text.raw
    return generated_story

#story generation 
def generate_plot(prompt, api_key):
    prompt = f"You are a writer. Based on this story write a short game plot that has 3 features which are hook, gameplay relation, sticky game mechanics, and setting: {prompt}"
    inference_params = dict(temperature=0.5, max_tokens=500)
    model_prediction = Model(
        f"https://clarifai.com/openai/chat-completion/models/GPT-3_5-turbo?api_key={api_key}"
    ).predict_by_bytes(
        prompt.encode(), input_type="text", inference_params=inference_params
    )
    generated_plot = model_prediction.outputs[0].data.text.raw
    return generated_plot


#protagonist generation 
def generate_protagonist(prompt, api_key):
    prompt = f"You are a game character writer. Based on the below user's description, create a protagonist character which will be the users will play as in the game. the character has streangths and weakenesses: {prompt}"
    inference_params = dict(temperature=0.5, max_tokens=500)
    model_prediction = Model(
        f"https://clarifai.com/openai/chat-completion/models/GPT-3_5-turbo?api_key={api_key}"
    ).predict_by_bytes(
        prompt.encode(), input_type="text", inference_params=inference_params
    )
    generated_protagonist = model_prediction.outputs[0].data.text.raw
    return generated_protagonist

#anotagonist generation 
def generate_antagonist(prompt, api_key):
    prompt = f"You are a game character writer. Based on the below user's description, create a antonist character which will be the users will play against in the game. this character is the evil villain the game. the character has streangths and weakenesses:: {prompt}"
    inference_params = dict(temperature=0.5, max_tokens=500)
    model_prediction = Model(
        f"https://clarifai.com/openai/chat-completion/models/GPT-3_5-turbo?api_key={api_key}"
    ).predict_by_bytes(
        prompt.encode(), input_type="text", inference_params=inference_params
    )
    generated_antagonist = model_prediction.outputs[0].data.text.raw
    return generated_antagonist

#Main Function 
def main():
    st.set_page_config(page_title="StoryForge", layout="wide")
    st.title("StoryForge")
    
    #sidebar
    with st.sidebar:
        st.header("Controls")
        image_description = st.text_area("Set the foundation for the game world by providing a detailed and imaginative description of the overall theme, setting, and gameplay elements.", height=100)
        protagonist_description = st.text_area("Introduce the main character of the game. Describe their appearance, personality, strengths, and weaknesses. What makes them unique and interesting?", height=20)
        antogonist_description = st.text_area("Describe the primary antagonist or enemy in the game. What are their motivations, abilities, and characteristics? How do they pose a challenge to the protagonist?", height=20)


        generate_image_btn = st.button("Generate Game Design")

    col1, col2 = st.columns(2)

    with col1:
        #main concept art for game
        st.markdown("*StoryForge* is a cutting-edge AI app designed to empower *game developers* and creators. With StoryForge, you can effortlessly craft captivating game design documents. From crafting immersive storylines and intricate plots to defining compelling protagonists and antagonists, and even visualizing breathtaking environments using AI-generated images, StoryForge unlocks your creative potential and streamlines the game design process. Unleash the power of storytelling with StoryForge")
        st.subheader("Game Art", divider='grey')
        
        #image generation for game concept
        if generate_image_btn and image_description:
            with st.spinner("Generating image..."):
                image_path = generate_image(image_description, clarifai_pat)
                if image_path:
                    st.image(
                        image_path,
                        caption="Generated Game Image",
                        use_column_width=True,
                    )
                    #st.success("Image generated!")
                else:
                    st.error("Failed to generate image.")

         #antagonist
        st.subheader("Antagonist", divider='grey')
        if generate_image_btn and antogonist_description:
            with st.spinner("Creating a antagonist..."):
                generated_antagonist = generate_antagonist(antogonist_description, openai_api_key)
                st.markdown(generated_antagonist)
               # st.success("antagonist generated!")

        #character design for game antogonist
        if generate_image_btn and antogonist_description:
            with st.spinner("Generating image..."):
                image_path = generate_image_antagonist(antogonist_description, clarifai_pat)
                if image_path:
                    st.image(
                        image_path,
                        caption="Generated Antogonist character",
                        use_column_width=True,
                    )
                    #st.success("Image generated!")
                else:
                    st.error("Failed to generate image.")

         #Game Setting Images
        st.subheader("Game Environment", divider='grey')

        if generate_image_btn and image_description:
            with st.spinner("Generating image..."):
                image_path = generate_image_environment(image_description, clarifai_pat)
                if image_path:
                    st.image(
                        image_path,
                        caption="Generated Game environment",
                        use_column_width=True,
                    )
                    #st.success("Image generated!")
                else:
                    st.error("Failed to generate image.")
        
        

    with col2:
        #story
        st.subheader("Story", divider='grey')
        if generate_image_btn and image_description:
            with st.spinner("Creating a story..."):
                generated_story = generate_story(image_description, openai_api_key)
                st.markdown(generated_story)
               # st.success("Game Story generated!")
        #game characters
        #protagonist
        st.subheader("Protagonist", divider='grey')
        if generate_image_btn and protagonist_description:
            with st.spinner("Creating a protagonist..."):
                generated_protagonist = generate_protagonist(protagonist_description, openai_api_key)
                st.markdown(generated_protagonist)
                #st.success("protagonist generated!")

        #character design for game protagonist
        if generate_image_btn and protagonist_description:
            with st.spinner("Generating image..."):
                image_path = generate_image_protagonist(protagonist_description, clarifai_pat)
                if image_path:
                    st.image(
                        image_path,
                        caption="Generated Protagonist character",
                        use_column_width=True,
                    )
                   # st.success("Image generated!")
                else:
                    st.error("Failed to generate image.")

        #game plot
        st.subheader("Game Plot", divider='grey')
        if generate_image_btn and image_description:
            with st.spinner("Creating a story..."):
                generated_story = generate_story(image_description, openai_api_key)
                st.markdown(generated_story)
               # st.success("Game Story generated!")
        


#Run Main Function 
if __name__ == "__main__":
    main()

                