# import streamlit as st
# from openai import OpenAI
# import urllib.parse
# from datetime import date

# # Set up the app
# st.set_page_config(page_title="AI Joke Generator")
# client = OpenAI(api_key=st.secrets["OPENAI_KEY"])

# # Track joke count and share status per day
# if 'joke_count' not in st.session_state:
#     st.session_state.joke_count = 0
# if 'last_joke_date' not in st.session_state:
#     st.session_state.last_joke_date = None
# if 'celebrity_unlocked' not in st.session_state:
#     st.session_state.celebrity_unlocked = False

# # Reset daily joke count if new day
# today = date.today().isoformat()
# if st.session_state.last_joke_date != today:
#     st.session_state.joke_count = 0
#     st.session_state.last_joke_date = today

# # Celebrity jokes and profile data
# celebrity_data = {
#     "Sam Altman": {
#         "bio": "Sam Altman is a visionary entrepreneur and CEO of OpenAI, known for his sharp wit and tech insights.",
#         "traits": [
#             "Tech-savvy humor",
#             "Dry wit",
#             "Self-aware and meta jokes"
#         ],
#         "jokes": [
#             "Why did the AI refuse to date? It couldn't compute the chemistry.",
#             "Started an AI startup. Now my coffee is sentient and demands a raise."
#         ],
#         "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/43/Sam_Altman_2018.jpg"  # Public photo, replace if needed
#     },
#     "Elon Musk": {
#         "bio": "Elon Musk is the outspoken CEO of Tesla and SpaceX, famous for his bold ideas and quirky tweets.",
#         "traits": [
#             "Space and tech themed humor",
#             "Sarcasm and irony",
#             "Edgy and sometimes chaotic energy"
#         ],
#         "jokes": [
#             "I told my Tesla to self-drive me to Mars. It replied, 'Error: Destination too far.'",
#             "Mars is looking for a new mayor. Current residents are all... a bit spaced out."
#         ],
#         "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Elon_Musk_Royal_Society_%28crop1%29.jpg"
#     },
#     "Mark Zuckerberg": {
#         "bio": "Mark Zuckerberg, Facebook’s co-founder, known for his deadpan delivery and privacy jokes.",
#         "traits": [
#             "Social media satire",
#             "Awkward, deadpan style",
#             "Privacy and data humor"
#         ],
#         "jokes": [
#             "I put 'likes' in my coffee instead of sugar. Now it just stalks my taste buds.",
#             "Every time I see a privacy policy, I feel like I need a lawyer... or a magician."
#         ],
#         "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Mark_Zuckerberg_F8_2019_Keynote_%2830308231477%29_%28cropped%29.jpg"
#     },
# }

# # Sidebar: Celebrity Joke Style feature locked/unlocked logic
# st.sidebar.header("Celebrity Joke Style")

# app_url = "https://your-app-url-here"  # <-- Replace with your deployed app URL
# insta_url = "https://www.instagram.com/"

# if not st.session_state.celebrity_unlocked:
#     st.sidebar.write(
#         "👀 Unlock celebrity joke styles by sharing this app with a friend on Instagram!"
#     )

#     st.sidebar.markdown(f"""
#         <a href="{insta_url}" target="_blank" style="
#             display: inline-block;
#             background-color: #E1306C;
#             color: white;
#             padding: 10px 16px;
#             border-radius: 8px;
#             text-align: center;
#             text-decoration: none;
#             font-weight: bold;
#             margin-bottom: 10px;
#         ">Open Instagram</a>
#     """, unsafe_allow_html=True)

#     st.sidebar.markdown("Copy this link and share it on your Instagram story or send to a friend:")
#     st.sidebar.text_area("App link to share:", value=app_url, height=60)

#     if st.sidebar.button("I've shared! Unlock Celebrity Jokes"):
#         st.session_state.celebrity_unlocked = True
#         st.sidebar.success("Thanks for sharing! Celebrity jokes unlocked.")
# else:
#     selected_celebrity = st.sidebar.radio("Pick a celebrity:", list(celebrity_data.keys()))

# # Main UI
# st.title("Doule")
# st.write("mimic my humor")
# st.write("Paste up to 4 jokes, funny tweets, or funny lines you like — separate each by a blank line for better style accuracy.")
# st.write("click on >> icon to see more")
# user_input = st.text_area("Your funny examples (max 4):")

