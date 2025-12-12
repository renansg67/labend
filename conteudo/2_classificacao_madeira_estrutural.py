import streamlit as st

def classificacao_madeira_estrutural_page():
    col1, col2, col3 = st.columns([.25, 3, 1.5])

    # REVISÃO: Título ligeiramente mais conciso
    col2.title("Ensaios Não Destrutivos Normatizados para Classificação de Madeira Estrutural")

    # REVISÃO: Sumário limpo e sem o título repetido
    col2.expander(":material/book: Sumário", expanded=True).markdown('''
        - [Início](#inicio)
        - [Sobre os Ensaios e a ABNT NBR 7190:2022](#sobre-os-ensaios-e-a-abnt-nbr-7190-2022)
            - [Classificação Visual](#classificacao-visual)
            - [Classificação Mecânica](#classificacao-mecanica)
            - [Densidade Aparente](#densidade-aparente)
    ''')
                                
    col2.header("Início")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    # REVISÃO: Texto de Introdução com mais fluidez
    col2.write("""
        Neste capítulo, serão apresentados os principais ensaios não destrutivos normatizados para a classificação da madeira estrutural, com foco nos fundamentos estabelecidos pela **ABNT NBR 7190:2022**.
        
        Esta norma passou por uma significativa reformulação e série de atualizações em 2022, após mais de 20 anos sem alterações (a versão anterior era de 1997). As mudanças visam aprimorar diversos contextos de utilização da madeira, resultando na separação da norma em 7 partes distintas:
    """)

    col3.video("https://www.youtube.com/watch?v=X5dpNCvzTcI")

    col3.info("""
        - ABNT NBR 7190-2: Métodos de ensaio para classificação visual e mecânica de peças estruturais de madeira
        - ABNT NBR 7190-3: Métodos de ensaio para corpos de prova isentos de defeitos para madeiras de florestas nativas
        - ABNT NBR 7190-4: Métodos de ensaio para caracterização de peças estruturais
        - ABNT NBR 7190-5: Métodos de ensaio para determinação da resistência e da rigidez de ligações com conectores mecânicos
        - ABNT NBR 7190-6: Métodos de ensaio para caracterização de madeira lamelada colada estrutural
        - ABNT NBR 7190-7: Métodos de ensaio para caracterização de madeira lamelada colada cruzada estrutural
    """)

    col2.image("imagens/graphviz.png")

    col2.header("Sobre os Ensaios e a ABNT NBR 7190:2022")

    # REVISÃO: Maior clareza sobre os critérios de classificação
    col2.write("""
        Os métodos aqui tratados complementam os ensaios de caracterização apresentados na seção anterior.
        
        A **ABNT NBR 7190-2:2022** estabelece o procedimento para a classificação de lotes de madeira provenientes de **florestas plantadas não homogêneas** com base em:
        
        * **Parâmetros visuais**
        * **Parâmetros mecânicos**

        A classe de resistência das peças estruturais deve ser determinada utilizando os dois parâmetros, sendo a classificação final estabelecida com base no **pior resultado obtido entre a classificação visual e a mecânica**.
    """)

    col2.subheader("Classificação Visual")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    # REVISÃO: Texto direto sobre a Classificação Visual
    col2.write("""
        A classificação visual é baseada na identificação e na avaliação da severidade de defeitos presentes na peça. O tamanho e a natureza desses defeitos determinam a classe de resistência a ser atribuída.
        
        A peça pode ser descartada para uso estrutural caso os defeitos ultrapassem os limites estabelecidos pela norma.
        
        **Os parâmetros visuais de avaliação incluem¹:**
    """)

    # REVISÃO: Formatação da lista de defeitos no info box para melhor visualização
    col3.info("""
        **¹Defeitos Visuais para Avaliação:**
        * Fissuras (passantes ou não passantes)
        * Inclinação excessiva das fibras
        * Dano mecânico
        * Presença de nós
        * Ataque biológico
        * Presença de medula
        * Bolsas de resina
        * Distorções dimensionais (Arqueamento, torcimento, esmoado, encanoamento e encurvamento)
    """)

    col2.subheader("Classificação Mecânica")

    # REVISÃO: Texto dividido em tópicos para melhor leitura
    col2.markdown("""
        A classificação mecânica exige a determinação de dois parâmetros-chave: **a densidade aparente** e o **módulo de elasticidade na flexão estática**.
        
        #### Ensaio de Flexão Estática - Critérios Operacionais
        
        O ensaio deve seguir rigorosos critérios dimensionais e de carregamento para evitar o rompimento da peça (mantendo-o semidestrutivo).
        
        **Critérios Dimensionais e de Posicionamento:**
        * A peça deve ser ensaiada na **posição deitada**, com a maior dimensão da seção transversal ($h$) na horizontal.
        * O vão livre deve ser de **18 vezes a largura ($b$)** da peça ensaiada.
        * O comprimento apoiado deve ser igual à **largura ($b$)** da peça.
        
        **Critério de Carregamento:**
        * A carga aplicada deve ser limitada a **$10\\%$ a $40\\%$ da força máxima de ruptura** da peça.
        
        **Alternativas Não Destrutivas:**
        Como alternativa aos métodos destrutivos amplamente empregados, o módulo de elasticidade também pode ser obtido por **métodos vibracionais** (detalhados na seção anterior), os quais apresentam boa correlação com o ensaio de flexão estática.
    """)

    col2.subheader("Densidade Aparente")

    # REVISÃO: Texto simplificado e com foco na correção de umidade
    col2.markdown("""
        A densidade aparente ($\\rho_{12}$) é determinada na **condição-padrão de 12% de umidade** (Umidade de Equilíbrio), conforme estipulado pela norma.
        
        Para peças ensaiadas com umidade diferente da padrão (no intervalo de $10\\%$ a $25\\%$), deve ser aplicada uma correção da densidade medida ($\\rho_{\\text{test}}$) para a densidade aparente padrão através da seguinte relação:
    """)

    col2.markdown(r"""
        $$
            \rho_{12}=\rho_{\text{test}}(1-0.5(U-0.12))
        $$
    """)

    col2.write("""
        É importante notar que essa necessidade de correção também se aplica ao módulo de elasticidade obtido no ensaio de flexão estática, que deve ser ajustado conforme as relações de umidade apresentadas na seção anterior.
    """)

    col2.info("""
        **Referências Bibliográficas**
             
        * **ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS**. NBR 7190:2022 — Projeto de estruturas de madeira. Rio de Janeiro: ABNT, 2022.      
    """)

if __name__ == "__main__":
    classificacao_madeira_estrutural_page()