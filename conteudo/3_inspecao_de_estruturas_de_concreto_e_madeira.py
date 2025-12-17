import streamlit as st

def inspecao_concreto():
    col1, col2, col3 = st.columns([.25, 3, 1.5])

    # REVISÃO: Título mais conciso
    col2.title("Ensaios Não Destrutivos na Inspeção de Estruturas de Madeira e Concreto")

    col2.expander(":material/book: Sumário", expanded=True).markdown('''
        - [Início](#inicio)
        - [Madeira](#madeira)
            - [Cronometragem do Tempo de Viagem da Onda de Tensão](#cronometragem-do-tempo-de-viagem-da-onda-de-tensao)
            - [Penetrografia](#penetrografia)
            - [*Pilodyn*](#pilodyn)
            - [Tomografia Acústica](#tomografia-acustica)
            - [Tomografia Elétrica](#tomografia-eletrica)
            - [Termografia](#termografia)
            - [Radar de Penetração de Solo (GPR)](#radar-de-penetracao-de-solo-gpr)
        - [Concreto](#concreto)
            - [Método Eletromagnético (Pacometria)](#metodo-eletromagnetico-pacometria)
                - [Usos da Pacometria em outros Ensaios](#usos-da-pacometria-em-outros-ensaios)
            - [Ensaio de Penetração de Pinos](#ensaio-de-penetracao-de-pinos)
            - [Ensaio de Raios X e $\\gamma$](#ensaio-de-raios-x-e-g-gammag)
            - [Inspeção por Imagens](#ensaio-de-inspecao-de-imagens)
            - [Profundidade de Carbonatação](#ensaio-de-profundidade-de-carbonatacao)
            - [Resistividade Elétrica](#ensaio-de-resistividade-eletrica)
            - [Potencial de Corrosão](#ensaio-de-potencial-de-corrosao)
            - [Radar de Penetração de Solo (GPR)](#radar-de-penetracao-de-solo-gpr)
            - [Termografia](#termografia)
    ''')

    col2.header("Início")

    # REVISÃO: Texto de introdução dividido para melhor digestão
    col2.write("""
        Os ensaios não destrutivos (ENDs) se consolidaram como alternativas confiáveis aos ensaios destrutivos para o diagnóstico de estruturas, oferecendo agilidade e segurança na avaliação estrutural. Estruturas de **concreto** são amplamente utilizadas no Brasil, enquanto a **madeira** é mais comum em outros países, como os Estados Unidos.
        
        Ambos os materiais estão sujeitos a desgaste e perda de resistência devido a fatores ambientais ou patologias decorrentes de falhas de projeto/processo. A inspeção, sem causar danos ou comprometimento, exige a aplicação de métodos não destrutivos e semi-destrutivos.
    """)

    col2.write("""
        **Pontos-Chave da Inspeção:**
        
        * **Madeira:** Muitos métodos aplicados em árvores vivas (setor florestal) são estendidos para a madeira pós-abatimento (toras ou peças estruturais), exigindo validação científica para cada contexto de aplicação.
        * **Concreto:** A inspeção do concreto armado requer atenção fundamental à presença da **armadura**. O conhecimento sobre o efeito do aço é crucial para a correta avaliação da qualidade do concreto inspecionado.
    """)
    # REVISÃO: Removida a longa lista de ensaios na introdução; eles estão no sumário.

    col2.header("Madeira")

    col2.subheader("Cronometragem do Tempo de Viagem da Onda de Tensão")

    # REVISÃO: Texto mais estruturado com foco nos dois principais usos
    col2.write("""
        Este ensaio é baseado na medição do tempo de viagem de ondas de tensão que atravessam a seção transversal da madeira para avaliar sua qualidade .
        
        O método utiliza dois acelerômetros posicionados em lados opostos do tronco. Um impacto induzido gera um sinal, e o tempo de propagação entre o emissor e o receptor é registrado. Conhecendo-se a distância, calcula-se a **velocidade de propagação** ao longo do tronco.
        
        #### Avaliação da Condição do Fuste
        
        Estudos estabelecem velocidades típicas para diferentes espécies. Velocidades mais baixas que o padrão podem indicar **deterioração interna** ou cavidades.
        
        * **Limitações:** A vasta gama de espécies e fatores ambientais podem gerar incertezas (falsos positivos/negativos).
        * **Recomendação:** Recomenda-se o uso de métodos complementares, como penetrógrafos e *Pilodyn*, para aumentar a confiabilidade e evitar o abate desnecessário.
        * **Custo/Tempo:** Este método é rápido (cerca de 2 minutos), sendo mais escalável que a Tomografia Acústica (cerca de 30 minutos).
    """)

    col2.write("""
        #### Determinação da Orientação das Fibras
        
        Além da inspeção do fuste, a cronometragem longitudinal pode determinar o ângulo das fibras em relação à vertical.
        
        * **Princípio:** Os acelerômetros são posicionados em diferentes angulações em relação à vertical.
        * **Resultado:** A rota que registra o **menor tempo de propagação** é a que indica a direção paralela às fibras, pois o feixe ultrassônico segue este caminho preferencial. Este método tem mostrado boa correlação com medições pós-abatimento.
    """)

    col2.subheader("Penetrografia")

    # REVISÃO: Uso de lista para as premissas
    col2.write("""
        A penetrografia utiliza **micro brocas** de pequeno diâmetro que penetram no interior da madeira, fornecendo parâmetros de resistência à penetração e resistência ao giro.
        
        * **Natureza Invasiva:** É considerado um ensaio invasivo por criar um orifício, mas não gera danos estruturais em árvores vivas, que são capazes de cicatrizar o local.
        
        O ensaio é baseado em duas premissas fundamentais de demanda de potência:
        
        1. **Resistência à Penetração:** Concentra-se na dificuldade da ponta da broca em perfurar o material (relacionada à **densidade**). O atrito lateral é desconsiderado.
        2. **Resistência à Rotação (Giro):** Concentra-se no atrito lateral, que pode ser usado para avaliar a presença de material na porção lateral da broca.
        
        As **curvas de amplitude** obtidas (gráficos de resistência) permitem ao operador diferenciar regiões de **madeira sã** daquelas com rachaduras internas, deterioração, cavidades ou galerias.
    """)

    col2.subheader("*Pilodyn*")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col3.image("https://www.researchgate.net/profile/Pieters-M-2/publication/277127938/figure/fig6/AS:669537175367692@1536641510502/The-Pilodyn-wood-tester-De-Pilodyn-houttester.ppm")

    col2.write("""
        O *Pilodyn* é um equipamento manual, constituído por uma agulha que é disparada na superfície.
        
        Sua finalidade é determinar a qualidade da madeira nas **camadas mais próximas à casca** ao avaliar a resistência à penetração da agulha.
        
        * **Princípio:** Quanto maior a penetração da agulha, **menor a densidade** da madeira superficial e vice-versa.
        * **Uso:** É um método de medida direta que pode ser utilizado em conjunto com técnicas indiretas para refinar a inspeção.
    """)

    col2.subheader("Tomografia Acústica")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.markdown("""
        A Tomografia Acústica utiliza um equipamento **multissensor** com acelerômetros distribuídos de forma equidistante e na mesma altura ao redor do tronco¹.
        
        O objetivo é avaliar a qualidade interna do fuste, diferenciando:
        
        * Regiões de **madeira sã**
        * Regiões com **biodeterioração**
        * **Cavidades**
        
        O ensaio se baseia na propagação de **ondas ultrassônicas**  (geradas por um martelo sônico) no interior do tronco. Múltiplos sensores captam o sinal, e as **velocidades de propagação** são medidas nas diferentes rotas entre os sensores. Todos os acelerômetros devem ser impactados para maximizar a coleta de dados.
        
        **Interpretação dos Resultados:**
        
        Os modelos interpoladores geram **gráficos bidimensionais** (tomogramas) da seção transversal do tronco:
        
        * **Velocidades Lentas:** Podem indicar cavidades ou deterioração (baixa rigidez).
        * **Velocidades Altas:** Representam uma condição de madeira sã, com rigidez e resistência adequadas.
    """)

    col3.info("¹As alturas normalmente utilizadas são: Diâmetro à altura do peito (DAP) e diâmetro à altura do solo (DAS). Os mesmos são obtidos a partir da medida da circunferência do tronco. Ao assumir que o tronco é circular, a aproximação das medidas de diâmetro é feita pela equação $D=C/\\pi$ ou $r=C/(2\\pi)$")

    col2.subheader("Tomografia Elétrica")

    # REVISÃO: Uso de lista para a interpretação e foco na limitação da umidade
    col2.write("""
        Semelhante à Tomografia Acústica, este método utiliza múltiplos sensores (eletrodos). No entanto, em vez de ondas ultrassônicas, propaga-se **corrente elétrica** no interior do tronco . A resistividade elétrica é medida entre os diferentes pontos.
        
        * **Valores Baixos de Resistividade:** Tendem a indicar locais com presença de **deterioração** e cavidades.
        * **Valores Altos de Resistividade:** São indicativos de **madeira sã** e de rigidez e resistência adequadas.
        
        #### Limitação da Umidade
        
        Esta técnica é altamente dependente da umidade do tronco.
        
        * Regiões mais úmidas apresentam **menor resistividade**.
        * Regiões secas apresentam **maior resistividade**.
        
        A interpretação requer cautela: uma cavidade seca pode apresentar alta resistividade, o que pode levar a um diagnóstico incorreto de madeira sã. É crucial diferenciar regiões secas devido a cavidades de regiões de madeira sã.
    """)

    col2.subheader("Termografia")

    col2.write("""
        A Termografia utiliza câmeras infravermelhas para detectar falhas com base nas **diferenças de temperatura** na superfície do material .
        
        Danos (fissuras, vazios ou cavidades) alteram as propriedades de condutividade térmica do material. Regiões sãs e com defeitos aquecem e esfriam em tempos distintos, criando gradientes de temperatura que são registrados pela câmera.
        
        * **Fator Limitante:** A inspeção requer uma **janela de aquecimento ou resfriamento** (diferença de temperatura induzida, natural ou artificial) para que o equipamento possa registrar as diferenças térmicas de forma eficaz.
    """)

    col2.subheader("Radar de Penetração de Solo (GPR)")

    col2.write("""
        O Radar de Penetração de Solo (Ground Penetrating Radar - GPR) baseia-se na emissão e recepção de ondas eletromagnéticas (frequências de rádio) através de antenas .
        
        #### Uso Principal (Madeira)
        
        Seu uso mais tradicional é no setor florestal para **mapear o posicionamento das raízes** no solo, com base na diferença de umidade e outras propriedades eletromagnéticas entre as raízes e o solo.
        
        #### Uso Secundário (Madeira)
        
        Estudos exploram a viabilidade do GPR na região do tronco para identificar cavidades e deterioração no fuste. Contudo, ainda não é o método preferencial em comparação a técnicas mais consolidadas como ultrassom e penetrografia.
    """)

    col2.header("Concreto")

    col2.subheader("Método Eletromagnético (Pacometria)")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col3.image(
        "https://github.com/renansg67/vetores/blob/master/png/pacometria.webp?raw=true",
        caption="Bosch D-tect: detector por radar eletromagnético para localizar tubulações, cabos e estruturas ocultas com precisão."
    )

    col2.write("""
        A pacometria utiliza o princípio **eletromagnético** para a detecção de armaduras no concreto . O equipamento é capaz de:
        
        * Determinar a **espessura do cobrimento** (distância da superfície do concreto à armadura).
        * Estimar o **diâmetro das armaduras**.
        
        Tudo isso é feito **sem necessidade de abertura** de janelas de inspeção.
        
        É essencial coletar o máximo de informações do projeto estrutural para auxiliar na interpretação dos resultados, minimizando erros que podem ocorrer em função da profundidade e do arranjo complexo das armaduras.
    """)

    col2.markdown("##### Usos da Pacometria em outros Ensaios")

    col2.write("O mapeamento das armaduras fornecido pela pacometria é fundamental para o sucesso de diversos ensaios complementares:")

    col2.markdown("###### Pacometria no ensaio de esclerometria")

    col2.write("Deve ser realizada previamente para **evitar áreas com armadura**. A presença de aço superestima o índice esclerométrico, já que o ensaio avalia a dureza superficial (primeiros $20\\,\\text{mm}$). Cobrimentos finos, em especial, podem levar a imprecisões, tornando o mapeamento essencial para aferir a resistência à compressão efetiva do concreto.")

    col2.markdown("###### Pacometria no ensaio de ultrassonografia")

    col2.write("É imprescindível para **considerar ou evitar a influência do aço**. A velocidade de propagação do pulso acústico é maior no aço que no concreto. Regiões com alta concentração de aço podem superestimar a velocidade medida e, consequentemente, a resistência à compressão do concreto. O mapeamento auxilia a adaptar o ensaio ou a escolher pontos de medição distantes da armadura.")

    col2.markdown("###### Pacometria no ensaio de potencial de corrosão")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.write("""
        A pacometria é crucial para **localizar a armadura** e definir o local exato para a abertura de **janelas de inspeção**.
        
        O ensaio de potencial de corrosão é semi-destrutivo, pois requer uma pequena quebra para fixar o eletrodo de trabalho (polo positivo, vermelho)². A pacometria assegura que a abertura seja mínima e direcionada, tornando o procedimento o menos invasivo possível.
    """)

    col3.info("²Polo positivo, vermelho.")

    col2.markdown("###### Pacometria no ensaio de resistividade elétrica")

    col2.write("No ensaio de resistividade elétrica, a pacometria é fundamental em duas situações:")

    col2.write("""
        1. **Predisposição à Corrosão:** As regiões de armadura tendem a ser **evitadas**, pois o aço (baixa resistividade) influencia a medida superficial do concreto.
        2. **Taxa de Corrosão:** As regiões de armadura tendem a ser **buscadas** para medições pontuais.
        
        Em ambos os casos, o mapeamento preciso das armaduras melhora a qualidade e a confiabilidade dos dados obtidos.
    """)

    col2.markdown("###### Pacometria no ensaio de penetração de pinos")

    col2.write("É imprescindível para **evitar o disparo de pinos em regiões com armadura**. A maior rigidez do aço, em comparação ao concreto, reduziria a profundidade de penetração do pino, o que resultaria na superestimação dos valores de resistência à compressão do concreto (menor profundidade $\\rightarrow$ maior resistência).")

    col2.subheader("Ensaio de Penetração de Pinos")

    col2.write("O ensaio de penetração de pinos, ao relacionar a profundidade de penetração com as propriedades de resistência e rigidez, pode ser utilizado como ensaio de inspeção. A inspeção, neste contexto, verifica se o concreto atende ou não aos parâmetros de resistência requeridos pelo projeto.")

    col2.subheader("Ensaio de Raios X e $\\gamma$")

    # REVISÃO: Uso de lista para as diferenças e destaque para a segurança
    col2.write("""
        Estes ensaios utilizam **radiação ionizante** que atravessa a amostra, sensibilizando um filme radiográfico .
        
        * **Regiões Escuras:** Maior incidência de radiação (menor absorção pelo material, como vazios ou defeitos).
        * **Regiões Claras:** Maior absorção da radiação (material denso, como armaduras ou concreto sadio).
        
        **Atenção:** Devido aos riscos à saúde humana (mutações, câncer), é fundamental o cuidado ao manipular os equipamentos.
    """)

    col2.markdown("#### Diferenças entre Raios X e Raios $\\gamma$")
    
    col2.write("Os dois ensaios diferem em vários aspectos:")

    col2.markdown("""
        * **Fonte de Radiação:**
            * **Raios X:** Proveniente de um tubo de raios catódicos.
            * **Raios $\\gamma$:** Emitida por uma pastilha radioativa.
        * **Energia de Radiação:**
            * **Raios X:** Depende da corrente elétrica ($i$) e da tensão ($U$) aplicadas, e do material do alvo (tubo).
            * **Raios $\\gamma$:** Associada à composição do elemento constituinte da pastilha, que define sua capacidade de penetração.
        * **Complexidade e Logística:**
            * **Raios X:** Exige energia elétrica. Quanto maior a espessura da amostra, mais robusta é a instalação. Ao cessar a energia, a radiação para.
            * **Raios $\\gamma$:** Não exige energia elétrica. O aparato é mais constante em função da espessura, dependendo do elemento radioativo. A radiação é constante, exigindo isolamento com metais pesados (chumbo) na fonte.
        * **Espessura da Amostra:** O ensaio por **Raios $\\gamma$** é geralmente mais adequado para amostras de maior espessura, por não exigir mudanças consideráveis no aparato.
    """)

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col3.info("¹O aparato do ensaio de raios $\\gamma$ normalmente consiste num equipamento que permite aos operadores direcionarem, à distância, a pastilha radioativa até a extremidade de um tubo-guia com colimador. Os elementos são: Cabo de controle; fonte de radiação (com bom isolamento); tubo-guia e colimador. O filme radiográfico é disposto na extremidade oposta, com a amostra entre o colimador e o filme.")

    col2.markdown("#### Conclusão para Uso")

    col2.markdown("O uso deve ser adequado à situação. Em **locais isolados ou sem acesso à energia elétrica**, recomenda-se o ensaio de Raios $\\gamma$. Em ambos os casos, a área deve ser isolada com espaçamento adequado para minimizar os riscos para operadores e o público.")

    col2.subheader("Ensaio de Inspeção de Imagens")

    col2.write("""
        A inspeção por imagens é um método superficial, geralmente o primeiro a ser empregado, devido à sua facilidade. Consiste na avaliação de possíveis defeitos no material por meio de fotografias tiradas em diferentes locais .
        
        * **Limitação:** Nem todas as patologias são detectadas a olho nu.
        * **Exemplos de Falhas Ocultas:** Carbonatação (não altera características visuais) e descontinuidades subsuperficiais/internas.
        
        Portanto, o diagnóstico não pode se resumir a este ensaio, sendo imprescindível a utilização de técnicas complementares e mais tecnológicas para detalhar o estado real da estrutura.
    """)

    col2.subheader("Ensaio de Profundidade de Carbonatação")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.markdown("""
        Este ensaio é crucial em estruturas de concreto . É baseado no indicador de **fenolftaleína**:
        
        * **Concreto Alcalino ($\\text{pH}>9$):** Coloração **rosada**.
        * **Concreto Carbonatado ($\\text{pH}<9$):** Regiões ficam **incolores**.
        
        O fenômeno da carbonatação, apesar de aumentar a dureza e a resistência à compressão do concreto (devido à característica rochosa do material), é extremamente prejudicial à armadura, pois **causa a despassivação do aço**, aumentando sua susceptibilidade à corrosão.
    """)

    col3.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Reinforcement_corrosion.JPG/960px-Reinforcement_corrosion.JPG", caption="Corrosion of reinforcement in concrete, dgania b, israel")

    col3.image(
        "https://github.com/renansg67/vetores/blob/master/png/carbonatacao1.png?raw=true", 
        caption="Processo de formação de carbonato de cálcio $\\text{CaCO}_{3}$ em duas etapas.", 
        width=300
    )

    col2.write("O processo de despassivação ocorre quando a frente de carbonatação atinge ou ultrapassa a profundidade da armadura (cobrimento). O avanço da carbonatação depende de diversos fatores: o dimensionamento, a qualidade dos materiais, as condições de confecção e as características do ambiente (agressividade).")

    col2.markdown("#### Reações Químicas da Carbonatação")

    col2.markdown("Para que a carbonatação ocorra, é necessária a entrada de água e gás carbônico ($\\text{CO}_{2}$) em fissuras. O $\\text{CO}_{2}$ reage com a água, produzindo ácido carbônico:")

    col2.latex(
        r"\text{H}_{2}\text{O} + \text{CO}_{2} \rightarrow \underset{\text{(Ácido carbônico)}}{\text{H}_{2}\text{CO}_{3}}"
    )

    col2.markdown("O ácido carbônico reage, então, com o hidróxido de cálcio ($\\text{Ca(OH)}_{2}$) do concreto endurecido, formando o carbonato de cálcio ($\\text{CaCO}_{3}$):")

    col2.latex(r"\text{H}_2\text{CO}_3 + \text{Ca(OH)}_2 \rightarrow \text{CaCO}_3 + \text{H}_2\text{O}")

    col2.write("Este processo resulta na **diminuição do pH** do concreto (de $\\sim 13$ para neutro) na região afetada, o que leva à despassivação e posterior corrosão das armaduras.")

    col2.markdown("#### Reações Químicas da Corrosão por Carbonatação")

    col2.markdown("Após a despassivação, o ferro ($\\text{Fe}$) do aço da armadura perde elétrons, formando o íon ferro ($\\text{Fe}^{2+}$):")

    col2.latex(r"\text{Fe} \rightarrow \text{Fe}^{2+} + 2\,\text{e}^{-}")

    col2.write("Na presença de água e oxigênio (umidade atmosférica), o íon hidroxila ($\\text{OH}^{-}$) é produzido:")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col3.image(
        "https://github.com/renansg67/vetores/blob/master/png/carbonatacao2.png?raw=true", 
        caption="Estágios de avanço da frente de carbonatação.",    
    )

    col2.latex(r"\frac{1}{2}\text{O}_2 + \text{H}_2\text{O} + 2\,\text{e}^{-} \rightarrow 2\,\text{OH}^{-}")

    col2.write("Finalmente, na presença da água (que aumenta a mobilidade da hidroxila), o íon ferro e a hidroxila reagem, formando o hidróxido de ferro (ferrugem):")

    col2.latex(r"\text{Fe}^{2+} + 2\,\text{OH}^{-} \rightarrow \underset{\text{Ferrugem}}{\text{Fe(OH)}_2}")

    col2.markdown("#### Corrosão por Íon Cloreto ($\\text{Cl}^{-}$)")

    col2.markdown("A corrosão também pode ser iniciada pela ação do íon cloreto. O cloreto reage com a água, produzindo ácido clorídrico, que também reduz o pH:")

    col2.latex(r"\text{H}_2\text{O} + \text{Cl}^{-} \rightarrow \text{HCl} + \text{O}_2")

    col2.write("Na armadura, o íon cloreto reage com o íon ferro, formando cloreto férrico ($\\text{FeCl}_{2}$):")

    col2.latex(r"\text{Fe}^{2+} + 2\,\text{Cl}^{-} \rightarrow \text{FeCl}_2")

    col2.write("Este, na presença do íon hidroxila, reage formando o hidróxido de ferro (ferrugem):")

    col2.latex(r"\text{FeCl}_2 + \text{OH}^{-} \rightarrow \text{Fe(OH)}_2 + 2\,\text{Cl}^{-}")

    col2.subheader("Ensaio de Resistividade Elétrica")

    col2.markdown("""
        Este ensaio avalia a **predisposição das armaduras à corrosão** com base na medição da resistividade ($\\rho$) na superfície do concreto.
        
        A resistividade é uma grandeza física que quantifica a dificuldade do material em conduzir corrente elétrica, expressa geralmente em $\\text{k}\\Omega\\,\\text{cm}$ para concreto.
    """)

    col2.latex(r"\rho=\dfrac{RA}{L}")

    col2.markdown("""
        * $R$: resistência elétrica ($\\Omega$)
        * $A$: área da seção transversal do material condutor
        * $L$: comprimento do condutor
        
        **Regra Geral:** Valores mais baixos de resistividade indicam **maior risco de corrosão**, ou seja, menor longevidade e durabilidade.
        
        #### Cuidados no Ensaio
        
        1. **Idade da Estrutura:** Estruturas recém-construídas apresentam resistividade mais baixa (maior teor de água), exigindo adaptações na interpretação. Estruturas antigas fornecem medidas mais confiáveis.
        2. **Preparo da Área:** É fundamental certificar-se da limpeza e uniformidade da superfície.
        3. **Fatores a Evitar:**
            * Áreas com presença de armadura (aço reduz a resistividade).
            * Áreas com carbonatação (carbonatação eleva a resistividade e pode levar a interpretações incorretas).
            * Locais com excesso de umidade ou superfícies irregulares.
        
        **Requisito Prévio:** Ensaios de **profundidade de carbonatação** e de **pacometria** (detecção magnética das armaduras) são requisitos fundamentais antes do ensaio de resistividade.
    """)

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.write("Pesquisadores elaboraram tabelas para facilitar a interpretação da resistividade em relação ao risco e à taxa de corrosão, em diferentes condições de medição:")

    col3.info("¹Estimativa de Probabilidade: A aferição deve ser feita na superfície do concreto **evitando áreas com armadura**.")

    col3.info("²Indicação de Taxa: A aferição deve ser feita na superfície do concreto **em áreas com presença de armadura**.")

    data = [
        {"$\\rho (\\text{k}\\Omega\\,\\text{cm})$": "$\\rho\\geq 100$",      "Risco de corrosão": "🟢 Insignificante"},
        {"$\\rho (\\text{k}\\Omega\\,\\text{cm})$": "$50 < \\rho < 100$", "Risco de corrosão": "🟡 Baixo"},
        {"$\\rho (\\text{k}\\Omega\\,\\text{cm})$": "$10 < \\rho < 50$",  "Risco de corrosão": "🟠 Moderado"},
        {"$\\rho (\\text{k}\\Omega\\,\\text{cm})$": "$\\rho\\leq 10$",       "Risco de corrosão": "🔴 Elevado"},
    ]

    col2.table(data)

    col2.caption("Estimativa de probabilidade de corrosão.")

    data = [
        {"$\\rho\\,(\\text{k}\\Omega\\,\\text{cm})$": "$\\rho > 100$",      "Taxa de corrosão": "🟡 Baixa"},
        {"$\\rho\\,(\\text{k}\\Omega\\,\\text{cm})$": "$10 < \\rho < 20$",  "Taxa de corrosão": "🟠 Baixa a moderada"},
        {"$\\rho\\,(\\text{k}\\Omega\\,\\text{cm})$": "$5 < \\rho < 10$",   "Taxa de corrosão": "🔴 Alta"},
        {"$\\rho\\,(\\text{k}\\Omega\\,\\text{cm})$": "$\\rho < 5$",        "Taxa de corrosão": "🟣 Muito alta"},
    ]

    col2.table(data)

    col2.caption("Indicação da taxa de corrosão.")

    col2.subheader("Ensaio de Potencial de Corrosão")

    # REVISÃO: Texto estruturado em lista para os passos e componentes do eletrodo
    col2.write("O objetivo é estimar a **probabilidade de corrosão** nas armaduras com base na diferença de potencial (tensão) medida entre o eletrodo de trabalho (fixado na armadura) e o eletrodo de referência.")

    col2.table(data)
    
    col2.write("A tabela abaixo mostra as probabilidades de corrosão conforme a **ASTM 876-C:2022**:")

    data = [
        {"U (mV)": "$U > -200$",        "Probabilidade (%)": "🟢 5"},
        {"U (mV)": "$-350 < U < -200$", "Probabilidade (%)": "🟠 Duvidosa"},
        {"U (mV)": "$U < -350$",        "Probabilidade (%)": "🔴 95"},
    ]

    col2.table(data)

    col2.markdown("#### Passos para a Execução do Ensaio ")

    col2.write("""
        1. **Definição da Área:** Definir o lote ou área de inspeção.
        2. **Percussão:** Realizar o ensaio de percussão para encontrar regiões com som cavo.
        3. **Pacometria:** Utilizar a pacometria para a detecção e mapeamento das armaduras.
        4. **Preparo:** Escarificação do local para garantir uniformidade e limpeza.
        5. **Janela de Inspeção:** Abrir uma janela de inspeção para acessar e expor parte da armadura.
        6. **Carbonatação:** É recomendado realizar o ensaio de carbonatação na janela aberta para verificar a despassivação da armadura.
        7. **Medição:** Aplicar solução tensoativa (detergente) e fixar o **eletrodo de trabalho** (Vermelho, +) na armadura exposta. Com o **eletrodo de referência** (Porta COM, preto, -) realizar as medidas em vários pontos da área.
    """)

    col2.markdown("#### Eletrodo de Referência ($\\text{Cu}/\\text{CuSO}_{4}$)")

    col2.markdown("""
        O eletrodo de referência de Sulfato de Cobre/Cobre é composto por:
        * Tubo roscado nas extremidades.
        * Tampa traseira (encaixe *plug*, o-ring, haste de cobre).
        * Tampa dianteira (o-ring, disco de madeira, esponja).
        * Solução interna de água e sulfato de cobre (ponto de supersaturação).
    """)

    col2.write("O tratamento de dados recomendado pela ASTM envolve a construção de **curvas equipotenciais** para mapear as áreas de maior corrosão. A correção do processo de corrosão geralmente envolve o uso de inibidores seguido de inspeções periódicas de acompanhamento.")

    col2.image(
        "https://github.com/renansg67/vetores/blob/master/png/pot-corrosao.png?raw=true",
        caption="Mapa de curvas equipotencias apresentando armadura em estágio avançado de corrosão."
    )

    col2.subheader("Radar de Penetração de Solo (GPR)")

    col2.write("""
        Em estruturas de concreto, o GPR (Radar de Penetração de Solo) é primariamente útil para o **mapeamento das armaduras** .
        
        * **Modelagem 3D:** É capaz de fornecer modelos 3D precisos das áreas mapeadas.
        * **Aplicação:** É essencial quando as informações de projeto são escassas, e também auxilia em outros ensaios que exigem o posicionamento exato das armaduras internas (como pacometria, ultrassom, etc.).
    """)

    col2.subheader("Termografia")

    col2.write("""
        A Termografia no concreto é usada para detectar **falhas superficiais ou subsuperficiais** que causam diferenças na radiação térmica emitida pela superfície .
        
        * **Detecção:** É comum ser utilizada para detectar desplacamento do concreto, fissuras, regiões com umidade ou vazios (ar) na estrutura. Em casos específicos, pode detectar a presença de armaduras.
        * **Princípio:** Falhas (vazios, umidade) alteram as propriedades de condução térmica do material. Regiões sãs e com defeitos aquecem e esfriam em tempos distintos, apresentando gradientes de temperatura que são detectados pela câmera.
        
        **Recomendação:** É um método de direcionamento. Requer o uso de outros ENDs para detalhar e estimar os danos, especialmente em regiões mais profundas e internas da estrutura.
    """)

    col2.info("""
        **Referências Bibliográficas**
              
        * **FALCÃO BAUER**, **L. A.** Materiais de Construção. 6. ed. Rio de Janeiro: LTC – Livros Técnicos e Científicos, 2019.
              
        * **ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS**. NBR 7190:2022 — Projeto de estruturas de madeira. Rio de Janeiro: ABNT, 2022.      
        
        * **ANDRADE, Silvio.** Carbonatação do Concreto. YouTube, 2016. Disponível em: https://www.youtube.com/watch?v=6up9gQ1Doik. Acesso em: 10/12/2025.      
        
        * **LEONI, Matheus.** Aula #111 - Ensaio de potencial de corrosão: o que você precisa saber sobre ele?. YouTube, 2023. Disponível em: https://www.youtube.com/watch?v=4pvZt_55DjQ. Acesso em: 10/12/2025.      
        
        * **LEONI, Matheus.** Aula #117 Qual câmera térmica comprar para começar na termografia?. YouTube, 2023. Disponível em: https://www.youtube.com/watch?v=wEntHZkZZT0. Acesso em 10/12/2025.
        
        * **SANTOS, Ibere.** AULA ON LINE EM 21 10 20 ENSAIO RADIOGRÁFICO. YouTube, 2020. Disponível em: https://www.youtube.com/watch?v=qJqPGt3ucDc. Acesso em: 10/12/25
        """)

if __name__ == "__main__":
    inspecao_concreto()