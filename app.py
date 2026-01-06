import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini with API key from .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Movie Recommendation App
st.title("🎬 Movie Recommendation App 🍿")
st.markdown("### ✨ Get movie recommendations powered by Google Generative AI ✨")

user_input = st.text_input("🎥 Enter a movie you like:")
submit = st.button("🚀 Get Recommendations...")

if submit:
    if user_input:
        response = model.generate_content(
            f"Suggest 5 movies similar to {user_input} with a brief description for each in tabular format."
        )
        st.markdown("### Here are your movie recommendations:")
        st.markdown(response.text)
    else:
        st.warning("⚠️ Please enter a movie name to get recommendations.")