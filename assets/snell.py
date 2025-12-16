import numpy as np
import plotly.graph_objects as go
from typing import Tuple, Optional

# --- Constantes para o Plot ---
MAX_COORD = 5
ARROW_OFFSET = 0.6

# -------------------------------------------------------------
# 1. FUNÇÕES DE CÁLCULO
# -------------------------------------------------------------

def calcular_impedancia(rho: float, V: float) -> float:
    """Calcula a impedancia acustica Z = rho * V."""
    if rho <= 0 or V <= 0:
        return 0.0
    return rho * V

def calcular_coeficientes_transmissao_reflexao(Z1: float, Z2: float) -> Tuple[float, float]:
    """Calcula os coeficientes de Reflexao (R) e Transmissao (T) para incidencia normal."""
    if (Z1 + Z2) == 0:
        return 0.0, 0.0
        
    R = ((Z2 - Z1) / (Z2 + Z1)) ** 2
    T = 1.0 - R
    
    return R, T

def calcular_energia_transmitida(E_incidente: float, T: float) -> float:
    """Calcula a energia transmitida (E_trans) a partir da energia incidente e do Coeficiente de Transmissao (T)."""
    return E_incidente * T

def calcular_angulo_critico(v1: float, v2: float) -> Optional[float]:
    """
    Calcula o angulo critico em graus. O angulo critico so existe se V1 < V2 (o meio refratado e mais rapido).
    Retorna o angulo em graus ou None.
    """
    if v1 <= 0 or v2 <= 0:
        return None
        
    # Angulo critico existe quando V1 < V2 e alpha_cr = arcsin(V1 / V2)
    ratio = v1 / v2
    if ratio < 1:
         return np.rad2deg(np.arcsin(ratio))
    else:
        # Não existe ângulo crítico para a condição V1 >= V2
        return None

def calcular_refracao(v1: float, v2: float, theta1_graus: float, angulo_critico_graus: Optional[float]) -> Tuple[Optional[float], str]:
    """
    Calcula o angulo de refracao (θ₂) usando a Lei de Snell.
    Requer o angulo critico pre-calculado para verificar Reflexao Total Interna (RTI).
    Retorna (theta2_rad, mensagem).
    """
    if v1 <= 0 or v2 <= 0:
        return None, "Erro: As velocidades devem ser positivas."
        
    theta1_rad = np.deg2rad(theta1_graus)
    
    snell_term = (v2 / v1) * np.sin(theta1_rad)
    
    if abs(snell_term) >= 1: # Usar >= para capturar o limite do angulo critico
        
        # Condicao de Reflexao Total Interna (RTI)
        if angulo_critico_graus is not None and theta1_graus >= angulo_critico_graus:
             resultado = f"Reflexao Total: Angulo de incidencia ({theta1_graus:.2f}°) >= Angulo critico ({angulo_critico_graus:.2f}°)."
             return None, resultado
        
        # Outros casos de sin(theta2) >= 1 (erros numericos ou θ1=90 em V1 >= V2)
        elif angulo_critico_graus is None and theta1_graus == 90.0:
            return np.deg2rad(90.0), "Angulo Limite: θ₁ = 90° e θ₂ = 90°."
        else:
            return None, "Erro de Calculo: O termo de Snell é >= 1 em uma condição onde RTI não deveria ocorrer."

    else:
        # Refracao Normal
        theta2_rad = np.arcsin(snell_term)
        theta2_graus = np.rad2deg(theta2_rad)
        
        resultado = f"Ângulo de Refração (θ₂): {theta2_graus:.2f}°"
        return theta2_rad, resultado


# -------------------------------------------------------------
# 2. FUNÇÕES DE VISUALIZAÇÃO
# -------------------------------------------------------------

