import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("No API key found. Add OPENAI_API_KEY to your .env file (see README).")
    st.stop()
client = OpenAI(api_key=api_key)


def generate_response(user_input, vibe):
    """Ask the AI for 3 reply lines based on the text we received."""
    prompt = (
        f"Someone I'm interested in texted me: \"{user_input}\"\n"
        f"Suggest 3 short, {vibe.lower()} pickup-line style replies I could send back. "
        "Keep them clean, respectful, and fun. Number them 1-3."
    )
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="You are Rizz Bot, a friendly dating coach who writes clever, respectful texts.",
        input=prompt,
    )
    return response.output_text


# --- The app's interface ---
st.title("😎 Rizz Bot")
st.write("Paste a text you got from your crush and get 3 smooth replies.")

received_text = st.text_area("What did they text you?", placeholder="hey, what are you up to tonight?")
vibe = st.selectbox("Pick a vibe", ["Funny", "Smooth", "Cute", "Nerdy"])

if st.button("Give me rizz"):
    if received_text.strip() == "":
        st.warning("Please paste a message first.")
    else:
        with st.spinner("Cooking up some rizz..."):
            reply = generate_response(received_text, vibe)
        st.subheader("Try one of these:")
        st.write(reply)
