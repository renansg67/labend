import streamlit as st

def atenuacao_de_ondas_acusticas():
    col1, col2, col3 = st.columns([.25, 3, 1.5])


    col2.title("Atenuação de ondas acústicas em sólidos")

    col2.expander(":material/book: Sumário", expanded=True).markdown('''
        - [Atenuação de ondas acústicas em sólidos](#atenuacao-de-ondas-acusticas-em-solidos)
            - [Início](#inicio)
            - [Mecanismos de atenuação](#mecanismos-de-atenuacao)
            - [Fatores que afetam o coeficiente](#fatores-que-afetam-o-coeficiente)
            - [Atenuação em materiais isotrópicos](#atenuacao-em-materiais-isotropicos)
            - [Materiais com fontes dispersoras](#materiais-com-fontes-dispersoras)
            - [Impacto das fontes dispersoras](#impacto-das-fontes-dispersoras)
            - [Atenuação em materiais pouco rígidos](#atenuacao-em-materiais-pouco-rigidos)
            - [Atenuação na madeira](#atenuacao-na-madeira)
    ''')

    col2.header("Início")

    # REVISÃO: Parágrafo longo dividido para melhor leitura.
    col2.write("""
        São vários os mecanismos de atenuação de ondas acústicas em sólidos. Neste capítulo será vista inicialmente uma abordagem mais generalizada para vários tipos de materiais e os mecanismos envolvidos nesse processo.
    """)

    col2.write("""
        A atenuação é a redução progressiva da intensidade (energia) da onda à medida que ela se propaga através do material. O fenômeno ocorre devido à dispersão (scattering) e à absorção de energia pelo meio. Os processos de atenuação variam consideravelmente entre materiais isotrópicos e anisotrópicos, sendo necessário um conhecimento aprofundado do material para interpretar corretamente os resultados dos ensaios não destrutivos.
    """)

    col2.markdown("#### Mecanismos de atenuação")

    col2.write("A atenuação é o fenômeno físico no qual a intensidade da onda é reduzida em função da distância percorrida no material. Isso ocorre devido à conversão da energia da onda acústica em outras formas de energia, como calor. A energia da onda acústica é atenuada de acordo com a seguinte expressão:")

    col2.markdown(r"""
        $$
            I=I_{0}e^{-2\alpha x}
        $$
    """)

    col2.write("Onde:")
    col2.markdown("""
        * $I$: Intensidade do sinal em uma distância $x$.
        * $I_{0}$: Intensidade inicial do sinal.
        * $e$: Base dos logaritmos naturais.
        * $\\alpha$: **Coeficiente de atenuação** (em $\\text{Np}/\\text{cm}$ ou $\\text{dB}/\\text{cm}$).
        * $x$: Distância percorrida.
    """)

    col2.write("Ao reorganizar a equação e aplicar o logaritmo natural, obtém-se o coeficiente de atenuação:")

    col2.markdown(r"""
        $$
            \alpha=\dfrac{1}{2x}\ln\left(\dfrac{I_{0}}{I}\right)
        $$
    """)

    col2.markdown("#### Fatores que afetam o coeficiente de atenuação")

    col2.markdown("""
        * **Frequência do transdutor:** Quanto maior a frequência, maior a atenuação.
        * **Distância percorrida:** A atenuação aumenta com a distância.
        * **Tipo de material:** Materiais com alta rigidez e densidade tendem a atenuar menos.
        * **Microestrutura:** A presença e o tamanho de grãos, poros, ou fibras (em materiais anisotrópicos) aumentam a dispersão.
        * **Temperatura e umidade:** Alteram a rigidez e, consequentemente, a atenuação.
        * **Defeitos e descontinuidades:** Fissuras, vazios ou inclusões geram reflexões e dispersão.
    """)

    col2.markdown("#### Atenuação em materiais isotrópicos")

    col2.write("""
        Em materiais isotrópicos, os mecanismos de atenuação mais importantes são a **dispersão** (*scattering*) e a **absorção**.
        
        * **Dispersão:** É a energia que é desviada do caminho original devido a interfaces (fronteiras de grãos, poros, agregados, etc.).
        * **Absorção:** É a conversão da energia acústica em calor, principalmente devido à viscosidade interna e à condução térmica.
    """)

    col2.write("A atenuação em materiais isotrópicos tem sido estudada de forma mais aprofundada, com modelos bem estabelecidos que consideram a microestrutura do material. No entanto, em materiais anisotrópicos (como a madeira), o fenômeno é mais complexo, sendo necessário um conhecimento prévio da estrutura interna e das direções de simetria elástica para uma análise precisa.")

    col2.subheader("Materiais com fontes dispersoras")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.write("""
        A dispersão (*scattering*) é o principal mecanismo de atenuação em materiais não homogêneos, como aços e ligas metálicas, que contêm grãos cristalinos. Esses grãos atuam como fontes dispersoras, desviando a trajetória da onda.
        
        A dispersão está diretamente relacionada à razão entre o comprimento de onda ($\\lambda$) e o tamanho médio do grão ($d_{\\text{grão}}$).
        
        Existem dois regimes principais de dispersão que se distinguem por essa razão  :
    """)

    col3.info("O coeficiente de atenuação por dispersão pode ser expresso como $\\alpha_{\\text{dispersão}}=A\\cdot f^{m}$, onde $A$ é uma constante e o expoente $m$ (que varia de 1 a 4) depende do regime de dispersão.")

    col2.markdown("##### Regime de Dispersão Rayleigh ($\\lambda \\gg d_{\\text{grão}}$)")
    col2.write("""
        Ocorre quando o comprimento de onda é **muito maior** que o tamanho do grão ($\\lambda/d_{\\text{grão}} > 10$).
        * **Atenuação:** O coeficiente de atenuação é proporcional à **quarta potência da frequência** ($f^{4}$), tornando a atenuação muito sensível a pequenas variações de frequência. É o regime dominante em materiais com grãos muito pequenos ou ao utilizar transdutores de baixa frequência.
    """)

    col2.markdown("##### Regime de Dispersão Estocástica (Stochastic) ($\\lambda\\approx d_{\\text{grão}}$)")
    col2.write("""
        Ocorre quando o comprimento de onda é **comparável** ao tamanho do grão.
        * **Atenuação:** O coeficiente de atenuação é aproximadamente proporcional ao **quadrado da frequência** ($f^{2}$), sendo intermediário entre Rayleigh e a região de fronteira (difusa), onde a atenuação se torna menos dependente da frequência ($f^{1}$).
    """)

    col2.subheader("Impacto das fontes dispersoras")

    col2.write("A maior dispersão do feixe ultrassônico faz com que parte da energia retorne na direção da fonte, dificultando a análise e, em casos extremos, impedindo a penetração completa da onda no material. Para contornar esse problema, a alternativa é a redução da frequência do transdutor, diminuindo o coeficiente de atenuação por dispersão, conforme a expressão $\\alpha_{\\text{dispersão}} \\propto f^{m}$.")

    col2.write("Em materiais com porosidade elevada (como o concreto), o mecanismo de dispersão também é relevante, sendo as partículas de agregados e os vazios as principais fontes dispersoras. A presença de fontes dispersoras de tamanhos variados resulta em um comportamento de atenuação complexo, exigindo um estudo aprofundado da microestrutura para a seleção da frequência ideal do transdutor.")

    col2.subheader("Atenuação em materiais com grãos colunares")

    col2.write("Em materiais com grãos que apresentam um formato alongado ou colunar, a atenuação é mais complexa, sendo influenciada pela direção de propagação do feixe em relação à orientação dos grãos. A atenuação é geralmente maior quando a direção de propagação é perpendicular ao eixo do grão. Essa variação direcional é um exemplo de anisotropia de atenuação, em que o coeficiente $\\alpha$ não é uma constante, mas um tensor que depende da orientação do ensaio.")

    col2.subheader("Atenuação em materiais pouco rígidos")

    col2.write("Em materiais com baixa rigidez, os mecanismos de absorção (conversão de energia em calor) tornam-se mais importantes que os de dispersão. A absorção é predominantemente causada por:")
    
    col2.markdown("""
        * **Viscosidade interna:** O atrito interno durante a movimentação das partículas converte energia mecânica em calor. A atenuação por este mecanismo é geralmente proporcional ao quadrado da frequência ($f^{2}$).
        * **Condução térmica:** A passagem da onda acústica provoca compressão e rarefação, gerando variações de temperatura local. A transferência de calor entre as regiões quentes e frias absorve energia da onda.
    """)
    
    col2.write("Em materiais poliméricos ou borrachas, onde a viscosidade é alta, a atenuação é dominada pela absorção. Nessas condições, a velocidade de propagação também é menor, reforçando a relação de que materiais pouco rígidos (baixo módulo de elasticidade) tendem a apresentar maior atenuação.")

    col2.subheader("Atenuação na madeira")

    # REVISÃO: Texto detalhado sobre a madeira estruturado em lista e parágrafos curtos.
    col2.write("A madeira é um material altamente anisotrópico e sua atenuação é complexa devido à sua estrutura fibrosa e heterogênea, que inclui anéis de crescimento e parênquimas. A atenuação varia drasticamente com a direção de propagação em relação aos seus eixos principais (Longitudinal, Radial e Tangencial).")
    
    col2.markdown("Os estudos demonstram que, em geral, o coeficiente de atenuação é:")
    
    col2.markdown("""
        * **Mínimo** na **direção Longitudinal (L)**, que é a direção paralela às fibras. A onda tem um caminho preferencial, com menor dispersão.
        * **Máximo** nas **direções Radial (R) e Tangencial (T)**, que são perpendiculares às fibras. A presença de parênquimas radiais e a orientação dos anéis de crescimento causam maior dispersão da energia.
    """)
    
    col2.write("Pesquisas usando ondas de compressão e cisalhamento (transversais) confirmam essa dependência direcional. Por exemplo, na direção Longitudinal, a atenuação é menor. Quando o ensaio é feito no plano Tangencial-Radial (TR), ou seja, perpendicular às fibras, os parênquimas radiais e as fibras são ortogonais à direção de propagação no plano LR, concordando com os maiores coeficientes de atenuação obtidos.")

    col2.write("Outros fatores também relacionados à atenuação, que foram mencionados na seção anterior, dizem respeito à temperatura e à umidade da amostra. Nota-se que a rigidez do material é inversamente proporcional a ambas as grandezas, dessa forma, nota-se redução na velocidade de propagação do pulso ultrassônico ao aumentá-las.")

    col2.write("Outra análise relevante foi feita, associada à propagação de ondas acústicas de cisalhamento em amostras com diferentes larguras dos anéis de crescimento. Nota-se que na direção radial, quando se aumenta a largura dos anéis, há baixa correlação entre esse aumento e a alteração da velocidade de propagação, com ela tendendo a permanecer constante. Entretanto, na direção tangencial, ao aumentar a largura dos anéis, as ondas de cisalhamento apresentaram aumento de velocidade de propagação.")

    col2.info("""
    **Referências**

    * **BUCUR, Voichita**. Acoustics of Wood. 3. ed. Berlin; Heidelberg: Springer, 2025. ISBN 978-3-662-70208-6
              
    * **AMERICAN SOCIETY FOR NONDESTRUCTIVE TESTING.** ASNT Level III Study Guide: Ultrasonic Testing Method (UT). 2. ed. Columbus, OH: ASNT, 2013.
    """)

if __name__ == "__main__":
    atenuacao_de_ondas_acusticas()