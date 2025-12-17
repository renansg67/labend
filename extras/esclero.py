import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import io

# --- 1. FUNÇÃO DO GRÁFICO (RESTAURADA E COLORIDA) ---
def gerar_plot_colorido(n_lin, n_col, lista_status):
    fig = go.Figure()
    espacamento = 30  # mm
    raio_circulo = 10
    
    largura_total = (n_col - 1) * espacamento
    altura_total = (n_lin - 1) * espacamento

    for r in range(n_lin):
        for c in range(n_col):
            idx = r * n_col + c
            x_pos = c * espacamento
            y_pos = (n_lin - 1 - r) * espacamento # P1 no topo esquerdo
            
            status_atual = lista_status[idx]
            # Lógica de cores baseada no descarte
            if "Mantido" in status_atual:
                cor_fill, cor_line = "rgba(46, 204, 113, 0.8)", "darkgreen"
            else:
                cor_fill, cor_line = "rgba(231, 76, 60, 0.8)", "darkred"

            # Quadrado de 30mm
            fig.add_shape(type="rect", x0=x_pos-15, y0=y_pos-15, x1=x_pos+15, y1=y_pos+15,
                          line=dict(color="rgba(0,0,0,0.1)"), fillcolor="rgba(0,0,0,0.05)")
            
            # Círculo circunscrito
            fig.add_shape(type="circle", x0=x_pos-raio_circulo, y0=y_pos-raio_circulo, 
                          x1=x_pos+raio_circulo, y1=y_pos+raio_circulo,
                          line=dict(color=cor_line, width=2), fillcolor=cor_fill)
            
            fig.add_annotation(x=x_pos, y=y_pos, text=f"P{idx+1}", showarrow=False,
                               font=dict(size=11, color="white" if "Descartado" in status_atual else "black"))

    fig.update_layout(
        xaxis=dict(range=[-25, largura_total+25], showgrid=False, title="Largura (mm)"),
        yaxis=dict(range=[-25, altura_total+25], showgrid=False, title="Altura (mm)", scaleanchor="x", scaleratio=1),
        width=500, height=500, plot_bgcolor='rgba(225, 255, 255, .5)', margin=dict(l=10, r=10, t=40, b=10)
    )
    return fig

# --- 2. INTERFACE E LÓGICA ---
def exibir_esclerometria_completa():
    st.header("🔨 Esclerometria NBR 7584:2012 — Relatório Completo")

    # CALIBRAÇÃO
    with st.expander("1. Calibração (Fator k)", expanded=False):
        c1, c2 = st.columns([2, 1])
        cal_in = c1.text_input("Valores na bigorna:", value="80 81 80 79 82 80 80 81 79 80")
        ie_nom = c2.number_input(r"$I_{E_{\text{nom}}}$", value=80.0)
        v_cal = [float(x) for x in cal_in.replace(',', '.').split() if x.strip()]
        k = (len(v_cal) * ie_nom) / sum(v_cal) if len(v_cal) >= 10 else 1.0
        st.latex(rf"k = {k:.3f}")

    # CONFIGURAÇÃO MALHA
    st.subheader("2. Malha de Ensaio")
    cl1, cl2 = st.columns(2)
    n_lin = cl1.number_input("Linhas", 1, 10, 4)
    n_col = cl2.number_input("Colunas", 1, 10, 4)
    
    # INPUT DE DADOS
    st.markdown("### 📥 Entrada de Índices")
    impactos = []
    for i in range(n_lin):
        cols = st.columns(n_col)
        for j in range(n_col):
            idx = i * n_col + j
            val = cols[j].number_input(f"P{idx+1}", value=30.0, step=1.0, key=f"inp_{idx}", label_visibility="collapsed")
            impactos.append(val)

    # --- 3. PROCESSAMENTO (NBR 7584) ---
    media_bruta = np.mean(impactos)
    l_inf1, l_sup1 = media_bruta * 0.9, media_bruta * 1.1
    
    status_pontos = []
    restantes_p1 = []
    for x in impactos:
        if l_inf1 <= x <= l_sup1:
            status_pontos.append("Mantido (Etapa 1)")
            restantes_p1.append(x)
        else:
            status_pontos.append("Descartado (Etapa 1)")

    area_valida = True
    ie_medio_final = 0.0
    ie_medio_temp, l_inf2, l_sup2 = 0.0, 0.0, 0.0
    msg_erro = ""

    if len(restantes_p1) < 5:
        area_valida = False
        msg_erro = "Rejeitado: < 5 pontos restantes."
    else:
        ie_medio_temp = np.mean(restantes_p1)
        l_inf2, l_sup2 = ie_medio_temp * 0.9, ie_medio_temp * 1.1
        for i, val in enumerate(impactos):
            if "Mantido" in status_pontos[i]:
                if not (l_inf2 <= val <= l_sup2):
                    status_pontos[i] = "Descartado (Etapa 2)"
                    area_valida = False
                    msg_erro = "Rejeitado: Inconsistência na Etapa 2."
        if area_valida: ie_medio_final = ie_medio_temp

    # --- 4. EXIBIÇÃO ---
    st.divider()
    tab_vis, tab_audit = st.tabs(["📊 Mapa e Resultados", "🔍 Auditoria Detalhada"])

    with tab_vis:
        c_p, c_m = st.columns([1.2, 1])
        with c_p:
            st.plotly_chart(gerar_plot_colorido(n_lin, n_col, status_pontos))
        with c_m:
            st.metric("Índice Efetivo ($I_{E_{\\alpha}}$)", f"{k*ie_medio_final:.2f}" if area_valida else "INVÁLIDO")
            st.metric("Média Bruta", f"{media_bruta:.2f}")
            if area_valida: st.success("Área Aprovada")
            else: st.error(msg_erro)

    with tab_audit:
        st.markdown(f"**Intervalo 1 (±10% Bruta):** `[{l_inf1:.2f} — {l_sup1:.2f}]`")
        if len(restantes_p1) >= 5:
            st.markdown(f"**Intervalo 2 (±10% Nova):** `[{l_inf2:.2f} — {l_sup2:.2f}]`")
        
        df_audit = pd.DataFrame({"Ponto": [f"P{i+1}" for i in range(len(impactos))], "Valor": impactos, "Análise": status_pontos})
        st.dataframe(df_audit, width="stretch")

    # --- 5. EXPORTAÇÃO CSV (RESTAURADO COM DETALHES) ---
    output = io.StringIO()
    output.write("RELATORIO DE ENSAIO DE ESCLEROMETRIA - NBR 7584\n")
    output.write(f"Status Final:;{'APROVADO' if area_valida else 'REJEITADO'}\n")
    output.write(f"Fator k:;{k:.3f}\n")
    output.write(f"Ie Efetivo final:;{k*ie_medio_final if area_valida else 'N/A'}\n")
    output.write("\n--- PARAMETROS DE CALCULO ---\n")
    output.write(f"Etapa 1 (Media {media_bruta:.2f});Intervalo;[{l_inf1:.2f} a {l_sup1:.2f}]\n")
    output.write(f"Etapa 2 (Media {ie_medio_temp:.2f});Intervalo;[{l_inf2:.2f} a {l_sup2:.2f}]\n")
    output.write("\n--- DETALHAMENTO POR PONTO ---\n")
    df_audit.to_csv(output, index=False, sep=';')
    
    st.download_button("📥 Baixar CSV com Memória de Cálculo", output.getvalue(), "relatorio_esclerometria.csv", "text/csv")

exibir_esclerometria_completa()