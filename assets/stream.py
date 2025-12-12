import time
import streamlit as st

def stream_text(text, delay):
    """
    Gera palavras uma por uma a partir de um texto.
    
    Args:
        text (str): O texto completo a ser renderizado.
        delay (float): O tempo de espera entre cada palavra.
    """
    for word in text.split(" "):
        yield word + " "
        time.sleep(delay)

    return st.write_stream(stream_text(text))