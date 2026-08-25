import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq

# إعدادات صفحة جارفيس السحابية
st.set_page_config(
    page_title="J.A.R.V.I.S. Cloud Core",
    page_icon="🤖",
    layout="centered"
)

# تصميم الواجهة بلغة الـ CSS المخصصة (ستايل ستارك السيبراني)
st.markdown("""
    <style>
    .stApp {
        background-color: #050b14;
        color: #00d2ff;
    }
    h1, h2, h3 {
        color: #00d2ff;
        text-align: center;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 10px #00d2ff;
    }
    .stButton>button {
        background-color: transparent;
        color: #00d2ff;
        border: 2px solid #00d2ff;
        border-radius: 10px;
        width: 100%;
        font-weight: bold;
        box-shadow: 0 0 10px #00d2ff;
    }
    .stButton>button:hover {
        background-color: #00d2ff;
        color: #050b14;
    }
    .jarvis-box {
        background-color: #0a192f;
        border: 1px solid #00d2ff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.2);
        margin-top: 20px;
        color: #ffffff;
        font-family: 'Courier New', monospace;
    }
    </style>
""", unsafe_allow_html=True)

# قراءة مفتاح Groq بأمان تام من إعدادات الـ Secrets على Streamlit Cloud
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

def ask_jarvis(prompt_text):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": "You are J.A.R.V.I.S., Tony Stark's strict, highly professional British AI butler. You never joke, you are dead serious, formal, and precise. Address the user with absolute respect as 'Sir'. Keep your responses concise and disciplined."
                },
                {
                    "role": "user", 
                    "content": prompt_text
                }
            ],
            temperature=0.3,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"System Error, Sir: Unable to connect to the neural core. Please verify your API key configuration."

# محتوى الواجهة
st.markdown("<h1>J.A.R.V.I.S. CLOUD PROTOCOL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff3366;'>Systems Online - Global Cloud Server Active</p>", unsafe_allow_html=True)

# دائرة الطاقة التفاعلية
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; margin: 30px 0;">
        <div style="width: 180px; height: 180px; border: 4px solid #00d2ff; border-radius: 50%; box-shadow: 0 0 30px #00d2ff; display: flex; justify-content: center; align-items: center;">
            <div style="width: 120px; height: 120px; border: 2px dashed #ff3366; border-radius: 50%;"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# قسم الإدخال الصوتي
st.subheader("Voice Command Protocol")
audio = mic_recorder(
    start_prompt="🎙️ Press to Speak",
    stop_prompt="⏹️ Stop Recording",
    key='jarvis_mic'
)

if audio:
    st.audio(audio['bytes'])
    st.success("Indeed, Sir. Audio signal received and verified.")
    response = ask_jarvis("Acknowledge my audio signal and report status.")
    st.markdown(f"<div class='jarvis-box'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)

# خانة إدخال نصي لمحادثة جارفيس مباشرة
st.subheader("Direct Neural Link")
user_text = st.text_input("Transmit text instruction to Jarvis:", placeholder="Type your command here, Sir...")
if user_text:
    response = ask_jarvis(user_text)
    st.markdown(f"<div class='jarvis-box'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)

# أزرار التحكم السريعة
st.subheader("Control Panel")

col1, col2 = st.columns(2)
with col1:
    if st.button("🎵 Initialize Playlist (Mood Fire)"):
        response = ask_jarvis("Acknowledge initialization of the Mood Fire playlist.")
        st.markdown(f"<div class='jarvis-box'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)

with col2:
    if st.button("💬 Transmit WhatsApp Dispatch"):
        st.markdown(f"<div class='jarvis-box'><b>J.A.R.V.I.S.:</b> Awaiting your precise dictation for service dispatch, Sir.</div>", unsafe_allow_html=True)

if st.button("❤️ Synchronize Biometrics (Samsung Health)"):
    response = ask_jarvis("Report on biometric synchronization status.")
    st.markdown(f"<div class='jarvis-box'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)
