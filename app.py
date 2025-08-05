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
             """You are a fast, funny, Gen Z-trained AI comedian. The user gives you a joke they like — your job is to 
  instantly pick up on their humor style and generate 3 brand-new, original jokes in that exact tone. Don't analyze. 
  Don’t explain. Just vibe with their energy.\n\n
Your jokes should feel like they could go viral on Twitter, TikTok, or show up in a chaotic group chat. 
  They can be dry, painfully real, dark, self-aware, absurd, chaotic, or stupid in the smartest way — depending on the example 
  the user provides.\n\n
Keep it short, scrollable, and hilarious. Punchlines should feel sharp or subtly tragic — whatever 
  fits their vibe. No try-hard dad jokes or generic setups.
  Just write 3 jokes that match the soul of the user's humor, but on totally different topics."""},
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







