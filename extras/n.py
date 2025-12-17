import streamlit as st
import numpy as np
import plotly.graph_objects as go
import assets.ut as ut 

st.set_page_config(layout="wide", page_title="Simulador NDT Profissional")

# --- CONSTANTES ---
MEGA, MILLI = 1_000_000, 0.001

st.title("🔬 Caracterização de Feixe e Onda Acústica")

# --- SIDEBAR (Parâmetros) ---
with st.sidebar:
    st.header("⚙️ Parâmetros de Entrada")
    
    st.subheader("Material")
    v_mat = st.number_input("Velocidade (m/s)", value=5900.0, step=100.0)
    L_mm = st.number_input("Espessura L (mm)", value=120.0, min_value=1.0)
    alpha_db_mm = st.slider("Atenuação (dB/mm)", 0.0, 0.2, 0.04, format="%.3f")
    
    st.divider()
    st.subheader("Transdutor")
    D_mm = st.number_input("Diâmetro Cristal D (mm)", value=19.0, min_value=1.0)
    f_MHz = st.number_input("Frequência (MHz)", value=2.25, min_value=0.1)

# --- CÁLCULOS TÉCNICOS ---
f_hz = f_MHz * MEGA
lambda_mm = ut.calcular_comprimento_onda(v_mat, f_hz) * 1000
zona_fresnel = ut.calcular_campo_proximo(D_mm * MILLI, f_hz, v_mat) * 1000
theta_div = ut.calcular_divergencia_feixe(v_mat, f_hz, D_mm * MILLI)
n_ondas = L_mm / lambda_mm

# --- MÉTRICAS NO TOPO ---
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Campo Próximo (N)", f"{zona_fresnel:.1f} mm")
m2.metric("Divergência (θ)", f"{theta_div:.2f}°")
m3.metric("Nº de Ondas", f"{n_ondas:.2f}")
m4.metric("Comprimento λ", f"{lambda_mm:.3f} mm")
m5.metric("Intensidade Final", f"{( (10**(-(alpha_db_mm * L_mm) / 20)) * (zona_fresnel/L_mm if L_mm > zona_fresnel else 1) )**2 * 100:.1f} %")

st.divider()

# --- MODELAGEM DO GRÁFICO ---
z_plot = np.linspace(0, L_mm, 1200)

# 1. Geometria e Decaimento
r_facho = np.where(
    z_plot <= zona_fresnel,
    D_mm / 2,
    D_mm / 2 + (z_plot - zona_fresnel) * np.tan(np.radians(theta_div))
)

amp_mat = 10**(-(alpha_db_mm * z_plot) / 20)
amp_geo = np.ones_like(z_plot)
if zona_fresnel > 0:
    mask = z_plot > zona_fresnel
    amp_geo[mask] = zona_fresnel / z_plot[mask]

amp_total = amp_mat * amp_geo
onda = (D_mm/2 * amp_total) * np.sin((2 * np.pi / lambda_mm) * z_plot)

# --- CONSTRUÇÃO VISUAL (PLOTLY) ---
fig = go.Figure()

# A. Facho com Gradiente de Intensidade (Fatias de transparência)
num_fatias = 60
z_fatias = np.array_split(z_plot, num_fatias)
r_fatias = np.array_split(r_facho, num_fatias)
amp_fatias = np.array_split(amp_total, num_fatias)

for i in range(num_fatias):
    # Opacidade baseada na amplitude média da fatia
    opacidade = np.mean(amp_fatias[i]) * 0.3
    z_slice = np.concatenate([z_fatias[i], z_fatias[i][::-1]])
    r_slice = np.concatenate([r_fatias[i], -r_fatias[i][::-1]])
    
    fig.add_trace(go.Scatter(
        x=z_slice, y=r_slice, fill='toself',
        fillcolor=f'rgba(65, 105, 225, {opacidade:.3f})',
        line=dict(width=0), showlegend=False, hoverinfo='skip'
    ))

# B. Bordas Geométricas (Facho conico)
fig.add_trace(go.Scatter(x=z_plot, y=r_facho, line=dict(color='rgba(100,100,100,0.3)', dash='dash'), name="Borda do Feixe"))
fig.add_trace(go.Scatter(x=z_plot, y=-r_facho, line=dict(color='rgba(100,100,100,0.3)', dash='dash'), showlegend=False))

# C. Onda Acústica (Sólida)
fig.add_trace(go.Scatter(x=z_plot, y=onda, line=dict(color='royalblue', width=2), name='Onda (Pressão)'))

# D. Marcadores de Ciclo (Triângulos)
picos_x = np.arange(lambda_mm/4, L_mm, lambda_mm)
picos_y = (D_mm/2 * (10**(-(alpha_db_mm * picos_x) / 20)) * np.where(picos_x > zona_fresnel, zona_fresnel/picos_x, 1))

fig.add_trace(go.Scatter(
    x=picos_x, y=picos_y + 0.3, mode='markers',
    marker=dict(symbol='triangle-down', color='red', size=7),
    name='Picos de Ciclo'
))

# E. Linha de Transição N
fig.add_vline(x=zona_fresnel, line_dash="dot", line_color="orange", 
              annotation_text=f"N={zona_fresnel:.1f}mm", annotation_position="bottom right")

fig.update_layout(
    height=550,
    xaxis_title="Profundidade no Material (mm)",
    yaxis_title="Amplitude / Expansão (mm)",
    template="plotly_white",
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

st.plotly_chart(fig, use_container_width=True)