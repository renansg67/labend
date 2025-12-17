import streamlit as st

def apresentacao_page():

    # Colunas principais
    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.markdown("# 🧱 LME | LabEND - Laboratório de Materiais e Estruturas | Ensaios Não Destrutivos")

    col2.image("https://github.com/renansg67/vetores/blob/master/png/landing-page.png?raw=true")

    # Bloco de texto de Boas-Vindas (Revisado para usar funções Streamlit)
    col2.subheader("Bem-vindo(a)! 👋")
    col2.write("""
        Esta plataforma apresenta conteúdos sobre diferentes **ensaios não destrutivos (END)** aplicados a **materiais de construção não metálicos**, como **concreto**, **madeira** e até mesmo **árvores** utilizadas em áreas urbanas.
    """)

    col2.subheader("🔍 O que você vai encontrar aqui")
    col2.markdown("""
        - Explicações didáticas sobre os **principais métodos de ensaio não destrutivo**, como esclerometria, ultrassom, termografia e tomografia.
        - **Imagens e esquemas ilustrativos** que mostram como cada técnica é aplicada na prática.
        - **Comparações entre materiais**, destacando como o comportamento varia entre concreto, madeira e outros materiais naturais.
        - Seções específicas dedicadas a **ensaios em estruturas, peças e árvores**, com foco em aplicações reais e exemplos de campo.
    """)

    col2.subheader("🎯 Nosso objetivo")
    col2.write("""
        Promover a **compreensão e a valorização dos ensaios não destrutivos** como ferramentas fundamentais para avaliar a qualidade, a segurança e o desempenho dos materiais — sem causar danos às estruturas.
        A plataforma serve como um **espaço de aprendizado e consulta**, voltado a estudantes, pesquisadores e interessados em tecnologia e conservação de materiais de construção.
    """)

    col3.info("🧩 **Dica:** Explore o menu superior para navegar entre as seções para aprender diversos tipos de ensaios e descobrir exemplos, imagens e explicações detalhadas sobre cada técnica e contexto.")

if __name__ == "__main__":
    apresentacao_page()