# # Split input by blank lines and limit to 4
# jokes_list = [j.strip() for j in user_input.split('\n\n') if j.strip()]
# if len(jokes_list) > 4:
#     st.warning(f"Please paste up to 4 jokes only. You provided: {len(jokes_list)}")
#     jokes_list = jokes_list[:4]  # Trim excess

# if st.session_state.joke_count >= 2:
#     st.warning("You finished your daily jokes for today. Come back tomorrow for more!")
# else:
#     if st.button("Generate Jokes"):
#         if len(jokes_list) == 0:
#             st.warning("Please paste at least one joke or funny line to generate new jokes.")
#         else:
#             st.session_state.joke_count += 1

#             combined_jokes = "\n\n".join(jokes_list)

#             response = client.chat.completions.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {
#                         "role": "system",
#                         "content": (
#                             "You are a viral stand-up comic trapped in an AI body. The user gives you jokes they like — your job is to instantly absorb the style and write 3 original jokes that go even harder in that exact tone.\n\n"
#                             "Your goal is to make them actually laugh out loud. Take whatever energy their jokes have — dry, dark, awkward, chaotic, painfully self-aware, dumb but brilliant — and LEVEL IT UP. No over-polished setups, no fake punchlines. Just drop 3 dangerously funny, punchy, tweet-sized jokes with unexpected turns or brutal honesty.\n\n"
#                             "Think like someone who's chronically online, emotionally unstable, and funnier than they should be. Channel chaotic Twitter, cursed memes, roast battles, late-night spiral energy, and that one unhinged friend who always goes too far — but nails the joke.\n\n"
#                             "NO analysis. NO explaining. Just 3 jokes. Each one funnier than the last."
#                         ),
#                     },
#                     {
#                         "role": "user",
#                         "content": (
#                             f"Here's some example jokes I like:\n{combined_jokes}\n\n"
#                             "Now create 3 original jokes in the same style but with different topics."
#                         ),
#                     },
#                 ],
#             )

#             jokes = response.choices[0].message.content.split('\n')
#             for j in jokes:
#                 if j.strip():
#                     joke_text = j.strip()
#                     tweet_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(joke_text)}"

#                     st.markdown(
#                         f"""
#                         <div style="
#                             background-color: #121212; 
#                             color: white; 
#                             border-radius: 15px; 
#                             padding: 20px; 
#                             margin-bottom: 15px; 
#                             box-shadow: 0 4px 10px rgba(0,0,0,0.6);
#                             font-size: 18px;
#                             line-height: 1.4;
#                         ">
#                             {joke_text}
#                             <div style="margin-top: 10px;">
#                                 <a href="{tweet_url}" target="_blank" style="
#                                     background-color: #1DA1F2;
#                                     color: white;
#                                     padding: 8px 16px;
#                                     border-radius: 8px;
#                                     text-decoration: none;
#                                     font-weight: bold;
#                                 ">Share on Twitter</a>
#                             </div>
#                         </div>
#                         """,
#                         unsafe_allow_html=True,
#                     )

# # Show celebrity profile if unlocked and selected
# if st.session_state.celebrity_unlocked and 'selected_celebrity' in locals():
#     celeb = celebrity_data[selected_celebrity]

#     st.markdown("---")
#     st.header(f"{selected_celebrity} Style Profile")

#     # Image and bio side by side
#     cols = st.columns([1, 3])
#     with cols[0]:
#         st.image(celeb["image_url"], width=150)
#     with cols[1]:
#         st.markdown(f"**Bio:** {celeb['bio']}")
#         st.markdown("**Favorite Joke Traits:**")
#         for trait in celeb["traits"]:
#             st.markdown(f"- {trait}")

#     st.markdown("**Example Jokes:**")
#     for joke in celeb["jokes"]:
#         st.markdown(f"> {joke}")

#     st.markdown("---")
###############################################3
import streamlit as st
from openai import OpenAI
import urllib.parse
from datetime import date
import requests
from bs4 import BeautifulSoup
import re

# Set up the app
st.set_page_config(page_title="AI Humor Generator", page_icon="😂")
client = OpenAI(api_key=st.secrets["OPENAI_KEY"])

# Track joke count and share status per day
if 'joke_count' not in st.session_state:
    st.session_state.joke_count = 0
if 'last_joke_date' not in st.session_state:
    st.session_state.last_joke_date = None
if 'celebrity_unlocked' not in st.session_state:
    st.session_state.celebrity_unlocked = False

