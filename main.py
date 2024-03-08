import streamlit as st
import whisper

model = whisper.load_model("base")
result = model.transcribe("input_1.mp3")
st.write(result["text"])