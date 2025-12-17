import streamlit as st

st.set_page_config(layout="wide")

pages = {
    "Início": [
        st.Page("./inicio/apresentacao.py", title="Página Inicial", icon=":material/flight_land:")
    ],
    "Principal": [
        st.Page("./conteudo/1_materiais_nao_metalicos.py", title="Materiais de Construção não Metálicos", icon=":material/polymer:"),
        st.Page("./conteudo/2_classificacao_madeira_estrutural.py", title="Classificação de Madeira Estrutural", icon=":material/carpenter:"),
        st.Page("./conteudo/3_inspecao_de_estruturas_de_concreto_e_madeira.py", title="Inspeção de Estruturas (Concreto e Madeira)", icon=":material/cabin:"),
        st.Page("./conteudo/4_inspecao_de_arvores.py", title="Inspeção de Árvores", icon=":material/forest:"),
        st.Page("./conteudo/5_matriz_de_rigidez.py", title="Matriz de Rigidez", icon=":material/background_grid_small:"),
        st.Page("./conteudo/6_propagacao_de_ondas_acusticas.py", title="Propagação de Ondas Acústicas", icon=":material/waves:"),
        st.Page("./conteudo/7_atenuacao_de_ondas_acusticas.py", title="Atenuação de Ondas Acústicas", icon=":material/cadence:"),
        st.Page("./conteudo/8_morfologia_vegetal.py", title="Morfologia Vegetal", icon=":material/nature:"),
    ],
    "Extras": [
        st.Page("./extras/extra_atenuacao.py", title="Atenuação", icon=":material/flare:"),
        st.Page("./extras/snell_calculator.py", title="Snell", icon=":material/south_east:"),
        st.Page("./extras/n.py", title="Ondas", icon=":material/ssid_chart:"),
        st.Page("./extras/hipsometria.py", title="Hipsometria", icon=":material/forest:"),
        st.Page("./extras/potencial.py", title="Potencial de Corrosão", icon=":material/electric_bolt:"),
        st.Page("./extras/esclero.py", title="Esclerometria", icon=":material/square:")
    ],
    "Auxiliar": [
        st.Page("./aux_files/links_auxiliares.py", title="Links", icon=":material/insert_link:")
    ],
}

pg = st.navigation(pages, position="top")
pg.run()