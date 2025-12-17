import streamlit as st
import plotly.graph_objects as go
import numpy as np
import assets.hip as hl

def exibir_interface_hipsometria():
    st.header("Hipsometria")

    # --- TABELA DE INSTRUÇÕES ---
    st.markdown("""
    | Cenário Selecionado | Visualização de Campo | Regra de Ângulo |
    | :--- | :--- | :--- |
    | **Terreno Plano** | Olhar para Cima (Topo) e para Baixo (Base) | Insira valores positivos |
    | **Aclive (Subida)** | Olhar para Cima para ambos os pontos | Insira valores positivos |
    | **Declive (Descida)** | Olhar para Baixo para ambos os pontos | Insira valores positivos |
    """)

    col_input, col_viz = st.columns([1, 2])

    with col_input:
        st.subheader("Parâmetros")
        
        cenario = st.selectbox(
            "Selecione o cenário de visada:",
            options=[
                "Terreno Plano / Olho no Meio",
                "Observador Abaixo da Base (Aclive)",
                "Observador Acima do Topo (Declive)"
            ]
        )
        
        dist_L = st.number_input("Distância Horizontal L (m)", value=15.0, min_value=1.0)
        
        # min_value=0.0 impede a inserção de números negativos
        ang_alpha = st.number_input("Ângulo para o Topo α (graus)", value=30.0, min_value=0.0)
        ang_beta = st.number_input("Ângulo para a Base β (graus)", value=10.0, min_value=0.0)

        h_total = hl.calcular_altura_hipsometro(dist_L, ang_alpha, ang_beta, cenario)
        st.metric("Altura Total Calculada", f"{h_total:.2f} m")

    with col_viz:
        fig = go.Figure()
        # --- 2. LÓGICA DE POSICIONAMENTO DA ÁRVORE (Mantida) ---
        h_a = dist_L * np.tan(np.radians(ang_alpha))
        h_b = dist_L * np.tan(np.radians(ang_beta))

        if cenario == "Terreno Plano / Olho no Meio":
            y_topo, y_base = h_a, -h_b
        elif cenario == "Observador Abaixo da Base (Aclive)":
            y_topo, y_base = h_a, h_b
        else: # Declive
            y_topo, y_base = -h_a, -h_b

        y_min, y_max = min(y_topo, y_base), max(y_topo, y_base)

        # --- 3. SOLO (RETÂNGULO SOB A BASE DA ÁRVORE) ---

        # --- 4. ÁRVORE (TRONCO E COPA) ---
        fig.add_trace(go.Scatter(x=[0, 0], y=[y_min, y_max], mode='lines', 
                                line=dict(color='saddlebrown', width=10), name="Tronco"))

        altura_copa = h_total * 0.4
        fig.add_trace(go.Scatter(
            x=[-2.5, 0, 2.5, -2.5], 
            y=[y_max - altura_copa, y_max, y_max - altura_copa, y_max - altura_copa], 
            fill="toself", line=dict(color='forestgreen'), showlegend=False
        ))

        # --- 5. OBSERVADOR E VISADAS ---
        fig.add_trace(go.Scatter(x=[-dist_L], y=[0], mode='markers', 
                                marker=dict(symbol='circle', size=15, color='black'), name="Observador"))
        fig.add_trace(go.Scatter(x=[-dist_L, 5], y=[0, 0], 
                                line=dict(color='gray', dash='dash', width=1), showlegend=False))

        fig.add_trace(go.Scatter(x=[-dist_L, 0], y=[0, y_topo], line=dict(color='red'), name="Visada α"))
        fig.add_trace(go.Scatter(x=[-dist_L, 0], y=[0, y_base], line=dict(color='blue'), name="Visada β"))

        fig.update_layout(
            xaxis=dict(
                visible=True,           # Tornamos o eixo visível para ver as grades
                showticklabels=False,   # Mas escondemos os números/rótulos
                range=[-dist_L-5, 10],
                showgrid=True,          # Ativa gridlines verticais
                gridcolor='rgba(255, 255, 255, 0.3)', # Linhas brancas suaves
                zeroline=False
            ),
            yaxis=dict(
                title="Altura (m)", 
                showgrid=True,          # Ativa gridlines horizontais
                gridcolor='rgba(255, 255, 255, 0.3)', # Linhas brancas suaves
                scaleanchor="x", 
                scaleratio=1,
                zeroline=True,          # Mantém a linha do horizonte (0) destacada
                zerolinecolor='gray'
            ),
            template="plotly_white",
            height=550,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    exibir_interface_hipsometria()