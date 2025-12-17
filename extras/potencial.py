import streamlit as st
import plotly.graph_objects as go
import numpy as np
import assets.pot as cl 

def exibir_interface_corrosao():
    st.set_page_config(page_title="Simulador de Corrosão", layout="wide")
    
    st.header("⚡ Simulador de Potencial de Corrosão")
    st.markdown("Análise baseada na norma **ASTM C876:2022** utilizando elétrodo de referência de Cobre/Sulfato de Cobre ($\\text{Cu/CuSO}_4$).")

    # --- CONFIGURAÇÃO E CENÁRIOS ---
    opcoes = [
        "Manual", 
        "Integridade Preservada", 
        "Corrosão por Pitting (Localizada)", 
        "Corrosão Severa (Na Armadura)"
    ]
    
    # Define "Corrosão Severa" como padrão (index 3)
    cenario = st.selectbox("Selecione o cenário de análise:", opcoes, index=3)

    # Malha fixa 5x5
    LINHAS, COLUNAS = 5, 5
    mid_y, mid_x = 2, 2  # Posição central da armadura

    col_input, col_viz = st.columns([1.2, 1.8])

    with col_input:
        st.subheader("Entrada de Dados (mV)")
        st.caption("Edição bloqueada nos cenários predefinidos. Use 'Manual' para editar.")

        grid_input = []
        is_disabled = (cenario != "Manual")

        for i in range(LINHAS):
            cols = st.columns(COLUNAS)
            row_data = []
            for j in range(COLUNAS):
                with cols[j]:
                    # Lógica de posicionamento da armadura para os cenários
                    na_armadura = (i == mid_y or j == mid_x)
                    no_cruzamento = (i == mid_y and j == mid_x)

                    # --- GERAÇÃO AUTOMÁTICA DE VALORES ---
                    if cenario == "Integridade Preservada":
                        val_default = np.random.randint(-160, -80)
                    elif cenario == "Corrosão por Pitting (Localizada)":
                        if no_cruzamento: val_default = np.random.randint(-520, -450)
                        elif na_armadura: val_default = np.random.randint(-280, -210)
                        else: val_default = np.random.randint(-160, -90)
                    elif cenario == "Corrosão Severa (Na Armadura)":
                        if na_armadura: val_default = np.random.randint(-580, -450)
                        else: val_default = np.random.randint(-300, -220)
                    else: # Manual
                        val_default = -200

                    val = st.number_input(
                        f"L{i+1}C{j+1}", 
                        value=val_default, 
                        step=5, 
                        key=f"input_{cenario}_{i}_{j}", 
                        label_visibility="collapsed",
                        disabled=is_disabled
                    )
                row_data.append(val)
            grid_input.append(row_data)
        
        matriz_np = np.array(grid_input)

    with col_viz:
        st.subheader("Mapa Equipotencial Suavizado")
        
        x_coords = np.arange(COLUNAS)
        y_coords = np.arange(LINHAS)

        fig = go.Figure()

        # Heatmap de Contorno
        fig.add_trace(go.Contour(
            z=matriz_np,
            x=x_coords,
            y=y_coords,
            colorscale=[[0, 'red'], [0.4, 'yellow'], [1, 'green']],
            zmin=-600, zmax=0,
            opacity=0.8,
            contours=dict(coloring='heatmap', showlabels=True),
            colorbar=dict(title="DDP (mV)")
        ))

        # Desenho das Barras de Armadura (Fixas no centro da malha 5x5)
        # Barra Vertical
        fig.add_shape(type="rect", x0=1.9, x1=2.1, y0=-0.5, y1=4.5,
                      fillcolor="rgba(60,60,60,0.6)", line_color="black", layer="below")
        # Barra Horizontal
        fig.add_shape(type="rect", x0=-0.5, x1=4.5, y0=1.9, y1=2.1,
                      fillcolor="rgba(60,60,60,0.6)", line_color="black", layer="below")

        fig.update_layout(
            xaxis=dict(side="top", tickvals=x_coords, ticktext=[f"C{j+1}" for j in x_coords]),
            yaxis=dict(autorange='reversed', tickvals=y_coords, ticktext=[f"L{i+1}" for i in y_coords]),
            width=500, height=480,
            margin=dict(l=10, r=10, t=50, b=10),
            template="plotly_white"
        )
        
        st.plotly_chart(fig, use_container_width=True)

    # --- DIAGNÓSTICO E TABELA DE REFERÊNCIA ---
    st.divider()
    
    u_min = np.min(matriz_np)
    
    # Lógica de Status Dinâmico
    if u_min > -200:
        label_status, cor_delta, msg_delta = "ESTÁVEL", "normal", "Baixo Risco"
    elif -350 <= u_min <= -200:
        label_status, cor_delta, msg_delta = "ATENÇÃO", "off", "Risco Incerto"
    else:
        label_status, cor_delta, msg_delta = "CRÍTICO", "inverse", "Alto Risco"

    c1, c2 = st.columns([1, 1.5])

    with c1:
        st.metric(
            label=f"Estado da Estrutura: {label_status}", 
            value=f"{u_min} mV", 
            delta=msg_delta, 
            delta_color=cor_delta
        )
        st.info(f"**Parecer Técnico:** {cl.interpretar_potencial(u_min)}")

    with c2:
        st.markdown("**Valores de Referência (ASTM C876)**")
        tabela_ref = {
            "Potencial de Elétrodo ($\\text{mV}$)": ["$U > -200$", "$-200$ a $-350$", "$U < -350$"],
            "Probabilidade de Corrosão": ["5% (Desprezível)", "Duvidosa", "95% (Ativa)"]
        }
        st.table(tabela_ref)

if __name__ == "__main__":
    exibir_interface_corrosao()