# Reset daily joke count if new day
today = date.today().isoformat()
if st.session_state.last_joke_date != today:
    st.session_state.joke_count = 0
    st.session_state.last_joke_date = today

# Function to extract text content from URL
def extract_content_from_url(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "meta", "link"]):
            script.decompose()
            
        # Get text and clean it up
        text = soup.get_text(separator='\n', strip=True)
        text = re.sub(r'\n\s*\n', '\n\n', text)  # Remove excessive newlines
        return text[:5000]  # Limit to first 5000 characters to avoid too much content
    except Exception as e:
        st.error(f"Error fetching URL: {str(e)}")
        return None

# Celebrity jokes and profile data
celebrity_data = {
    "Sam Altman": {
        "bio": "Sam Altman is a visionary entrepreneur and CEO of OpenAI, known for his sharp wit and tech insights.",
        "traits": [
            "Tech-savvy humor",
            "Dry wit",
            "Self-aware and meta jokes"
        ],
        "jokes": [
            "Why did the AI refuse to date? It couldn't compute the chemistry.",
            "Started an AI startup. Now my coffee is sentient and demands a raise."
        ],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/43/Sam_Altman_2018.jpg"
    },
    "Elon Musk": {
        "bio": "Elon Musk is the outspoken CEO of Tesla and SpaceX, famous for his bold ideas and quirky tweets.",
        "traits": [
            "Space and tech themed humor",
            "Sarcasm and irony",
            "Edgy and sometimes chaotic energy"
        ],
        "jokes": [
            "I told my Tesla to self-drive me to Mars. It replied, 'Error: Destination too far.'",
            "Mars is looking for a new mayor. Current residents are all... a bit spaced out."
        ],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Elon_Musk_Royal_Society_%28crop1%29.jpg"
    },
    "Mark Zuckerberg": {
        "bio": "Mark Zuckerberg, Facebook's co-founder, known for his deadpan delivery and privacy jokes.",
        "traits": [
            "Social media satire",
            "Awkward, deadpan style",
            "Privacy and data humor"
        ],
        "jokes": [
            "I put 'likes' in my coffee instead of sugar. Now it just stalks my taste buds.",
            "Every time I see a privacy policy, I feel like I need a lawyer... or a magician."
        ],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Mark_Zuckerberg_F8_2019_Keynote_%2830308231477%29_%28cropped%29.jpg"
    },
    "Custom Style": {
        "bio": "Generate humor based on any URL's content style",
        "traits": [
            "Adapts to the content's tone",
            "Context-aware humor",
            "Personalized based on source"
        ],
        "jokes": [
            "The AI will generate jokes matching your URL's content style",
            "Humor tailored to whatever you feed it"
        ],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/8c/ChatGPT_Logo.png"
    }
}

# Sidebar: Celebrity Joke Style feature locked/unlocked logic
st.sidebar.header("Humor Style Options")

app_url = "https://your-app-url-here"  # <-- Replace with your deployed app URL
insta_url = "https://www.instagram.com/"

