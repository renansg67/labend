import time
import streamlit as st

def stream_text(text, delay=0.02):
    """
    Gera palavras uma por uma a partir de um texto.
    
    Args:
        text (str): O texto completo a ser renderizado.
        delay (float): O tempo de espera entre cada palavra.
    """
    for word in text.split(" "):
        yield word + " "
        time.sleep(delay)

# --- Como usar ---
texto_exemplo = "Olá! Eu sou uma função generalizada que pode ler qualquer string."

if st.button("Stream Texto"):
    st.write_stream(stream_text(texto_exemplo))