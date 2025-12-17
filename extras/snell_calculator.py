import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Snell Explorer NDT")

st.title("🔦 Refração Acústica e Transmissão de Energia")
st.caption("Análise de interface baseada na Lei de Snell e Impedância Acústica")

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Parâmetros de Entrada")
    
    st.subheader("🌐 Meio 1 (Incidente)")
    v1 = st.number_input("$v_1$ (m/s)", value=1500.0, step=100.0)
    rho1 = st.number_input(r"$\rho_1$ (kg/m³)", value=1000.0, step=50.0)
        
    st.subheader("🌐 Meio 2 (Refratado)")
    v2 = st.number_input("$v_2$ (m/s)", value=3000.0, step=100.0)
    rho2 = st.number_input(r"$\rho_2$ (kg/m³)", value=2700.0, step=50.0)
    
    st.divider()
    theta1_deg = st.slider(r"Ângulo de Incidência $\theta_1$ (°)", 0.0, 90.0, 20.0, 0.5)

# --- PROCESSAMENTO TÉCNICO ---
Z1 = rho1 * v1
Z2 = rho2 * v2

# Coeficientes (Incidência Normal)
r_coeff = (Z2 - Z1) / (Z2 + Z1)
R = r_coeff**2
T = 1 - R

# Ângulo Crítico
sin_crit = v1 / v2 if v1 < v2 else None
ang_critico = np.degrees(np.arcsin(sin_crit)) if sin_crit and sin_crit <= 1 else None

# Snell
sin_theta2 = (v2 / v1) * np.sin(np.radians(theta1_deg))
reflexao_total = sin_theta2 > 1.0
theta2_deg = np.degrees(np.arcsin(sin_theta2)) if not reflexao_total else None

# --- INTERFACE PRINCIPAL ---
tab1, tab2 = st.tabs(["📊 Simulação Visual", "📖 Teoria e Fórmulas"])

with tab1:
    col_viz, col_info = st.columns([2, 1], gap="large")
    
    with col_viz:
        # --- CRIAÇÃO DO GRÁFICO PLOTLY ---
        fig = go.Figure()
        length = 10
        
        # 1. Áreas dos Meios (Fundo sutil)
        fig.add_hrect(y0=0, y1=12, fillcolor="blue", opacity=0.05, line_width=0, name="Meio 1")
        fig.add_hrect(y0=-12, y1=0, fillcolor="orange", opacity=0.05, line_width=0, name="Meio 2")
        
        # 2. Linha da Interface e Normal
        fig.add_hline(y=0, line=dict(color="black", width=2))
        fig.add_vline(x=0, line=dict(color="gray", width=1, dash="dash"))

        # 3. Raio Incidente
        x_inc = -length * np.sin(np.radians(theta1_deg))
        y_inc = length * np.cos(np.radians(theta1_deg))
        fig.add_trace(go.Scatter(x=[x_inc, 0], y=[y_inc, 0], mode='lines',
                                 line=dict(color='blue', width=4), name=r'Raio Incidente'))

        # 4. Raio Refletido (Energia R)
        x_ref = length * np.sin(np.radians(theta1_deg))
        y_ref = length * np.cos(np.radians(theta1_deg))
        fig.add_trace(go.Scatter(x=[0, x_ref], y=[0, y_ref], mode='lines',
                                 line=dict(color='red', width=max(1, 4 * R), dash='dot'), 
                                 name=f'Reflexão ({R*100:.1f}%)'))

        # 5. Raio Refratado ou Mensagem de Reflexão Total
        if not reflexao_total:
            x_refr = length * np.sin(np.radians(theta2_deg))
            y_refr = -length * np.cos(np.radians(theta2_deg))
            fig.add_trace(go.Scatter(x=[0, x_refr], y=[0, y_refr], mode='lines',
                                     line=dict(color='green', width=max(1, 4 * T)), 
                                     name=r'Refração'))
        else:
            fig.add_annotation(x=0, y=-5, text="REFLEXÃO TOTAL INTERNA", showarrow=False, 
                               font=dict(size=16, color="red"))

        fig.update_layout(
            height=600,
            showlegend=True,
            xaxis=dict(range=[-11, 11], showgrid=False, zeroline=False, visible=False),
            yaxis=dict(range=[-11, 11], showgrid=False, zeroline=False, visible=False),
            margin=dict(l=0, r=0, t=20, b=0),
            paper_bgcolor='rgba(0,0,0,0)', # Fundo transparente
            plot_bgcolor='rgba(0,0,0,0)'   # Fundo transparente
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_info:
        st.subheader("Resultados")
        
        if reflexao_total:
            st.error(r"Ocorre Reflexão Total ($\theta_1 > \theta_{cr}$)")
        
        # Uso de st.metric padrão
        st.metric(label=r"Ângulo de Refração ($\theta_2$)", 
                  value=f"{theta2_deg:.2f}°" if not reflexao_total else "N/A")
        
        st.metric(label=r"Ângulo Crítico ($\theta_{cr}$)", 
                  value=f"{ang_critico:.2f}°" if ang_critico else "N/A")
        
        st.divider()
        st.write("**Distribuição de Energia:**")
        st.metric("Transmissão (T)", f"{T*100:.1f} %")
        st.metric("Reflexão (R)", f"{R*100:.1f} %")
        st.progress(T)

with tab2:
    st.header("Referencial Teórico")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Lei de Snell-Descartes")
        st.latex(r"\frac{\sin \theta_1}{v_1} = \frac{\sin \theta_2}{v_2}")
        st.markdown(r"""
        Define a mudança de direção do feixe sônico ao passar de um meio com velocidade $v_1$ 
        para um meio com velocidade $v_2$.
        """)
    with c2:
        st.subheader("Impedância e Reflexão")
        st.latex(r"Z = \rho \cdot v")
        st.latex(r"R = \left( \frac{Z_2 - Z_1}{Z_2 + Z_1} \right)^2")
        st.markdown(r"A eficiência da transmissão depende do casamento de impedâncias ($Z$).")