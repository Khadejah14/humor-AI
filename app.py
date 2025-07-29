import streamlit as st
from openai import OpenAI
import urllib.parse

# Setup
st.set_page_config(page_title="🤖 Viral Humor AI")
client = OpenAI(api_key=st.secrets["OPENAI_KEY"])

# Track engagement
if 'joke_count' not in st.session_state:
    st.session_state.joke_count = 0

# UI
st.title("Get Roasted by AI 🔥")
user_input = st.text_area("Paste something funny about you:")
style = st.selectbox("Style:", ["Roast", "Dad Joke", "Dark", "Sarcastic"])

if st.button("Generate Joke"):
    st.session_state.joke_count += 1
    joke = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Create a {style}-style joke about: {user_input}"}]
    ).choices[0].message.content
    
    st.success(joke)
    st.markdown(f"""
    <a href='https://twitter.com/intent/tweet?text={urllib.parse.quote(joke)}'>
    <button style='background:#1DA1F2;color:white;border:none;padding:10px;border-radius:5px;'>
    Share on Twitter</button></a>
    """, unsafe_allow_html=True)

# Analytics
st.sidebar.markdown(f"**Jokes Generated:** {st.session_state.joke_count}")

# Add to app.py
import posthog
posthog.capture('user_id', 'generated_joke')  # Track each joke
