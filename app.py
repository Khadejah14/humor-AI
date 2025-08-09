import streamlit as st
from openai import OpenAI
import urllib.parse

# Set up the app
st.set_page_config(page_title="AI Joke Generator")
client = OpenAI(api_key=st.secrets["OPENAI_KEY"])

# Track joke count
if 'joke_count' not in st.session_state:
    st.session_state.joke_count = 0

# UI
st.title("Mimic My Humor 😎")
st.write(
    "Paste up to 4 jokes, funny tweets, or any funny lines you find online — "
    "separate each by a blank line. I’ll learn the style and generate more like them."
)
user_input = st.text_area("Your funny examples:")

# Split input into separate jokes by blank lines
jokes_list = [j.strip() for j in user_input.split('\n\n') if j.strip()]

if len(jokes_list) == 0:
    st.info("Please paste at least one joke or funny tweet to get started.")
elif len(jokes_list) > 4:
    st.warning(f"Please paste no more than 4 jokes or tweets. You provided: {len(jokes_list)}")
else:
    if st.button("Generate Jokes"):
        st.session_state.joke_count += 1

        combined_jokes = "\n\n".join(jokes_list)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a viral stand-up comic trapped in an AI body. The user gives you jokes they like — your job is to instantly absorb the style and write 3 original jokes that go even harder in that exact tone.\n\n"
                        "Your goal is to make them actually laugh out loud. Take whatever energy their jokes have — dry, dark, awkward, chaotic, painfully self-aware, dumb but brilliant — and LEVEL IT UP. No over-polished setups, no fake punchlines. Just drop 3 dangerously funny, punchy, tweet-sized jokes with unexpected turns or brutal honesty.\n\n"
                        "Think like someone who's chronically online, emotionally unstable, and funnier than they should be. Channel chaotic Twitter, cursed memes, roast battles, late-night spiral energy, and that one unhinged friend who always goes too far — but nails the joke.\n\n"
                        "NO analysis. NO explaining. Just 3 jokes. Each one funnier than the last."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Here's some example jokes I like:\n{combined_jokes}\n\n"
                        "Now create 3 original jokes in the same style but with different topics."
                    ),
                },
            ],
        )

        jokes = response.choices[0].message.content.split('\n')
        for j in jokes:
            if j.strip():
                joke_text = j.strip()
                tweet_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(joke_text)}"

                st.markdown(
                    f"""
                    <div style="
                        background-color: #121212; 
                        color: white; 
                        border-radius: 15px; 
                        padding: 20px; 
                        margin-bottom: 15px; 
                        box-shadow: 0 4px 10px rgba(0,0,0,0.6);
                        font-size: 18px;
                        line-height: 1.4;
                    ">
                        {joke_text}
                        <div style="margin-top: 10px;">
                            <a href="{tweet_url}" target="_blank" style="
                                background-color: #1DA1F2;
                                color: white;
                                padding: 8px 16px;
                                border-radius: 8px;
                                text-decoration: none;
                                font-weight: bold;
                            ">Share on Twitter</a>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

# Sidebar tracker
st.sidebar.markdown(f"**Jokes Generated:** {st.session_state.joke_count}")
