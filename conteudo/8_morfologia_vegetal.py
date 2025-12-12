import streamlit as st

col1, col2, col3 = st.columns([.25, 3, 1.5])

col2.title("Morfologia Vegetal")

col2.header("Início")

# REVISÃO: Parágrafo longo dividido.
col2.write("""
A anatomia da madeira estuda a estrutura interna do lenho, revelando como os diferentes tipos celulares se organizam para permitir condução, suporte e armazenamento. Esse campo é fundamental para compreender tanto a diversidade entre espécies quanto o comportamento tecnológico da madeira, já que muitos de seus atributos — como resistência, durabilidade, densidade e trabalhabilidade — derivam diretamente da organização anatômica do xilema secundário.
""")

col2.write("""
O capítulo inicia contextualizando a formação do lenho a partir do câmbio vascular, explicando como o crescimento em espessura gera tecidos novos e como fatores ambientais influenciam a distinção entre lenho inicial e tardio. A seguir, introduz-se a diferença essencial entre angiospermas e gimnospermas: enquanto estas se estruturam quase exclusivamente com traqueídes, aquelas apresentam um conjunto mais complexo de vasos, fibras e parênquima, produzindo grande variedade de padrões estruturais.
""")

col2.write("""
A anatomia macroscópica é apresentada como ponto de partida para a identificação visual, abordando aspectos como anéis de crescimento, porosidade, disposição dos raios e presença de canais. Na sequência, o capítulo aprofunda-se na organização microscópica, descrevendo a forma e a função dos principais tipos celulares, bem como suas variações diagnósticas — como perfurações, agrupamentos, tipos de parênquima  e características dos raios. 
""")

col2.write("""
Por fim, discute-se como tais estruturas influenciam o desempenho da madeira em aplicações práticas. A relação entre anatomia e propriedades físicas e mecânicas, o comportamento na secagem e usinagem, a permeabilidade ao tratamento preservativo e os fatores que afetam a durabilidade natural são examinados como exemplos de como a estrutura celular determina o uso mais adequado de cada espécie. O capítulo se encerra destacando a importância da anatomia da madeira na identificação de espécies, na avaliação da qualidade do material e no entendimento de variações naturais que impactam a produção e o processamento.
""")

col2.header("Anatomia da Madeira")

col1, col2, col3 = st.columns([.25, 3, 1.5])

# REVISÃO: O parágrafo sobre a anatomia foi quebrado e organizado em blocos temáticos para maior clareza.
col2.markdown("#### Estrutura do Xilema e Floema")
col2.write("""
Tanto o alburno como o cerne fazem parte do xilema secundário. O caule aumenta muito mais de diâmetro na periferia. O raio parenquimático tende a sofrer dilatação na região do floema, devido ao maior crescimento da periferia. Ele está presente tanto no xilema quanto no floema.
""")

col2.write("""
O floema secundário é formado por células condutoras como os elementos de tubo crivado e suas células companheiras, raio parenquimático e tecidos de sustentação, podendo ser fibras ou esclereides.
""")

col2.markdown("#### Câmbio e Produção de Tecidos")
col2.write("""
Da mesma forma do que no floema, no câmbio temos as iniciais fusiformes e as radiais. As radiais produzem raio parenquimático para dentro e para fora em relação ao câmbio. Já as fusiformes produzem os elementos de tubo crivado e suas células companheiras e os elementos axiais como fibras e esclereides.
""")

col2.markdown("#### Diferenças entre Coníferas (Gimnospermas) e Outras Espécies")
col2.write("""
Em coníferas, o xilema normalmente é composto somente por traqueides  e células de raio, raramente parênquima axial. No floema, há presença de células crivadas em sucessão. Devido ao rompimento que ocorre nas camadas de maior diâmetro na epiderme, o felogênio é responsável por produzir súber para fora e feloderme para dentro.
""")

col3.image("imagens/tronco-partes.png", width=220)

col2.table(data=[
    {"Atributo": "Folhas", "Gimnospermas": "Aciculifoliadas", "Angiospermas": "Latifoliadas"},
    {"Atributo": "Elementos de vaso", "Gimnospermas": "Não", "Angiospermas": "Sim"},
    {"Atributo": "Fruto", "Gimnospermas": "Não", "Angiospermas": "Sim"},
    {"Atributo": "Exemplos", "Gimnospermas": "Araucária, pinus", "Angiospermas": "Quase todas as nativas"},
    {"Atributo": "Flores", "Gimnospermas": "Não", "Angiospermas": "Sim"},
    {"Atributo": "Casca ao redor das sementes", "Gimnospermas": "Não", "Angiospermas": "Sim"},
    {"Atributo": "Sementes ao redor de um eixo", "Gimnospermas": "Sim", "Angiospermas": "Não"},
])

col2.info("""
    **Referências**
             
    * **CECCANTINI, Gregório.** Morfologia Vegetal - Aula 17 - Anatomia da Madeira. YouTube, 2017. Disponível em: [https://www.youtube.com/watch?v=0pVfOpylmcE](https://www.youtube.com/watch?v=0pVfOpylmcE). Acesso em: 10/12/2025.     

    * **LABORATÓRIO DE PRODUTOS FLORESTAIS.** Vídeoaula - Identificação Anatômica de Madeira. YouTube, 2013. Disponível em: [https://www.youtube.com/watch?v=94QP-zc05kg](https://www.youtube.com/watch?v=94QP-zc05kg). Acesso em: 10/12/2025.
""")