import streamlit as st
import numpy as np
# Importa as funcoes do arquivo snell_calculator.py
from assets.snell import (
    calcular_refracao, 
    criar_figura_refracao,
    calcular_impedancia,
    calcular_coeficientes_transmissao_reflexao,
    calcular_energia_transmitida,
    calcular_angulo_critico
)

# 1. Configuração e Título
st.set_page_config(layout="wide", page_title="Refracao Acustica e Transmissao - Lei de Snell")

st.title("Simulação da Refração e Transmissão de Ondas Acústicas")
st.markdown("Calcula o ângulo de refração (Lei de Snell) e a transmissão de energia (baseado na Impedância Acústica) ao passar da interface entre dois meios.")

# Define as colunas principais (Entrada e Visualização/Resultados)
col_input, col_display = st.columns([.5, 2], gap="large")

# --- A. Configuracoes de Entrada (Coluna Esquerda) ---
with col_input:
    # Agrupamento visual dos inputs com um container
    with st.container(border=True): 
        st.markdown("#### Parâmetros de Entrada")
        
        # Meio 1 (Incidente)
        st.markdown("##### Meio 1 (Incidência)")
        v1 = st.number_input("Velocidade do Som, $V_1$ (m/s)", 
                             value=1500.0, min_value=1.0, step=10.0, format="%.1f")
        rho1 = st.number_input("Massa Específica, $\\rho_1$ (kg/m³)", 
                               value=1000.0, min_value=1.0, step=10.0, format="%.1f")
        E_incidente = st.number_input("Energia Incidente, $E_{\\text{inc}}$ (unidades)",
                                       value=100.0, min_value=0.0, step=1.0, format="%.1f")
        
        # Meio 2 (Refratado)
        st.markdown("##### Meio 2 (Refração)")
        v2 = st.number_input("Velocidade do Som, $V_2$ (m/s)", 
                             value=343.0, min_value=1.0, step=10.0, format="%.1f")
        rho2 = st.number_input("Massa Específica, $\\rho_2$ (kg/m³)", 
                               value=1.2, min_value=0.1, step=0.1, format="%.2f")
        
        # Angulo de Incidencia
        st.markdown("##### Ângulo de Entrada")
        theta1_graus = st.slider("Ângulo de Incidência ($\\theta_1$ em graus)", 
                                 min_value=0.0, max_value=90.0, value=30.0, step=0.1, format="%.1f")

# --- B. Processamento e Resultados (Coluna Direita) ---
with col_display:
    st.markdown("#### Resultados da Simulação")
    
    # Processamento de todos os cálculos
    Z1 = calcular_impedancia(rho1, v1)
    Z2 = calcular_impedancia(rho2, v2)
    R, T = calcular_coeficientes_transmissao_reflexao(Z1, Z2)
    E_trans = calcular_energia_transmitida(E_incidente, T)
    E_refle = E_incidente * R
    angulo_critico_graus = calcular_angulo_critico(v1, v2)
    theta2_rad, resultado_msg = calcular_refracao(v1, v2, theta1_graus, angulo_critico_graus)
    
    
    # --- B1. Impedância e Coeficientes de Transmissão ---
    col_Z, col_coef = st.columns(2)

    col_Z.markdown("##### Transmissão e Reflexão (Incidência Normal)")
    col_Z.markdown("Cálculos baseados na Impedância Acústica ($\\mathbf{Z = \\rho V}$), assumindo incidência **normal** ($\\mathbf{\\theta_1 = 0^\\circ}$).")
    
    with col_Z:
        st.metric(label="Impedância Acústica Meio 1 ($Z_1$)", value=f"{Z1:,.2f} kg/(m²⋅s)")
        st.metric(label="Impedância Acústica Meio 2 ($Z_2$)", value=f"{Z2:,.2f} kg/(m²⋅s)")
        st.metric(label="Coeficiente de Reflexão ($R$)", value=f"{R:.4f} ({R*100:.2f} %)")
        st.metric(label="Coeficiente de Transmissão ($T$)", value=f"{T:.4f} ({T*100:.2f} %)")
        st.metric(label="Energia Transmitida ($E_{\\text{trans}}$)", value=f"{E_trans:.2f} unidades")


    with col_coef:
        st.markdown("**Resultado da Refração:**")
        st.info(resultado_msg)
        
        if angulo_critico_graus is not None:
            st.markdown(f"**Ângulo Crítico ($\\alpha_{{cr}}$)**: {angulo_critico_graus:.2f}°")
            st.markdown("Reflexão Total Interna ocorre quando $\\theta_{1} \\ge \\alpha_{cr}$.")
        else:
            st.markdown("**Ângulo Crítico:** Não existe (o meio 2 é mais lento que o meio 1, $V_1 \\ge V_2$).")
    
        # Visualização (gráfico)
        fig = criar_figura_refracao(theta1_graus, theta2_rad, resultado_msg, angulo_critico_graus)
        st.plotly_chart(fig, use_container_width=True)
        


# --- C. Fórmulas de Referência ---
st.markdown("---")
# Usando um expander para reduzir o espaço ocupado por fórmulas de referência
with st.expander("Fórmulas Teóricas de Referência", expanded=False): 
    st.markdown("##### Impedância Acústica e Coeficientes (Incidência Normal)")
    st.latex(r'''
        Z=\rho V \quad \text{(Impedância Acústica)}
    ''')
    st.latex(r'''
        R=\left(\dfrac{Z_{2}-Z_{1}}{Z_{2}+Z_{1}}\right)^{\!\!2} \quad \text{(Coeficiente de Reflexão)}
    ''')
    st.latex(r'''
        T=1-R \quad \text{e} \quad E_{\text{trans}}=E_{\text{inc}} \cdot T \quad \text{(Coeficiente e Energia Transmitida)}
    ''')

    st.markdown("##### Lei de Snell (Refração) e Ângulo Crítico")
    if angulo_critico_graus is not None:
        st.latex(r'''
            \alpha_{\text{cr}}=\arcsin\left(\dfrac{V_{1}}{V_{2}}\right) \quad \text{Se } V_2 > V_1
        ''')
    st.latex(r'''
        \dfrac{\sin\alpha_{1}}{\sin\alpha_{2}}=\dfrac{V_{1}}{V_{2}} \implies \theta_2 = \arcsin \left( \frac{V_2}{V_1} \sin(\theta_1) \right)
    ''')