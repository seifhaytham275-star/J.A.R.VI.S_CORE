import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq
from gtts import gTTS
import os

# إعدادات صفحة جارفيس السحابية
st.set_page_config(
    page_title="J.A.R.V.I.S. Cloud Core",
    page_icon="🤖",
    layout="centered"
)

# تصميم الواجهة السيبرانية (Stark HUD)
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

# قراءة مفتاح Groq بأمان تام من إعدادات الـ Secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

def speak_response(text, lang='en'):
    """دالة نطق الرد: إنجليزي بصوت بريطاني صارم أو مصري بلهجة منضبطة"""
    try:
        if lang == 'ar':
            tts = gTTS(text=text, lang='ar')
        else:
            tts = gTTS(text=text, lang='en', tld='co.uk') # لكنة بريطانية بامتياز
            
        audio_file = "jarvis_voice.mp3"
        tts.save(audio_file)
        st.audio(audio_file, format='audio/mp3', autoplay=True)
    except Exception as e:
        pass

def ask_jarvis(prompt_text):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        
        # كشف لغة الكلام لتحديد الشخصية المناسبة
        is_arabic = any(("\u0600" <= c <= "\u06ff") or ("\u0750" <= c <= "\u077f") for c in prompt_text)
        
        if is_arabic:
            system_prompt = "أنت J.A.R.V.I.S. المساعد الذكي الخاص بلواء العمليات. تتحدث باللهجة المصرية ولكن بأسلوب محترم، صارم، وعسكري منضبط، وتناديني دائماً بـ 'يا باشا' أو 'يا لواء'."
        else:
            system_prompt = "You are J.A.R.V.I.S., Tony Stark's strict, highly professional British AI butler. You never joke, you are dead serious, formal, and precise. Address the user with absolute respect as 'Sir'. Keep your responses concise and disciplined."

        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_text}
            ],
            temperature=0.3,
        )
        reply = completion.choices[0].message.content
        return reply, ('ar' if is_arabic else 'en')
    except Exception as e:
        return "System Error, Sir: Neural core connection failed.", 'en'

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

# خانة إدخال نصي (تتعرف تلقائياً لو كتبت إنجليزي أو مصري)
st.subheader("Direct Neural Link")
user_text = st.text_input("Transmit text instruction to Jarvis:", placeholder="Type in English or Egyptian Arabic, Sir...")
if user_text:
    response, lang_type = ask_jarvis(user_text)
    st.markdown(f"<div class='jarvis-box'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)
    speak_response(response, lang=lang_type)

# أزرار التحكم السريعة
st.subheader("Control Panel")

col1, col2 = st.columns(2)
with col1:
    if st.button("🎵 Initialize Playlist (Mood Fire)"):
        response, lang_type = ask_jarvis("Initialize Mood Fire playlist, Sir.")
        st.markdown(f"<div class='jarvis-box'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)
        speak_response(response, lang=lang_type)

with col2:
    if st.button("💬 Transmit WhatsApp Dispatch"):
        response, lang_type = ask_jarvis("أمرك يا باشا، في انتظار توجيهاتك للرسالة.")
        st.markdown(f"<div class='jarvis-box'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)
        speak_response(response, lang=lang_type)

if st.button("❤️ Synchronize Biometrics (Samsung Health)"):
    response, lang_type = ask_jarvis("Report on biometric synchronization status, Sir.")
    st.markdown(f"<div class='jarvis-box'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)
    speak_response(response, lang=lang_type)
