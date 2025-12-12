import numpy as np
import plotly.graph_objects as go
from scipy.fft import fft, fftfreq 

def plot_fft_analysis(sinal_tempo, fs, titulo):
    """
    Gera dois gráficos Plotly (Domínio do Tempo e Domínio da Frequência) 
    para um dado sinal.

    Parâmetros:
    - sinal_tempo (np.array): O array de dados do sinal no domínio do tempo.
    - fs (int): Taxa de amostragem (Hz).
    - titulo (str): Título base para os gráficos.
    
    Retorna:
    - tuple: (fig_tempo, fig_freq)
    """
    N = len(sinal_tempo)
    T = 1.0 / fs
    t = np.linspace(0.0, N*T, N, endpoint=False)
    
    # 1. Domínio da Frequência (FFT)
    yf = fft(sinal_tempo)
    xf = fftfreq(N, T)[:N//2]
    
    # Obtém a magnitude (descartando a parte simétrica e o componente DC)
    magnitude = 2.0/N * np.abs(yf[0:N//2])
    
    # ----------------------------------------------------
    # --- GRÁFICO 1: DOMÍNIO DO TEMPO ---
    # ----------------------------------------------------
    fig_tempo = go.Figure()
    fig_tempo.add_trace(go.Scatter(x=t, y=sinal_tempo, 
                                   mode='lines', 
                                   name='Amplitude',
                                   line=dict(color='orange', width=1.5)))
    
    fig_tempo.update_layout(
        title=f'{titulo} - Domínio do Tempo',
        xaxis_title='Tempo (s)',
        yaxis_title='Amplitude',
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        template="plotly_white"
    )

    # ----------------------------------------------------
    # --- GRÁFICO 2: DOMÍNIO DA FREQUÊNCIA (ESPECTRO) ---
    # ----------------------------------------------------
    fig_freq = go.Figure()
    fig_freq.add_trace(go.Bar(x=xf, y=magnitude, 
                              name='Magnitude',
                              marker_color='royalblue'))
    
    # Limita o eixo X para melhor visualização das frequências relevantes
    # Procura a frequência máxima que tem magnitude significativa (ex: > 0.05)
    indices_significativos = np.where(magnitude > 0.05)[0]
    if indices_significativos.size > 0:
        freq_max_plot = xf[indices_significativos[-1]] * 1.5
    else:
        freq_max_plot = 50 # Padrão se não houver picos claros
         
    fig_freq.update_layout(
        title=f'{titulo} - Domínio da Frequência (FFT)',
        xaxis_title='Frequência (Hz)',
        yaxis_title='Magnitude',
        xaxis_range=[0, freq_max_plot],
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        template="plotly_white"
    )

    return fig_tempo, fig_freq