import numpy as np

def interpretar_potencial(U_mv: float) -> str:
    if U_mv > -200:
        return "5% (Baixa probabilidade)"
    elif -350 <= U_mv <= -200:
        return "Inconclusivo (Zona Duvidosa)"
    else:
        return "95% (Alta probabilidade)"

def preparar_matriz(grid_data: list) -> np.ndarray:
    return np.array(grid_data)[::-1]