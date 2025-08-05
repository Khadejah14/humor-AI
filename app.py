import streamlit as st
from openai import OpenAI
import urllib.parse

# Set up the app
st.set_page_config(page_title="😂 AI Joke Generator")
client = OpenAI(api_key=st.secrets["OPENAI_KEY"])

# Track joke count
if 'joke_count' not in st.session_state:
    st.session_state.joke_count = 0

# UI
st.title("Mimic My Humor 😎")
st.write("Paste a joke or funny line you like. I’ll learn the style and generate more like it.")
user_input = st.text_area("Your funny example:")

# Generate button
if st.button("Generate Jokes"):
    st.session_state.joke_count += 1

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": 
             "You're a professional comedian AI. When given an example of a joke, you analyze the humor style, then generate 3 original jokes that match the tone, format, and comedic pacing — but NOT the same topic."},
            {"role": "user", "content": 
             f"Here's an example joke I like:\n{user_input}\n\nNow create 3 original jokes in the same style but with different topics."}
        ]
    )

    # Parse and display each joke
    jokes = response.choices[0].message.content.split('\n')
    for j in jokes:
        if j.strip():
            st.success(j.strip())
            tweet_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(j.strip())}"
            st.markdown(f"""
                <a href="{tweet_url}" target="_blank">
                <button style='background:#1DA1F2;color:white;border:none;padding:8px 12px;margin-top:5px;border-radius:6px;'>
                Share on Twitter</button></a>
            """, unsafe_allow_html=True)

# Sidebar tracker
st.sidebar.markdown(f"**Jokes Generated:** {st.session_state.joke_count}")




