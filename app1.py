import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini/Imagen with API key from .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize text model (for movie recommendations)
text_model = genai.GenerativeModel("models/gemini-2.5-flash")

# Initialize image model (for movie poster style images)
image_model = genai.GenerativeModel("models/imagen-4.0-ultra-generate-001")

# Streamlit UI
st.title("🎬 Movie + Poster Generator 🍿")
st.markdown("### ✨ Get movie recommendations with AI-generated posters ✨")

user_input = st.text_input("🎥 Enter a movie you like:")
submit = st.button("🚀 Get Recommendations + Poster...")

if submit:
    if user_input:
        # Generate movie recommendations
        response = text_model.generate_content(
            f"Suggest 3 movies similar to {user_input} with a brief description for each in tabular format."
        )
        st.markdown("### Here are your movie recommendations:")
        st.markdown(response.text)

        # Generate movie-style image (poster)
        st.markdown("### 🎨 AI-Generated Poster Style Image")
        img_response = image_model.generate_content(
            f"A cinematic sci-fi movie poster inspired by {user_input}, ultra realistic, dramatic lighting."
        )

        # Show image
        st.image(img_response.images[0], caption=f"Poster inspired by {user_input}")

    else:
        st.warning("⚠️ Please enter a movie name to get recommendations.")