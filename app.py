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
    h1, h2 {
        color: #00d2ff;
        text-align: center;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 15px #00d2ff;
    }
    .jarvis-status {
        background-color: #0a192f;
        border: 1px solid #00d2ff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 0 25px rgba(0, 210, 255, 0.3);
        margin-top: 25px;
        color: #ffffff;
        font-family: 'Courier New', monospace;
        text-align: center;
        font-size: 19px;
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
st.markdown("<h1>J.A.R.V.I.S. ACTIVE MIC PROTOCOL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff3366;'>Neural Audio Stream Active, Sir</p>", unsafe_allow_html=True)

# قلب نظام الطاقة التفاعلي (مظهر سيبراني بحت)
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; margin: 30px 0;">
        <div style="width: 210px; height: 210px; border: 4px solid #00d2ff; border-radius: 50%; box-shadow: 0 0 45px #00d2ff; display: flex; justify-content: center; align-items: center;">
            <div style="width: 140px; height: 140px; border: 2px dashed #ff3366; border-radius: 50%; animation: rotation 20s infinite linear;"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# الميكروفون المباشر بدون أزرار حشو قديمة
st.markdown("<h3 style='text-align: center; font-size: 18px; color: #00d2ff;'>Transmit Voice Command Below:</h3>", unsafe_allow_html=True)
audio = mic_recorder(
    start_prompt="🔴 Start Voice Link",
    stop_prompt="⏹️ Disconnect & Process",
    key='live_mic_core'
)

if audio:
    # محاكاة تلقي واستجابة النظام الصوتي فور التسجيل
    signal_prompt = "Acknowledge live voice transmission and report combat readiness, Sir."
    response, lang_type = ask_jarvis(signal_prompt)
    
    st.markdown(f"<div class='jarvis-status'><b>J.A.R.V.I.S.:</b> {response}</div>", unsafe_allow_html=True)
    speak_response(response, lang=lang_type)
