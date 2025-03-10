import speech_recognition as sr
import streamlit as st


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