import pandas as pd
import numpy as np

def calcular_curvas_atenuacao(frequencia_max_mhz=10, pontos=50):
    """
    Calcula o coeficiente de atenuação (alpha) para diferentes materiais 
    em função da frequência, usando a relação alpha = a * f^b.

    Args:
        frequencia_max_mhz (int): Frequência máxima para o cálculo (em MHz).
        pontos (int): Número de pontos na curva de frequência.

    Returns:
        pandas.DataFrame: DataFrame contendo Frequência, Atenuação (dB/cm) e Material.
    """
    
    # 1. Definição do Eixo X (Frequência)
    frequencia_mhz = np.linspace(1, frequencia_max_mhz, pontos) 

    # 2. Dados Teóricos de Atenuação (Coeficientes a e b)
    # a: dB/cm/MHz^b | b: Dependência da Frequência
    data_materiais = {
        'Tecido Mole (b=1.0)': {'a': 0.5, 'b': 1.0},
        'Gordura (b=1.0)': {'a': 0.4, 'b': 1.0},
        'Madeira (b=2.5)': {'a': 0.4, 'b': 2.5}, # NOVO: Atenuação alta e dependência elevada
        'Água Pura (b=2.0)': {'a': 0.0002, 'b': 2.0},
        'Aço Forjado (b=2.0)': {'a': 0.02, 'b': 2.0},
        'Concreto/Heterogêneo (b=4.0)': {'a': 0.08, 'b': 4.0}
    }

    df = pd.DataFrame()

    # 3. Cálculo das Curvas
    for material, params in data_materiais.items():
        a = params['a']
        b = params['b']
        
        # Cálculo: alpha (dB/cm) = a * (frequencia ^ b)
        alpha_db_cm = a * (frequencia_mhz ** b)
        
        temp_df = pd.DataFrame({
            'Frequência (MHz)': frequencia_mhz,
            'Atenuação (dB/cm)': alpha_db_cm,
            'Material': material,
            'Dependência (b)': b,
            'Coeficiente (a)': a
        })
        
        df = pd.concat([df, temp_df], ignore_index=True)
        
    return df
