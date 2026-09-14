import streamlit as st
import google.generativeai as genai 
from streamlit_mic_recorder import speech_to_text

import os
genai.configure(api_key=os.getenv("TU-CLAVE-AQUI"))
modelo=genai.GenerativeModel("gemini-3.6-flash")

st.title("BlackPink IA")

pregunta = st.text_input("Escribe tu pregunta:")

st.write("Presiona el boton del microfono y habla")
voz_texto= speech_to_text(language="es-ES", use_container_width=True)

if voz_texto:
    pregunta = voz_texto
    st.write("Dijiste: " + pregunta)

hablar=st.checkbox("Responder con voz")

if st.button("Preguntar") and pregunta:
    respuesta = modelo.generate_content(pregunta)
    st.write(respuesta.text) 
    if hablar:
        import pyttsx3
        voz=pyttsx3.init()
        voz.say(respuesta.text)
        voz.runAndWait()
