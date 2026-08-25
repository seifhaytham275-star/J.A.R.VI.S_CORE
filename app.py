import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq
from gtts import gTTS
import os

# إعدادات صفحة جارفيس السيبرانية
st.set_page_config(
    page_title="J.A.R.V.I.S. Neural Voice Core",
    page_icon="🤖",
    layout="centered"
)

# تصميم واجهة ستارك الصافية
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
        text-shadow: 0 0 15px #00d2ff;
    }
    .stButton>button {
        background-color: transparent;
        color: #00d2ff;
        border: 2px solid #00d2ff;
        border-radius: 10px;
        width: 100%;
        font-weight: bold;
        box-shadow: 0 0 10px #00d2ff;
        font-family: 'Courier New', monospace;
    }
    .stButton>button:hover {
        background-color: #00d2ff;
        color: #050b14;
    }
    .jarvis-status {
        background-color: #0a192f;
        border: 1px solid #00d2ff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 0 25px rgba(0, 210, 255, 0.3);
        margin-top: 20px;
        color: #ffffff;
        font-family: 'Courier New', monospace;
        text-align: center;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# قراءة مفتاح Groq بأمان تام
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

def speak_response(text, lang='en'):
    """دالة نطق الرد: بريطاني فخم للإنجليزي، وعسكري منضبط للمصري"""
    try:
        if lang == 'ar':
            tts = gTTS(text=text, lang='ar')
        else:
            tts = gTTS(text=text, lang='en', tld='co.uk')
            
        audio_file = "jarvis_voice.mp3"
        tts.save(audio_file)
        st.audio(audio_file, format='audio/mp3', autoplay=True)
    except Exception as e:
        pass

def ask_jarvis(prompt_text):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        
        # كشف لغة الكلام تلقائياً (إنجليزي أو مصري)
        is_arabic = any(("\u0600" <= c <= "\u06ff") or ("\u0750" <= c <= "\u077f") for c in prompt_text)
        
        if is_arabic:
            system_prompt = "أنت J.A.R.V.I.S. المساعد الذكي الخاص بلواء العمليات. تتحدث باللهجة المصرية بأسلوب محترم، صارم، وعسكري منضبط، وتناديني دائماً بـ 'يا باشا' أو 'يا لواء'."
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

# عنوان الهولوغرام
st.markdown("<h1>J.A.R.V.I.S. ACTIVE PROTOCOL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff3366;'>Neural Audio Stream Active, Sir</p>", unsafe_allow_html=True)

# دائرة الطاقة التفاعلية
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; margin: 25px 0;">
        <div style="width: 180px; height: 180px; border: 4px solid #00d2ff; border-radius: 50%; box-shadow: 0 0 35px #00d2ff; display: flex; justify-content: center; align-items: center;">
            <div style="width: 120px; height: 120px; border: 2px dashed #ff3366; border-radius: 50%;"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# إضافة خانة إدخال نصي ذكية وسريعة (عشان تكتب أو تقولي اللي في دماغك ويرد عليك فوراً بذكاء وبدون ردود محفوظة)
st.markdown("<h3 style='text-align: center; font-size: 16px; color: #00d2ff;'>Direct Neural Command Link:</h3>", unsafe_allow_html=True)
user_input = st.text_input("", placeholder="Type your instruction here, Sir (e.g., How are you? / عامل إيه يا جارفيس)...", key="neural_input")

if user_input:
    response, lang_type = ask_jarvis(user_input)
    st.markdown(f"<div class='jarvis-status'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)
    speak_response(response, lang=lang_type)

# لوحة الاختصارات السريعة (الواتساب، البلاي ليست، وسامسونج هيلث)
st.markdown("<h3 style='text-align: center; margin-top: 30px; font-size: 18px;'>Tactical Control Shortcuts</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("🎵 Mood Fire Playlist"):
        response, lang_type = ask_jarvis("Initialize Mood Fire playlist and report status, Sir.")
        st.markdown(f"<div class='jarvis-status'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)
        speak_response(response, lang=lang_type)

with col2:
    if st.button("💬 WhatsApp Dispatch"):
        response, lang_type = ask_jarvis("أمرك يا باشا، جاهز لتنفيذ وإرسال رسالة الواتساب بدقة.")
        st.markdown(f"<div class='jarvis-status'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)
        speak_response(response, lang=lang_type)

if st.button("❤️ Synchronize Samsung Health"):
    response, lang_type = ask_jarvis("Report on Samsung Health biometric synchronization status, Sir.")
    st.markdown(f"<div class='jarvis-status'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)
    speak_response(response, lang=lang_type)
