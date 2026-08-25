import streamlit as st
from streamlit_mic_recorder import mic_recorder

# إعدادات صفحة جارفيس السحابية
st.set_page_config(
    page_title="J.A.R.V.I.S. Cloud Core",
    page_icon="🤖",
    layout="centered"
)

# تصميم الواجهة بلغة الـ CSS المخصصة لتكون سوداء بنيون أزرق (ستايل ستارك)
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
    </style>
""", unsafe_allow_html=True)

# محتوى الواجهة
st.markdown("<h1>J.A.R.V.I.S. CLOUD PROTOCOL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff3366;'>Systems Online - Global Cloud Server Active</p>", unsafe_allow_html=True)

# دائرة الطاقة التفاعلية
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; margin: 40px 0;">
        <div style="width: 200px; height: 200px; border: 4px solid #00d2ff; border-radius: 50%; box-shadow: 0 0 30px #00d2ff; display: flex; justify-content: center; align-items: center;">
            <div style="width: 140px; height: 140px; border: 2px dashed #ff3366; border-radius: 50%;"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# قسم الإدخال الصوتي (مايك جارفيس)
st.subheader("Voice Command Protocol")
audio = mic_recorder(
    start_prompt="🎙️ اضغط للتحدث مع جارفيس",
    stop_prompt="⏹️ إيقاف التسجيل",
    key='jarvis_mic'
)

if audio:
    st.audio(audio['bytes'])
    st.success("Jarvis: Audio signal received, Sir. Processing command...")

# أزرار التحكم السريعة
st.subheader("Control Panel")

if st.button("🎵 تشغيل بلاي ليست (Mood Fire)"):
    st.success("Jarvis: Initializing Mood Fire playlist, Sir.")

if st.button("💬 إرسال رسالة واتساب"):
    st.info("Jarvis: What is your message, Sir?")

if st.button("❤️ فحص المؤشرات الحيوية (Samsung Health)"):
    st.warning("Jarvis: Accessing cloud biometrics... Heart rate and sleep status synchronized.")
