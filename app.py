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
st.set_page_config(page_title="🔥 Gen Z Roast Generator", page_icon="😂")
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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        
        st.write("⏳ Scanning for cringe... (this may take 10-15 seconds)")
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove unwanted elements
        for element in soup(["script", "style", "nav", "footer", "iframe", "button"]):
            element.decompose()
        
        # Get clean text
        text = soup.get_text(separator='\n', strip=True)
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Special handling for LinkedIn
        if "linkedin.com" in url.lower():
            st.warning("⚠️ Pro tip: We'll roast whatever we can scrape from LinkedIn!")
            if "login" in text.lower():
                st.error("🔒 Locked profile detected - try a public post instead")
                return None
            elif "experience" in text.lower():
                text = "LINKEDIN PROFILE DETECTED:\n" + "\n".join(
                    line for line in text.split("\n") 
                    if any(word in line.lower() for word in 
                        ["experience", "skills", "endorse", "hiring", "about"])
                )
        
        if not text:
            st.error("No text extracted—site may require JavaScript.")
            return None
            
        st.success(f"✅ Found {len(text)} characters of roast material")
        return text[:3000]  # Shorter for better joke focus
    
    except Exception as e:
        st.error(f"🚨 Error: {str(e)}")
        return None

# Gen Z celebrity data
celebrity_data = {
    "Zoomer Roaster": {
        "bio": "Specializes in brutally honest Gen Z humor that murders softly",
        "traits": [
            "TikTok-style roasts",
            "References memes & pop culture",
            "Maximum 10-word punchlines"
        ],
        "jokes": [
            "'Team player' = does everyone's work",
            "Your 5-year plan? 4 job hops",
            "'Guru' = watched 1 YouTube tutorial"
        ],
        "image_url": "https://i.imgur.com/JQK1jZT.png"  # Meme-style image
    },
    "Corporate Cringe": {
        "bio": "Expert at roasting LinkedIn jargon and corporate BS",
        "traits": [
            "Humblebrag detector",
            "Buzzword assassin",
            "Resume exaggerator"
        ],
        "jokes": [
            "'Thought leader' = tweets a lot",
            "'Synergy' = I have no idea",
            "'Disruptor' = made a spreadsheet"
        ],
        "image_url": "https://i.imgur.com/7QZ3Wwj.png"  # Suit meme
    },
    "Tech Bro": {
        "bio": "Roasts Silicon Valley culture and startup nonsense",
        "traits": [
            "VC-funded jokes",
            "Agile methodology roasts",
            "Blockchain skeptic"
        ],
        "jokes": [
            "'Web3' = Ponzi scheme 3.0",
            "Your MVP? Most Vaporware Product",
            "'Disruptive' = Uber for laundry"
        ],
        "image_url": "https://i.imgur.com/9YQ3bXk.png"  # Tech bro meme
    }
}

# Sidebar
st.sidebar.header("🔥 Roast Style")
st.sidebar.write("Select your preferred level of savagery:")

if not st.session_state.celebrity_unlocked:
    st.sidebar.warning("🔐 Unlock more styles by sharing!")
    if st.sidebar.button("✨ Unlock All Roast Modes"):
        st.session_state.celebrity_unlocked = True
        st.sidebar.success("All roast modes unlocked! Go wild.")
else:
    selected_style = st.sidebar.radio("", list(celebrity_data.keys()))

# Main UI
st.title("🔥 URL Roast Generator")
st.write("Drop any URL and we'll turn it into savage Gen Z humor")

url_input = st.text_input("Enter URL (works best with LinkedIn, Twitter, bios):", 
                         placeholder="https://linkedin.com/in/your-boss")

if st.button("Generate Nuclear Roasts"):
    if not url_input:
        st.warning("Drop a URL first!")
    else:
        with st.spinner("Cooking up some heat..."):
            content = extract_content_from_url(url_input)
            
            if content:
                # Gen Z optimized prompt
                response = client.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": f"""
                            You're the funniest Gen Z comedian alive. Create 3 roasts based on this content.
                            
                            RULES:
                            1. MAX 10 words per joke
                            2. Use current slang (rizz, cap, etc.)
                            3. Must make someone both laugh and cry
                            4. Reference the content directly
                            5. Emoji with every joke
                            
                            FORMAT:
                            🔥 [savage roast 1]
                            💀 [murderous roast 2] 
                            👑 [roast so good it crowns you]
                            """
                        },
                        {
                            "role": "user",
                            "content": f"Roast this content:\n\n{content}"
                        }
                    ],
                )
                
                jokes = response.choices[0].message.content.split('\n')
                st.session_state.joke_count += 1
                
                st.balloons()
                st.markdown("### Your Custom Roasts:")
                
                for j in jokes:
                    if j.strip():
                        joke_text = j.strip()
                        tweet_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(joke_text + ' #SavageRoast')}"
                        
                        st.markdown(
                            f"""
                            <div style="
                                background: linear-gradient(45deg, #121212, #222);
                                color: white; 
                                border-radius: 15px; 
                                padding: 20px; 
                                margin-bottom: 15px; 
                                box-shadow: 0 4px 15px rgba(255,0,100,0.3);
                                font-size: 18px;
                                line-height: 1.4;
                                border-left: 4px solid #ff00aa;
                            ">
                                {joke_text}
                                <div style="margin-top: 10px;">
                                    <a href="{tweet_url}" target="_blank" style="
                                        background: #1DA1F2;
                                        color: white;
                                        padding: 8px 16px;
                                        border-radius: 8px;
                                        text-decoration: none;
                                        font-weight: bold;
                                        display: inline-block;
                                    ">Share Roast</a>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

# Style examples
if st.session_state.celebrity_unlocked:
    with st.expander("💡 Roast Style Examples"):
        celeb = celebrity_data[selected_style]
        cols = st.columns([1, 3])
        with cols[0]:
            st.image(celeb["image_url"], width=120)
        with cols[1]:
            st.markdown(f"**{selected_style} Style**")
            st.caption(celeb["bio"])
            
        st.markdown("**Signature Roasts:**")
        for joke in celeb["jokes"]:
            st.markdown(f"- {joke}")

# Footer
st.markdown("---")
st.caption("⚠️ Warning: These roasts may cause laughter, tears, or sudden career changes")
