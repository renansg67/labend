import numpy as np

def calcular_altura_hipsometro(L: float, alpha_deg: float, beta_deg: float, cenario: str) -> float:
    """
    Calcula a altura total usando apenas magnitudes positivas de ângulos.
    """
    if L <= 0: return 0.0
    
    # Garantir que trabalhamos com valores positivos (magnitude)
    a = np.radians(abs(alpha_deg))
    b = np.radians(abs(beta_deg))
    
    if cenario == "Terreno Plano / Olho no Meio":
        # Soma das componentes acima e abaixo do horizonte
        return L * (np.tan(a) + np.tan(b))
    
    elif cenario == "Observador Abaixo da Base (Aclive)":
        # Diferença entre a altura do topo e a altura da base (ambos acima)
        return L * abs(np.tan(a) - np.tan(b))
    
    else: # Observador Acima do Topo (Declive)
        # Diferença entre a profundidade da base e a profundidade do topo (ambos abaixo)
        return L * abs(np.tan(b) - np.tan(a))