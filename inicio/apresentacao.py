import streamlit as st

def apresentacao_page(): 
    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.markdown("# 🧱 LabEND | Portal de Ensaios Não Destrutivos")


    #col2.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Guernica_reproduction_on_tiled_wall%2C_Guernica%2C_Spain_%28PPL3-Altered%29_julesvernex2.jpg/960px-Guernica_reproduction_on_tiled_wall%2C_Guernica%2C_Spain_%28PPL3-Altered%29_julesvernex2.jpg")

    col2.markdown("""
        #### Bem-vindo(a)! 👋  
        Esta plataforma apresenta conteúdos sobre diferentes **ensaios não destrutivos (END)** aplicados a **materiais de construção não metálicos**, como **concreto**, **madeira** e até mesmo **árvores** utilizadas em áreas urbanas.

        ---

        ### 🔍 O que você vai encontrar aqui

        - Explicações didáticas sobre os **principais métodos de ensaio não destrutivo**, como esclerometria, ultrassom, termografia e tomografia.  
        - **Imagens e esquemas ilustrativos** que mostram como cada técnica é aplicada na prática.  
        - **Comparações entre materiais**, destacando como o comportamento varia entre concreto, madeira e outros materiais naturais.  
        - Seções específicas dedicadas a **ensaios em estruturas, peças e árvores**, com foco em aplicações reais e exemplos de campo.  

        ---

        ### 🎯 Nosso objetivo

        Promover a **compreensão e a valorização dos ensaios não destrutivos** como ferramentas fundamentais para avaliar a qualidade, a segurança e o desempenho dos materiais — sem causar danos às estruturas.  
        A plataforma serve como um **espaço de aprendizado e consulta**, voltado a estudantes, pesquisadores e interessados em tecnologia e conservação de materiais de construção.

        ---

        🧩 **Dica:** Explore o menu superior para navegar entre os diferentes tipos de ensaios e descobrir exemplos, imagens e explicações detalhadas sobre cada técnica.
    """)
    
    with col3.expander("Ultrassom para inspeção de árvores", expanded=True):
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Abstract_pattern_on_a_tree_stump.jpg/330px-Abstract_pattern_on_a_tree_stump.jpg")
        if st.button("Saiba mais :material/search:", key="us"):
            st.switch_page("./conteudo/4_inspecao_de_arvores.py")

    with col3.expander("Carbonatação como ensaio complementar a outros ENDs", expanded=True):
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Betonkorrosion_unter_Autobahnbruecke_%2802%29.JPG/330px-Betonkorrosion_unter_Autobahnbruecke_%2802%29.JPG")
        if st.button("Saiba mais :material/search:", key="carbonatacao"):
            st.switch_page("./conteudo/3_inspecao_de_estruturas_de_concreto_e_madeira.py")

    #with col3.expander("Termografia para inspeção de fachadas", expanded=True):
    #    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Infrared_thermal_imaging_during_a_yacht_survey.jpg/500px-Infrared_thermal_imaging_during_a_yacht_survey.jpg")
    #    if st.button("Saiba mais :material/search:", key="termografia"):
    #        st.switch_page("./conteudos/3_inspecao_de_estruturas_de_concreto_e_madeira.py")

    col1, col2, col3, col4 = st.columns([.25, 1.5, 1.5, 1.5])
    with col2.expander("Ensaio de flexão estática conforme ABNT NBR 7190", expanded=True):
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Stacked_Timber_Displaying_Growth_Rings.jpg/330px-Stacked_Timber_Displaying_Growth_Rings.jpg")
        if st.button("Saiba mais :material/search:", key="flexao_estatica"):
            #st.switch_page("./conteudo/2_classificacao_madeira_estrutural.py")
            st.switch_page("./conteudo/2_classificacao_madeira_estrutural.py")

    with col3.expander("Livros e materiais para consulta", expanded=True):
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Christen_Dalsgaard_-_In_a_pine_wood._Study_-_Google_Art_Project.jpg/250px-Christen_Dalsgaard_-_In_a_pine_wood._Study_-_Google_Art_Project.jpg")
        if st.button("Saiba mais :material/search:", key="intro"):
            st.switch_page("./biblioteca/introducao.py")
            

if __name__ == "__main__":
    apresentacao_page()