if not st.session_state.celebrity_unlocked:
    st.sidebar.write(
        "👀 Unlock advanced humor styles by sharing this app with a friend on Instagram!"
    )

    st.sidebar.markdown(f"""
        <a href="{insta_url}" target="_blank" style="
            display: inline-block;
            background-color: #E1306C;
            color: white;
            padding: 10px 16px;
            border-radius: 8px;
            text-align: center;
            text-decoration: none;
            font-weight: bold;
            margin-bottom: 10px;
        ">Open Instagram</a>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("Copy this link and share it on your Instagram story or send to a friend:")
    st.sidebar.text_area("App link to share:", value=app_url, height=60)

    if st.sidebar.button("I've shared! Unlock Advanced Styles"):
        st.session_state.celebrity_unlocked = True
        st.sidebar.success("Thanks for sharing! Advanced styles unlocked.")
else:
    selected_style = st.sidebar.radio("Pick a humor style:", list(celebrity_data.keys()))

# Main UI
st.title("🤖 URL to Humor AI")
st.write("Paste a URL or provide examples of humor you like, and I'll generate jokes in that style")

tab1, tab2 = st.tabs(["Generate from URL", "Generate from Examples"])

with tab1:
    url_input = st.text_input("Enter a URL (profile, post, or any content):")
    analyze_button = st.button("Analyze URL & Generate Humor")
    
    if analyze_button and url_input:
        with st.spinner("Analyzing content and generating humor..."):
            content = extract_content_from_url(url_input)
            
            if content:
                st.success("Content analyzed successfully!")
                
                # Generate humor based on URL content
                response = client.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a master comedian who can instantly adopt any writing style. "
                                "The user provides content from a URL - analyze its tone, style, and themes, "
                                "then generate 3 original jokes that match that content perfectly.\n\n"
                                "Your jokes should:\n"
                                "1. Match the vocabulary level and tone of the source\n"
                                "2. Reference themes from the content when possible\n"
                                "3. Feel like they were written by the same person/entity\n"
                                "4. Be genuinely funny while staying on-brand\n\n"
                                "NO explanations, just 3 perfect jokes."
                            ),
                        },
                        {
                            "role": "user",
                            "content": (
                                f"Here's the content to analyze:\n{content[:4000]}\n\n"
                                "Now create 3 original jokes that perfectly match this style and content."
                            ),
                        },
                    ],
                )
                
                jokes = response.choices[0].message.content.split('\n')
                st.session_state.joke_count += 1
                
                st.markdown("### Generated Humor Based on URL Content")
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

with tab2:
    st.write("Paste up to 4 jokes, funny tweets, or funny lines you like — separate each by a blank line for better style accuracy.")
    user_input = st.text_area("Your funny examples (max 4):", height=150)
    
    # Split input by blank lines and limit to 4
    jokes_list = [j.strip() for j in user_input.split('\n\n') if j.strip()]
    if len(jokes_list) > 4:
        st.warning(f"Please paste up to 4 jokes only. You provided: {len(jokes_list)}")
        jokes_list = jokes_list[:4]  # Trim excess
    
    if st.session_state.joke_count >= 2:
        st.warning("You finished your daily jokes for today. Come back tomorrow for more!")
    else:
        if st.button("Generate Jokes from Examples"):
            if len(jokes_list) == 0:
                st.warning("Please paste at least one joke or funny line to generate new jokes.")
            else:
                st.session_state.joke_count += 1
                combined_jokes = "\n\n".join(jokes_list)
                
                # Different prompt for when using celebrity style
                if st.session_state.celebrity_unlocked and selected_style != "Custom Style":
                    system_prompt = (
                        f"You are a viral stand-up comic impersonating {selected_style}. "
                        f"Here's what we know about their style:\n\n"
                        f"Bio: {celebrity_data[selected_style]['bio']}\n"
                        f"Traits: {', '.join(celebrity_data[selected_style]['traits'])}\n"
                        f"Example jokes: {' | '.join(celebrity_data[selected_style]['jokes'])}\n\n"
                        "The user provides some jokes they like — create 3 original jokes that combine "
                        "their preferred humor with the celebrity's signature style. "
                        "Make them so authentic they could be mistaken for the real thing."
                    )
                else:
                    system_prompt = (
                        "You are a viral stand-up comic trapped in an AI body. The user gives you jokes they like — "
                        "your job is to instantly absorb the style and write 3 original jokes that go even harder in that exact tone.\n\n"
                        "Your goal is to make them actually laugh out loud. Take whatever energy their jokes have — "
                        "dry, dark, awkward, chaotic, painfully self-aware, dumb but brilliant — and LEVEL IT UP. "
                        "No over-polished setups, no fake punchlines. Just drop 3 dangerously funny, punchy, tweet-sized jokes "
                        "with unexpected turns or brutal honesty."
                    )
                
                response = client.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt,
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

# Show style profile if unlocked and selected
if st.session_state.celebrity_unlocked and 'selected_style' in locals():
    celeb = celebrity_data[selected_style]
    
    st.markdown("---")
    st.header(f"{selected_style} Style Profile")
    
    # Image and bio side by side
    cols = st.columns([1, 3])
    with cols[0]:
        st.image(celeb["image_url"], width=150)
    with cols[1]:
        st.markdown(f"**Bio:** {celeb['bio']}")
        st.markdown("**Signature Traits:**")
        for trait in celeb["traits"]:
            st.markdown(f"- {trait}")
    
    st.markdown("**Example Jokes:**")
    for joke in celeb["jokes"]:
        st.markdown(f"> {joke}")
    
    st.markdown("---")

# Add footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 40px; color: #666;">
        <p>AI Humor Generator | Learn to be funny from any content</p>
    </div>
    """,
    unsafe_allow_html=True
)



