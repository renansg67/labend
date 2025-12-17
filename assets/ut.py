import numpy as np

def calcular_comprimento_onda(V: float, f: float) -> float:
    return V / f if V > 0 and f > 0 else 0.0

def calcular_campo_proximo(D: float, f: float, V: float) -> float:
    """Nf = D² * f / (4 * V)"""
    if V <= 0: return 0.0
    return (D**2 * f) / (4 * V)

def calcular_divergencia_feixe(V: float, f: float, D: float) -> float:
    """sin(theta) = 1.22 * L / D"""
    if V <= 0 or f <= 0 or D <= 0: return 0.0
    lw = V / f
    arg = 1.22 * (lw / D)
    return np.rad2deg(np.arcsin(arg)) if arg <= 1 else 90.0

def calcular_ressonancia_amostra(V_material: float, L_amostra: float, n: int = 1) -> float:
    """f = n * (V / (2 * L))"""
    if L_amostra <= 0: return 0.0
    return n * (V_material / (2 * L_amostra))

def gerar_envelope_feixe(z: np.ndarray, D_mm: float, Nf_mm: float, theta_deg: float) -> np.ndarray:
    """Calcula o raio do feixe ao longo da profundidade z."""
    r0 = D_mm / 2
    return np.where(z <= Nf_mm, 
                    r0, 
                    r0 + (z - Nf_mm) * np.tan(np.deg2rad(theta_deg)))