def criar_figura_refracao(theta1_graus: float, theta2_rad: Optional[float], resultado_msg: str, angulo_critico_graus: Optional[float]) -> go.Figure:
    """
    Cria um diagrama de refracao Plotly (2º -> 4º quadrante), incluindo o angulo critico.
    (Mantenha inalterada)
    """
    fig = go.Figure()
    annotations = []
    
    # 1. Interface e Normal
    fig.add_trace(go.Scatter(x=[-MAX_COORD, MAX_COORD], y=[0, 0], 
                             mode='lines', name='Interface', 
                             line=dict(color='darkgray', width=2)))
    
    fig.add_trace(go.Scatter(x=[0, 0], y=[-MAX_COORD, MAX_COORD], 
                             mode='lines', name='Normal', 
                             line=dict(color='black', dash='dot')))

    # 2. Raio Incidente (Meio 1, 2º Quadrante)
    theta1_rad = np.deg2rad(theta1_graus)
    x_inc = -MAX_COORD * np.sin(theta1_rad)
    y_inc = MAX_COORD * np.cos(theta1_rad)
    
    fig.add_trace(go.Scatter(x=[0, x_inc], y=[0, y_inc], 
                             mode='lines', name=f'Incidência (θ₁={theta1_graus:.2f}°)',
                             line=dict(color='blue', width=3)))

    # 3. Adiciona Seta (Vetor) do Raio Incidente
    x_arrow1 = -ARROW_OFFSET * np.sin(theta1_rad)
    y_arrow1 = ARROW_OFFSET * np.cos(theta1_rad)
    
    annotations.append(dict(
        x=x_arrow1, y=y_arrow1, 
        ax=x_arrow1 * 0.99, ay=y_arrow1 * 0.99, 
        xref='x', yref='y', axref='x', ayref='y',
        showarrow=True, arrowhead=7, arrowsize=1.5, arrowwidth=2, arrowcolor='blue'
    ))

    # 4. Raio Refratado (Meio 2, 4º Quadrante) ou Reflexao Total
    if theta2_rad is not None:
        # Raio Refratado
        x_refr = MAX_COORD * np.sin(theta2_rad)
        y_refr = -MAX_COORD * np.cos(theta2_rad)
        
        fig.add_trace(go.Scatter(x=[0, x_refr], y=[0, y_refr], 
                                 mode='lines', name=f'Refração (θ₂={np.rad2deg(theta2_rad):.2f}°)',
                                 line=dict(color='red', width=3)))
        
        # Adiciona Seta (Vetor) do Raio Refratado
        x_arrow2 = ARROW_OFFSET * np.sin(theta2_rad)
        y_arrow2 = -ARROW_OFFSET * np.cos(theta2_rad)
        
        annotations.append(dict(
            x=x_arrow2, y=y_arrow2, 
            ax=x_arrow2 * 0.99, ay=y_arrow2 * 0.99, 
            xref='x', yref='y', axref='x', ayref='y',
            showarrow=True, arrowhead=7, arrowsize=1.5, arrowwidth=2, arrowcolor='red'
        ))
        
    else:
        # Reflexao Total (Raio refletido no Meio 1, 1º Quadrante)
        x_refle = MAX_COORD * np.sin(theta1_rad) 
        y_refle = MAX_COORD * np.cos(theta1_rad)
        
        fig.add_trace(go.Scatter(x=[0, x_refle], y=[0, y_refle], 
                                 mode='lines', name='Reflexão (Total)',
                                 line=dict(color='orange', width=3, dash='dash')))

        # Adiciona Seta (Vetor) do Raio Refletido
        x_arrow_refle = ARROW_OFFSET * np.sin(theta1_rad)
        y_arrow_refle = ARROW_OFFSET * np.cos(theta1_rad)
        
        annotations.append(dict(
            x=x_arrow_refle, y=y_arrow_refle, 
            ax=x_arrow_refle * 0.99, ay=y_arrow_refle * 0.99, 
            xref='x', yref='y', axref='x', ayref='y',
            showarrow=True, arrowhead=7, arrowsize=1.5, arrowwidth=2, arrowcolor='orange'
        ))

    # 5. Desenha o Ângulo Crítico, se existir (no 1º e 2º quadrantes)
    if angulo_critico_graus is not None:
        alpha_cr_rad = np.deg2rad(angulo_critico_graus)
        
        # Raio de Incidencia Critica (2º Quadrante)
        x_cr_inc = -MAX_COORD * np.sin(alpha_cr_rad)
        y_cr_inc = MAX_COORD * np.cos(alpha_cr_rad)

        # Raio de Reflexao Total (1º Quadrante, limite)
        x_cr_refle = MAX_COORD * np.sin(alpha_cr_rad) 
        y_cr_refle = MAX_COORD * np.cos(alpha_cr_rad)

        fig.add_trace(go.Scatter(x=[x_cr_inc, 0, x_cr_refle], y=[y_cr_inc, 0, y_cr_refle], 
                                 mode='lines', name=f'Ângulo Crítico (Inc/Refletido)',
                                 line=dict(color='gray', width=1, dash='dot')))


    # 6. Configuracoes Finais
    fig.update_layout(
        title=f'Simulação da Refração Acústica<br><sup>{resultado_msg}</sup>',
        xaxis=dict(range=[-MAX_COORD * 1.2, MAX_COORD * 1.2], constrain='domain'),
        yaxis=dict(range=[-MAX_COORD * 1.2, MAX_COORD * 1.2], scaleanchor="x", scaleratio=1),
        showlegend=True,
        annotations=annotations 
    )
    
    return fig