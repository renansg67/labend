import streamlit as st

def apresentacao_page():
    
    # Colunas de imagens ilustrativas (Anatomia da Madeira)
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    col1.image(
        "https://upload.wikimedia.org/wikipedia/commons/6/6e/Woody_Dicot_Stem_Cross_Section_Quercus_Wood_40x_%2834991087693%29.jpg",
        caption="Seção Transversal de Madeira Dicotiledônea (Angiosperma)"
    )
    col2.image(
        "https://upload.wikimedia.org/wikipedia/commons/4/4c/Gymnosperm_Stem_Soft_Wood_in_Pinus_%2836087417260%29.jpg",
        caption="Seção Transversal de Madeira de Conífera (Gimnosperma - Pinus)"
    )
    col3.image(
        "https://upload.wikimedia.org/wikipedia/commons/a/aa/Gymnosperm_Stem_Circular_Bordered_Pits_in_Pinus_Wood_%2836484401545%29.jpg",
        caption="Pontoações Areoladas Circulares em Pinus (Detalhe)"
    )
    col4.image(
        "https://upload.wikimedia.org/wikipedia/commons/a/ac/Gymnosperm_Stem_Soft_Wood_in_Pinus_%2836087426450%29.jpg",
        caption="Madeira Macia de Pinus (Visão Tangencial)"
    )
    
    # Colunas principais
    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.markdown("# 🧱 LabEND | Portal de Ensaios Não Destrutivos")

    # Imagem de capa
    col3.image("imagens/intro-cap-1.jpg") 

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

    col2.info("🧩 **Dica:** Explore o menu lateral para navegar entre os diferentes tipos de ensaios e descobrir exemplos, imagens e explicações detalhadas sobre cada técnica.")
    
    # Colunas de imagens de aplicação (fundo)
    col1, col2, col3, col4, col5 = st.columns([.25, 1, 1, 1, 1.5])

    col2.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Abstract_pattern_on_a_tree_stump.jpg/330px-Abstract_pattern_on_a_tree_stump.jpg",
        caption="Ultrassom para inspeção de árvores",
        width="stretch"
    )
    col3.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Betonkorrosion_unter_Autobahnbruecke_%2802%29.JPG/330px-Betonkorrosion_unter_Autobahnbruecke_%2802%29.JPG",
        caption="Ensaio de profundidade de carbonatação como ensaio complementar a outros ENDs",
        width="stretch"
    )
    col4.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Stacked_Timber_Displaying_Growth_Rings.jpg/330px-Stacked_Timber_Displaying_Growth_Rings.jpg",
        caption="Ensaio de flexão estática conforme ABNT NBR 7190",
        width="stretch"
    )

if __name__ == "__main__":
    apresentacao_page()