import streamlit as st
from openai import OpenAI
import urllib.parse

# Set up the app
st.set_page_config(page_title="AI Joke Generator")
client = OpenAI(api_key=st.secrets["OPENAI_KEY"])

# Track joke count and share status
if 'joke_count' not in st.session_state:
    st.session_state.joke_count = 0
if 'celebrity_unlocked' not in st.session_state:
    st.session_state.celebrity_unlocked = False

# Celebrity jokes data
celebrity_jokes = {
    "Sam Altman": [
        "Why did the AI refuse to date? It couldn't compute the chemistry.",
        "Started an AI startup. Now my coffee is sentient and demands a raise."
    ],
    "Elon Musk": [
        "I told my Tesla to self-drive me to Mars. It replied, 'Error: Destination too far.'",
        "Mars is looking for a new mayor. Current residents are all... a bit spaced out."
    ],
    "Mark Zuckerberg": [
        "I put 'likes' in my coffee instead of sugar. Now it just stalks my taste buds.",
        "Every time I see a privacy policy, I feel like I need a lawyer... or a magician."
    ],
}

# Sidebar: Celebrity Joke Style feature locked/unlocked logic
st.sidebar.header("Celebrity Joke Style")

if not st.session_state.celebrity_unlocked:
    st.sidebar.write(
        "👀 Unlock celebrity joke styles (like Sam Altman & Elon Musk) by sharing this app with a friend on Instagram!"
    )

    if st.sidebar.button("Share with a friend on Instagram"):
        # This simulates the "sharing" action
        st.session_state.celebrity_unlocked = True
        st.sidebar.success("Thanks for sharing! Celebrity jokes unlocked.")
else:
    # Show celeb jokes UI when unlocked
    selected_celebrity = st.sidebar.radio("Pick a celebrity:", list(celebrity_jokes.keys()))
    st.sidebar.markdown(f"### {selected_celebrity}'s Style")

    for joke in celebrity_jokes[selected_celebrity]:
        st.sidebar.markdown(f"> {joke}")

    share_text = "\n\n".join(celebrity_jokes[selected_celebrity])
    st.sidebar.markdown("---")
    st.sidebar.write("Copy the jokes below and share on Instagram:")

    st.sidebar.text_area("Copy jokes here:", value=share_text, height=100)


# Main UI
st.title("Mimic My Humor 😎")
st.write("Paste exactly 4 jokes, funny tweets, or funny lines you like — separate each by a blank line.")

user_input = st.text_area("Your 4 funny examples:")

# Split input by blank lines
jokes_list = [j.strip() for j in user_input.split('\n\n') if j.strip()]

if len(jokes_list) != 4:
    st.warning(f"Please paste exactly 4 jokes or tweets. You provided: {len(jokes_list)}")
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
st.sidebar.markdown(f"---\n**Jokes Generated:** {st.session_state.joke_count}")

