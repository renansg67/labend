import streamlit as st
import plotly.express as px
from assets.att import calcular_curvas_atenuacao

col1, col2, col3 = st.columns([.25, 3, 1.5])

col2.markdown("## Fatores que afetam o coeficiente de atenuação ($\\alpha$)")

col2.markdown("##### 📜 Teoria da Lei de Potência: $\\alpha = a \\cdot f^b$")

col2.markdown("""
A atenuação ultrassônica ($\\alpha$) é a perda de energia da onda em função da distância percorrida. Ela é descrita pela **Lei de Potência**, onde o coeficiente de atenuação é dependente da frequência ($f$).
""")

# Fórmula em display
col2.latex(r'''
\alpha = a \cdot f^b
''')

col2.markdown("""
* **$\\alpha$ (Atenuação):** A perda de energia por unidade de distância ($\\text{dB/cm}$).
* **$f$ (Frequência):** A frequência da onda ($\\text{MHz}$).
* **$a$ (Coeficiente):** Reflete a atenuação em $1 \\text{ MHz}$ (propriedade intrínseca do material).
* **$b$ (Expoente):** O fator mais importante, pois define o **mecanismo físico** dominante de perda de energia.
""")

col2.markdown("##### Mecanismos Físicos e o Expoente $b$")

col2.markdown("""
O expoente $b$ é determinado pela forma como a energia da onda é dissipada no meio (Absorção ou Espalhamento).
""")

col1, col2, col3, col4 = st.columns([.25, 1.5, 1.5, 1.5])

col4.info("💡 **Dica de END:** Quanto maior o valor de $b$, mais crítico é usar frequências baixas para garantir a penetração profunda no material.")

with col2:
    st.info("###### Caso 1: $b \\approx 1$ (Absorção)")
    st.markdown("""
    * **Mecanismo:** Conversão de energia sônica em calor devido à viscosidade do meio (Absorção Viscosa).
    * **Relação:** Linear ($\\alpha$ dobra quando $f$ dobra).
    * **Típico em:** **Tecidos Moles** (músculo, gordura) e fluidos.
    """)
    
with col3:
    st.warning("###### Caso 2: $b \\approx 2$ a $4$ (Espalhamento)")
    st.markdown("""
    * **Mecanismo:** Dispersão da energia da onda por heterogeneidades internas (grãos, poros, fibras).
    * **Relação:** Exponencialmente mais alta.
    * **Típico em:** **Concreto** ($b \\approx 4$), **Metais** com granulação grossa, **Madeira** ($b \\approx 2.5$) e Compósitos. 
    """)

col1, col2, col3 = st.columns([.25, 3, 1.5])

col2.markdown("""
O gráfico Log-Log (ambos eixos logarítmicos) é útil pois transforma a relação de potência em uma linha reta ($\\log(\\alpha) = \\log(a) + b \\cdot \\log(f)$), onde a **inclinação da linha é igual ao expoente $b$**.
""")

col1, col2, col3 = st.columns([.25, 3, 1.5])

# 1. Carrega os dados de forma enxuta
df_curvas = calcular_curvas_atenuacao(frequencia_max_mhz=15, pontos=100)

fig = px.line(
    df_curvas, 
    x='Frequência (MHz)', 
    y='Atenuação (dB/cm)', 
    color='Material', 
    line_dash='Material',
    log_y=True,     # Eixo Y logarítmico
    log_x=True,     # <--- ADICIONE ESTE PARÂMETRO! Eixo X logarítmico
    title='Atenuação Ultrassônica em Diversos Materiais (α vs. f) - Gráfico Log-Log',
    hover_data=['Dependência (b)', 'Coeficiente (a)']
)

# 3. MUDANÇA DA POSIÇÃO DA LEGENDA AQUI
fig.update_layout(
    yaxis_title="Coeficiente de Atenuação α (dB/cm) - Escala Logarítmica",
    
    # Configurações para mover a legenda para baixo e centralizar
    legend=dict(
        orientation="h",        # Define a orientação horizontal
        yanchor="bottom",       # Âncora no fundo
        y=-0.3,                 # Posição y (0 é a linha do gráfico, -0.3 coloca abaixo)
        xanchor="center",       # Âncora no centro horizontal
        x=0.5                   # Posição x (0.5 é o centro)
    ),
    height=600 # Opcional: Aumentar a altura total para compensar o espaço inferior
)

col2.plotly_chart(fig, use_container_width=True)