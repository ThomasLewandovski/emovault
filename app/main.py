import streamlit as st
import sys
import os
import subprocess
from dotenv import load_dotenv

# 添加项目根目录到路径，使用相对路径提高可移植性
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

# 加载.env文件中的环境变量
load_dotenv(os.path.join(root_dir, '.env'))

from app.dialogue_model import DeepSeekDialogueGenerator
from app.sentiment_analysis import analyze_sentiment
from app.knowledge_base import get_best_advice
import app.SpeechRecognition as sr

# 从环境变量获取API密钥
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    st.error("错误：未设置DEEPSEEK_API_KEY环境变量，请在.env文件中设置或通过系统环境变量设置后再运行")
    st.stop()

# 初始化对话生成器
dialogue_generator = DeepSeekDialogueGenerator(api_key)

# 设置 Streamlit 页面
st.set_page_config(page_title="EmoVault", layout="wide")

st.title("🌿 EmoVault")
st.write("你的私人情绪树洞")

# 初始化聊天记录
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 语音识别功能
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        st.write("请开始说话...")
        audio = recognizer.listen(source)

    try:
        transcript = recognizer.recognize_google(audio, language='zh-CN')
        st.write(f"您说的是: {transcript}")
        return transcript
    except sr.RequestError:
        st.write("无法连接到语音识别服务。")
    except sr.UnknownValueError:
        st.write("未能识别您的语音。")
    return None

# 获取用户输入
user_input = st.chat_input("💬 说出你的感受吧，我在听……")

if st.button("使用语音输入"):
    user_input = recognize_speech_from_mic()

if user_input:
    # **分析用户情绪**
    sentiment_data = analyze_sentiment(user_input)
    sentiment_label = max(sentiment_data, key=sentiment_data.get)  # 最高概率的情绪
    sentiment_score = sentiment_data[sentiment_label]  # 取该情绪的分数

    # **格式化情绪分析结果**
    sentiment_text = ", ".join([f"{key}: {value:.2f}%" for key, value in sentiment_data.items()])
    primary_emotion_text = f"🧠 **主要情绪：{sentiment_label} {sentiment_score:.2f}%**"

    # **在对话记录中增加情绪分析结果**
    st.session_state.chat_history.append(("📊 情绪分析", f"{primary_emotion_text}\n📈 **完整分析：** {sentiment_text}, 请根据我的心情分析结果生成更能安慰我的话"))

    # **生成优化回复**
    response = dialogue_generator.generate(
        f"用户输入：{user_input}，用户情绪：{sentiment_label}（{sentiment_score:.2f}%)",
        max_tokens=500,
        temperature=0.7
    )

    # **提供个性化建议**
    advice = get_best_advice(sentiment_label)
    st.session_state.chat_history.append(("🎯 建议", advice))

    # **保存聊天记录**
    st.session_state.chat_history.append(("User", user_input))
    st.session_state.chat_history.append(("EmoVault", response))

# **显示聊天记录**
st.subheader("📜 对话记录")
for role, text in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(text)