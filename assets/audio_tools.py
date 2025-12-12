import numpy as np

def gerar_pulso_amortecido(frequencia_hz, duracao_seg, amplitude_max, taxa_amostragem, decaimento_rapidez, atraso_seg=0):
    """
    Gera um pulso senoidal amortecido (sonificação de um pulso ultrassônico) 
    usando NumPy para ser reproduzido pelo st.audio.

    Atenção: A frequência (frequencia_hz) é a frequência de sonificação audível.
    """
    # 1. Cria a base temporal
    # Garante que o array tenha espaço suficiente para o pulso e o atraso
    total_duration = duracao_seg + atraso_seg
    t = np.linspace(0, total_duration, int(taxa_amostragem * total_duration), False)
    
    # 2. Gera o envelope de amortecimento
    envelope = np.zeros_like(t)
    
    # Índice onde o pulso começa
    start_index = int(taxa_amostragem * atraso_seg)
    
    # Base temporal apenas para o pulso
    t_pulso = t[start_index:] - atraso_seg
    
    # Aplica o decaimento exponencial
    envelope_pulso = np.exp(-decaimento_rapidez * t_pulso)
    
    # Insere o envelope na matriz completa (com silêncio inicial, se houver)
    envelope[start_index:] = envelope_pulso
    
    # 3. Gera a onda senoidal (frequência de sonificação)
    onda_senoidal = amplitude_max * np.sin(2 * np.pi * frequencia_hz * t)
    
    # 4. Sinal final (onda x envelope)
    sinal_final = onda_senoidal * envelope
    
    return sinal_final