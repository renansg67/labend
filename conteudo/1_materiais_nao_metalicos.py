import streamlit as st
from assets.fft_tools import plot_fft_analysis
import numpy as np

def materiais_nao_metalicos_page():
    col1, col2, col3 = st.columns([.25, 3, 1.5])

    # REVISÃO: Título mais conciso e profissional
    col2.title("Ensaios Não Destrutivos (END) em Materiais de Construção Não Metálicos")

    col3.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Reciprocal_roof_structure%2C_the_Octagonal_Shelter%2C_Mags_Wood_in_Evanton_Community_Wood_%28geograph_6866216%29.jpg/960px-Reciprocal_roof_structure%2C_the_Octagonal_Shelter%2C_Mags_Wood_in_Evanton_Community_Wood_%28geograph_6866216%29.jpg", caption="Estrutura de Cobertura Recíproca ('Reciprocal Roof'), o Abrigo Octogonal em Mags Wood. **Crédito e Licença:** Julian Paren, via geograph.org.uk (CC BY-SA 2.0).")

    col2.expander(":material/book: Sumário", expanded=True).markdown('''
        - [Início](#inicio)
        - [Concreto](#concreto)
            - [Ensaio de Dureza Superficial (Esclerometria)](#ensaio-de-dureza-superficial-esclerometria)
            - [Ensaio de Propagação de Ondas de Tensão](#ensaio-de-propagacao-de-ondas-de-tensao)
                - [Método da Frequência de Ressonância](#metodo-da-frequencia-de-ressonancia)
                - [Método da Propagação de Pulso Ultrassônico](#metodo-da-propagacao-de-pulso-ultrassonico)
            - [Ensaio de Penetração de Pinos](#ensaio-de-penetracao-de-pinos)
        - [Madeira](#madeira)
            - [Métodos de Frequência de Ressonância](#metodos-utilizando-a-frequencia-de-ressonancia)
                - [Método de Vibração Transversal](#metodo-de-vibracao-transversal)
                - [Método dos Modos de Vibração](#metodo-dos-modos-de-vibracao)
            - [Ensaio de Flexão Estática](#ensaio-de-flexao-estatica)
            - [Método da Propagação de Ondas de Tensão](#metodo-da-propagacao-de-ondas-de-tensao)
                - [Barra Viscoelástica Submetida a um Impacto](#barra-viscoelastica-submetida-a-um-impacto)
                - [Cronometragem do Tempo de Propagação (ToF)](#cronometragem-do-tempo-de-propagacao-da-onda-de-tensao)
                - [Método do Pulso-Eco](#metodo-do-pulso-eco)
                - [Pitch and Catch](#pitch-and-catch)
    ''')
                                
    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.header("Início")
    
    col3.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/HD.6D.698_%2812365544204%29.jpg/960px-HD.6D.698_%2812365544204%29.jpg", caption="Um dispositivo de monitoramento revolucionário, capaz de detectar instantaneamente falhas em soldas, foi desenvolvido no Laboratório do Noroeste do Pacífico como parte do programa de pesquisa e desenvolvimento em ensaios não destrutivos da AEC. (c. 1970)")

    # REVISÃO: Parágrafo 1 - Simplificação e melhoria da fluidez
    col2.write("""
        Os materiais de construção não metálicos, como o concreto e a madeira, são amplamente utilizados em estruturas. Nas últimas décadas, com o avanço das técnicas e do conhecimento na área, os Ensaios Não Destrutivos (END) têm sido empregados para complementar e facilitar a caracterização desses materiais.
        
        A utilização de ENDs permite maior escalabilidade na avaliação das condições de resistência e rigidez do material ensaiado. Além de complementar os ensaios destrutivos, os ENDs podem, em muitos casos, encurtar o caminho até a caracterização final e, em estudos com correlações bem estabelecidas, até dispensar métodos destrutivos que demandam mais tempo de execução.
    """)

    # REVISÃO: Parágrafo 2 - Concreto - Simplificação e uso de listas
    col2.write("""
        Embora o concreto contenha armaduras metálicas para resistir aos esforços de tração, ele é avaliado por meio de ensaios específicos focados nas características da própria matriz de concreto.
        
        Isso possibilita a avaliação da influência de seus diversos componentes (cimento, agregados miúdos e graúdos) e permite a caracterização por meio de:

        * **Ensaios Semidestrutivos:** como o ensaio de penetração de pinos.
        * **Ensaios Não Destrutivos:** como a esclerometria (dureza superficial) e a propagação de ondas de tensão (procedimentos vibracionais e ultrassônicos).

        Para a aplicação correta desses ensaios, é fundamental uma avaliação prévia dos fatores que podem influenciá-los, como degradação por intempéries. Este capítulo abordará esses fenômenos e a importância de condições de ensaio adequadas para obtenção de dados coerentes de resistência à compressão e rigidez. Tais análises aprimoram tanto os ensaios de laboratório (corpos de prova) quanto os conduzidos em estruturas reais.

        As principais normas brasileiras utilizadas são: **ABNT NBR 7584:2012** (medição da dureza superficial para o concreto endurecido) e **ABNT NBR 8802:2019** (ensaio de ultrassom).
    """)

    # REVISÃO: Parágrafo 3 - Madeira - Simplificação e melhoria da fluidez
    col2.write("""
        Para a madeira, diversos métodos de ensaio análogos aos do concreto são utilizados com as devidas adaptações. Por ser um material **ortotrópico** — apresentando propriedades elásticas distintas em três planos ortogonais de isotropia — a maior dificuldade reside em sua elevada heterogeneidade.
        
        A aplicação de ENDs, como a propagação de ondas de tensão, tem crescido devido à correlação com as propriedades de resistência e rigidez. O ensaio de flexão estática, normatizado pela **ABNT NBR 7190:2022**, é essencial para caracterizar a propriedade de rigidez. Essa norma, por sua vez, valida a incorporação de métodos vibracionais que calculam o módulo de elasticidade a partir da frequência fundamental de ressonância, obtida por análise de Fourier.

        Nesta parte, serão detalhados o método de **vibração transversal** (barra biapoiada) e o dos **modos de vibração** (cálculo de módulos de elasticidade longitudinal e transversal a partir de modos flexionais e torsionais).
    """)

    col2.header("Concreto")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col3.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Burden_Poured_Concrete_Bunker_01.jpg/960px-Burden_Poured_Concrete_Bunker_01.jpg", caption="Chris Burden – 'Pouren Concrete Bunker' (2003). Estação ferroviária de Deutschlandsberg, Estíria (Áustria).")
    
    col3.info("""
        **Ensaios não destrutivos em estruturas em concreto: Aplicação e métodos de ensaio**
              
        Canal: Instituto de Engenharia
              
        [Link para YouTube](https://www.youtube.com/watch?v=eFt-84qv7TU)
    """)

    # REVISÃO: Subheader com o termo técnico "Esclerometria"
    col2.subheader("Ensaio de Dureza Superficial (Esclerometria)")

    # REVISÃO: Quebra de parágrafo 2 em lista para melhor visualização da etapa normativa
    col2.write("""
        Este ensaio mede, através do impacto, a dureza superficial do concreto, avaliada nos primeiros 2 cm da superfície. A leitura é um valor adimensional baseado na reflexão do êmbulo.
        
        Devido à repetibilidade exigida, é crucial seguir rigorosamente a **ABNT NBR 7584:2012** para a calibração e execução:
        
        **1. Calibração:**
        * Utilizar uma bigorna específica.
        * Realizar no mínimo 10 impactos para obter um índice esclerométrico igual a 80.
        * O **fator de correção ($k$)** do esclerômetro é calculado a partir dos índices obtidos e do índice nominal ($I_{E_{\\text{nom}}}$), fornecido pelo fabricante:
    """)

    col2.markdown(r'''
    $$
            k=\dfrac{n I_{E_{\text{nom}}}}{\displaystyle\sum_{i=1}^{n}I_{E_{i}}}
    $$''', width="stretch")

    col2.write("""
        **2. Ensaio na Área de Interesse:**
        * Definir uma área de ensaio (entre 9 cm² e 20 cm²).
        * Realizar pelo menos 16 impactos, com pontos distintos e distando, no mínimo, 3 cm entre si.
        * Calcular o índice esclerométrico médio da área.
        * **Descarte:** Eliminar índices que distoem em mais de 10% da média calculada. Pelo menos 5 valores devem ser mantidos para a área ser considerada válida.
        * Calcular a nova média (Índice Esclerométrico Médio, $I_E$).
        
        **3. Ajuste Final:**
        * O valor final (Índice Esclerométrico Médio Efetivo, $I_{E_\\alpha}$) é ajustado pelo coeficiente de correção ($k$):
    """)

    col2.markdown(r'''
    $$
            I_{E\alpha}=k\cdot I_{E}
    $$''', width="stretch")

    # REVISÃO: Parágrafo 3 em lista para fatores de influência
    col2.write("""
        **Recomendações e Fatores de Influência:**

        * **Preparação da Superfície:** A área deve ser limpa por polimento (disco ou prisma de carborundum, ou máquina politriz).
        * **Umidade:** Superfícies úmidas devem ser evitadas, pois a umidade tende a **subestimar** o índice.
        * **Carbonatação:** Concreto carbonatado deve ser evitado, pois a carbonatação tende a **superestimar** o valor, devido ao aumento da dureza superficial.
        * **Posicionamento:** A superfície de ensaio deve ser preferencialmente vertical, e o esclerômetro deve ser posicionado ortogonalmente à superfície.
        * **Elementos Estruturais:** Evitar áreas com dimensões menores que 100 mm na direção de impacto, ou usar um apoio na face oposta para aumentar a rigidez do elemento, prevenindo ressonância, vibração e dissipação de energia.
        * **Heterogeneidade:** Quanto maior a heterogeneidade, maior deve ser a quantidade de áreas de ensaio. Cada área de ensaio fornece apenas um índice esclerométrico médio efetivo.
    """)

    col2.subheader("Ensaio de propagação de ondas de tensão")

    col2.write("""
        A análise neste ensaio baseia-se na interpretação do sinal de ondas mecânicas (acústicas) produzidas no meio. A frequência de propagação varia conforme a excitação do corpo de prova ou estrutura:
        
        * **Ondas Acústicas (Audíveis):** Baixa frequência, produzidas tipicamente por um impacto na superfície.
        * **Ondas Ultrassônicas:** Frequência acima de 20 kHz, produzidas por transdutores específicos.

        Os métodos subsequentes são dinâmicos e envolvem a propagação de ondas de tensão, que podem ser de curta ou longa duração.
        
        * **Método da Frequência de Ressonância:** Pode ser realizado em regime **transiente** (mudança abrupta, impacto) ou **estacionário** (estímulos vibracionais de maior duração).
        * **Propagação de Ondas Ultrassônicas:** Utiliza diferentes arranjos de transdutores para determinar o intervalo entre a emissão e a recepção do sinal acústico, permitindo o cálculo da velocidade de propagação e, consequentemente, do módulo de elasticidade na direção de ensaio.
    """)

    col2.write("""
        As principais ondas empregadas são: **ondas longitudinais** (pressão ou compressão) e **ondas transversais** (cisalhamento). A escolha do transdutor define o tipo de onda transmitida.

        A velocidade de propagação para ondas longitudinais ($V_{L}$) é dada por:
    """)

    col2.markdown(r'''
    $$
            V_{L}=\sqrt{\dfrac{2\mu+\lambda}{\rho}}
    $$''', width="stretch")

    col2.write("em que $\\mu$ e $\\lambda$ são os parâmetros de Lamé, que relacionam as propriedades elásticas de um material e podem ser expressos em função do módulo de elasticidade longitudinal ($E$), do módulo de elasticidade transversal ($G$), e do coeficiente de Poisson ($\\nu$):")

    col2.markdown(r'''
        $$
            \begin{matrix}\mu=G=\dfrac{E}{2(1 + \nu)} & \lambda=\dfrac{E\nu}{(1+\nu)(1-2\nu)}\end{matrix}
        $$
    ''')

    col2.write("Para ondas transversais, a equação é simplificada, não dependendo de $\\lambda$:")

    col2.markdown(r'''
    $$
            V_{T}=\sqrt{\dfrac{\mu}{\rho}}
    $$''', width="stretch")

    col2.write("Outras relações fundamentais, como o módulo volumétrico ($\\kappa$), obtido sob pressão simultânea em todas as faces de um elemento cúbico infinitesimal, são apresentadas:")

    col2.markdown(r'''
    $$
            \kappa=\dfrac{E}{3(1-2\nu)}
    $$''', width="stretch")

    col2.write("O módulo de elasticidade ($E$) e o coeficiente de Poisson ($\\nu$) também podem ser reescritos em função de $\\mu$ e $\\lambda$:")

    col2.markdown(r'''
    $$
            E=\dfrac{\mu(2\mu+3\lambda)}{\mu+\lambda}
    $$''', width="stretch")

    col2.write("e")

    col2.markdown(r'''
    $$
            \nu=\dfrac{\lambda}{2(\mu+\lambda)}
    $$''', width="stretch")

    col2.write("Ao expressar a lei de Hooke em função dos parâmetros de Lamé, considerando as tensões principais ($\\sigma$) e as deformações principais ($u$):")

    col2.markdown(r'''
    $$
            \begin{array}{rcl}   
                \sigma_{xx}&=&(2\mu+\lambda)u_{xx}+\lambda(u_{yy}+u_{zz})\\
                \sigma_{yy}&=&(2\mu+\lambda)u_{yy}+\lambda(u_{xx}+u_{zz})\\
                \sigma_{zz}&=&(2\mu+\lambda)u_{zz}+\lambda(u_{xx}+u_{yy})
            \end{array}
    $$''', width="stretch")

    col2.write("e as seguintes condições de carregamento:")

    col2.markdown(r'''
    $$
            P=(2\mu+\lambda)\left(\dfrac{P}{E}\right)+\lambda\left(-\dfrac{2\nu P}{E}\right)
    $$''', width="stretch")

    col2.markdown(r'''
    $$ 
            0=(2\mu+\lambda)\left(-\dfrac{\nu P}{E}\right)+\lambda\left(\dfrac{P}{E}-\dfrac{\nu P}{E}\right)
    $$''', width="stretch")

    # REVISÃO: Conclusão do bloco matemático mais clara
    col2.markdown("a partir das quais se derivam as equações que relacionam $\\lambda=f(E,\\nu)$, $\\nu=f(\\mu,\\lambda)$ e $E=f(\\mu,\\lambda)$.")

    col2.markdown("##### Método da frequência de ressonância")

    col2.write("""
        No concreto, este ensaio visa determinar as propriedades de rigidez do material. O corpo de prova é posicionado em um sistema vibratório, recebe um impacto externo, e o sistema de medição realiza a análise de sinais com base no intervalo de frequências. O resultado é o **módulo de elasticidade dinâmico** do corpo de prova.

        A **ABNT NBR 8522-2:2021** fornece as diretrizes para a conversão desse valor no **módulo de elasticidade estático ($E_{\\text{est}}$)**. Métodos empíricos alternativos consideram: massa do corpo de prova ($M$), formato (prismático, circular ou retangular) e a frequência de ressonância ($n$).
    """)

    col2.write("Uma equação que relaciona esses elementos é:")

    col2.markdown(r'''
    $$
            E_{\text{din}}=CMn^{2}
    $$''', width="stretch")

    col2.markdown("em que $C$ é o fator de forma, $M$ é a massa do corpo de prova e $n$ é a frequência de ressonância fundamental.")

    # REVISÃO: Correção da repetição do parágrafo
    col2.write("""
        Um corpo de prova possui várias frequências de vibração que produzem amplitudes elevadas. A **frequência fundamental de ressonância** é caracterizada por ser a primeira frequência (primeiro harmônico) que gera uma amplitude de vibração significativamente maior que as anteriores.
    """)

    col2.markdown("##### Método da propagação de pulso ultrassônico")

    col2.write("O Módulo de Elasticidade Dinâmico ($E_{\\text{din}}$) e a velocidade de propagação do pulso ultrassônico ($V$) são relacionados por:")

    col2.markdown(r'''
    $$
            E_{\text{din}}=f(\rho,\nu,V)
    $$''', width="stretch")

    col2.markdown(r'''
    $$
            V=\sqrt{\dfrac{E_{\text{din}}(1-\nu)}{\rho(1+\nu)(1-2\nu)}}
    $$''', width="stretch")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.write("Módulo de elasticidade estático¹")

    col3.info("¹Tanto o módulo de elasticidade estático quanto a resistência à compressão podem ser obtidos de maneira experimental por meio do ensaio de propagação de ondas, desde que o concreto ensaiado possua similaridade com aqueles em que já foram estabelecidas funções de correlação dependentes da velocidade do pulso ultrassônico.")

    col2.markdown(r'''
    $$
            E=f(V)
    $$''', width="stretch")

    col2.write("Resistência à compressão")

    col2.markdown(r'''
    $$
            f_{C}=f(V)
    $$''', width="stretch")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.write("Fatores que afetam a velocidade de propagação do pulso ultrassônico no concreto²")

    # REVISÃO: Formato de lista no st.info para melhor leitura
    col3.info("""
        **²Fatores de Influência:**
        * Idade do concreto
        * Massa específica do concreto
        * Massa específica, tipo e características dos agregados
        * Temperatura e umidade
        * Efeito da armadura (teórico e em estruturas reais)
        * Tipo de cimento
        * Tipo de cura
        * Tipo de adensamento
        * Direção de ensaio
    """)

    col2.subheader("**Ensaio de penetração de pinos**")

    col2.write("""
        Ensaio **semidestrutivo** que utiliza um dispositivo carregado com pólvora para disparar um pino contra o corpo de prova ou estrutura. A resistência do concreto à compressão é estimada com base na profundidade de penetração do pino.

        As correlações associam diretamente a profundidade de penetração à resistência à compressão. Por isso, é fundamental um conhecimento prévio das propriedades do concreto (em laboratório) para estabelecer correlações de resistência confiáveis em estruturas reais.

        **Precauções:** Devem ser consideradas as condições do ensaio e um estudo preliminar deve ser realizado para evitar:
        
        * Áreas com alta concentração de armaduras.
        * Regiões com concreto carbonatado ou com presença de umidade.

        O ensaio é mais indicado para concretos endurecidos de **maior resistência**, assegurando que o pino não exceda o limite de penetração estabelecido pela norma.
    """)

    col2.header("Madeira")

    col2.write("""
        A caracterização de peças em madeira segue a **ABNT NBR 7190:2022**. A norma exige que as propriedades de resistência e rigidez sejam obtidas na **condição-padrão**, com a umidade das peças em **12%**. Ou seja, caso a umidade seja diferente deste valor, os parâmetros obtidos precisam ser reajustados para a condição aparente, caso a umidade fosse de 12%.

        A umidade em base seca ($U_{\\text{BS}}$) é calculada por:
    """)

    col2.markdown(r'''
    $$
            U_{\text{BS}}=\dfrac{m_{\text{total}}-m_{\text{seca}}}{m_{\text{seca}}}=\dfrac{m_{\text{água}}}{m_{\text{seca}}}
    $$''', width="stretch")

    col2.markdown("""
        Enquanto que a umidade em base úmida é dada por
    """)

    col2.markdown(r"""
                  $$
            U_{\text{BU}}=\dfrac{m_{\text{água}}}{m_{\text{total}}}
        $$""")
    
    col2.markdown("onde $m_{\\text{total}}=m_{\\text{água}} + m_{\\text{seca}}$")

    col2.markdown(
        "Além da umidade, consideram-se os diferentes tipos de densidade medidos em amostras de madeira: Densidade básica ($\\rho_{\\text{b\\'{a}sica}}$) e densidade aparente ($\\rho_{\\text{aparente}}$). "
        "Essas grandezas são definidas por:"
    )

    col2.markdown(r'''
    $$
            \begin{matrix}
                \rho_{\text{básica}}=\dfrac{m_{\text{seca}}}{v_{\text{saturado}}} & \rho_{\text{aparente}}=\dfrac{m_{\text{aparente}}}{v_{\text{aparente}}}
            \end{matrix}
    $$''', width="stretch")

    col2.write("As propriedades de resistência ($f$) e rigidez ($E$) podem ser corrigidas para a umidade-padrão de 12% conforme as seguintes equações, onde $U$ é a umidade atual:")

    col2.markdown(r'''
    $$
            \begin{array}{rcl}
                f_{12}&=f_{U}\big(1+0.03(U-12)\big)\\
                E_{12}&=E_{U}\big(1+0.02(U-12)\big)
            \end{array}
    $$''', width="stretch")

    col2.write("Com essas considerações, a caracterização pode ser realizada utilizando métodos como: vibração transversal, modos de vibração, flexão estática e propagação de ondas de tensão.")

    col2.subheader("**Métodos utilizando a frequência de ressonância**")

    col2.markdown("##### Método de vibração transversal")

    col2.write("O método consiste em submeter uma barra de madeira biapoiada a uma deflexão inicial e liberá-la para oscilar verticalmente. O sistema de medição determina a frequência de ressonância fundamental ($f$), permitindo o cálculo do Módulo de Elasticidade (MOE) por meio da equação:")

    col2.markdown(r'''
    $$
            \text{MOE}=\dfrac{f^{2}WS^{3}}{2.46Ig}
    $$''', width="stretch")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.write("a partir do aparato experimental abaixo:")

    col2.container(horizontal_alignment="center").image(
        "imagens/vibracao-transversal-livre.png",
        width=650
    )

    col2.markdown("##### Método dos modos de vibração")

    col2.write("""
        Este método envolve a análise de Fourier do gráfico de amplitude do sinal em um intervalo de frequências. Existem três modos de vibração utilizados para caracterização: **longitudinal, flexural e torsional**.
        
        O ensaio impacta uma das extremidades da barra de madeira, e microfones condensadores na extremidade oposta, associados a um circuito medidor, capturam o gráfico da ação combinada de deslocamentos. Após a decomposição dos gráficos para cada modo de vibração, são determinadas as frequências de ressonância da amostra.

        Com essa grandeza, é possível calcular o módulo de elasticidade ($E$) e o módulo de cisalhamento ou elasticidade transversal ($G$):
    """)

    col1, col2, col3 = st.columns([.25, 3, 1.5])
    
    with col2:
        st.write("""
            A **Análise de Fourier**, usando a Transformada Rápida de Fourier (FFT), é a base para entender ensaios vibracionais e acústicos. Ela nos permite ver a composição interna de um sinal.
            
            Um sinal complexo capturado no **Domínio do Tempo** (gráfico esquerdo) é decomposto em suas frequências constituintes no **Domínio da Frequência** (gráfico direito).
        """)
        


        # --- PARÂMETROS GLOBAIS ---
        fs = 1000       # Taxa de amostragem (1000 amostras por segundo)
        duracao = 5     # Duração do sinal (5 segundos)
        N = fs * duracao # Número total de pontos
        t = np.linspace(0.0, duracao, N, endpoint=False)

        # --- GERAÇÃO DE UM SINAL COMPLEXO GENÉRICO ---
        # Componente 1: Frequência Base (10 Hz, amplitude alta)
        f1 = 10  
        amp1 = 1.0
        # Componente 2: Harmônico ou Frequência Secundária (30 Hz, amplitude média)
        f2 = 30
        amp2 = 0.5
        # Ruído de fundo (para um espectro mais realista)
        ruido = 0.15 
        
        sinal_generico = (
            amp1 * np.sin(2.0 * np.pi * f1 * t) +
            amp2 * np.sin(2.0 * np.pi * f2 * t) +
            ruido * np.random.randn(N)
        )
        
        # Gera os gráficos usando a função importada
        fig_tempo_gen, fig_freq_gen = plot_fft_analysis(sinal_generico, fs, "Exemplo")


        # --- EXIBIÇÃO NO STREAMLIT ---
        
        st.subheader("Visualização e Decomposição do Sinal")
        
        col_t_gen, col_f_gen = st.columns(2)
        
        with col_t_gen:
            st.plotly_chart(fig_tempo_gen)
            st.markdown(f"Domínio do Tempo: Mostra a amplitude total do sinal em função do tempo. A onda parece complexa porque é a **soma** de todas as frequências presentes.")

        with col_f_gen:
            st.plotly_chart(fig_freq_gen)
            st.markdown(f"Domínio da Frequência (FFT): Separa o sinal em picos. Vemos dois picos principais, um em **{f1} Hz** (o mais alto, amplitude {amp1}) e outro em **{f2} Hz** (amplitude {amp2}), que são as frequências que compõem o sinal.")

    col2.write("Modo de Vibração Longitudinal:")

    col2.markdown(r'''
    $$
            E=4\rho L^{2}\left(\!\dfrac{f_{L,n}}{n}\!\right)^{2}
    $$''', width="stretch")

    col2.write("Modo Flexional:")

    col2.markdown(r'''
    $$
            E=\dfrac{4\pi^{2}L^{4}\rho f_{F,n}^{2}A}{Ik_{i}^{4}}
    $$''', width="stretch")

    col2.write("Modo Torsional:")

    col2.markdown(r'''
    $$
            G=4\rho l^{2}\left(\dfrac{f_{n}^{T}}{n}\right)^{2}
    $$''', width="stretch")

    col2.subheader("**Ensaio de flexão estática**")

    col2.write("""
        Para a determinação do módulo de elasticidade, pode-se empregar o ensaio de 3 pontos ou o de 4 pontos. A **ABNT NBR 7190 (Parte 4)** permite a determinação do módulo de elasticidade na flexão estática para lotes de florestas plantadas não homogêneos, utilizando a equação:
    """)

    col2.markdown(r'''
    $$
            E_{0}=\dfrac{1}{4}\left(\dfrac{L}{b}\right)^{\!\!3}\dfrac{\Delta F}{\Delta e}\dfrac{1}{h}
    $$''', width="stretch")

    col2.write("Essa equação é obtida pela combinação da equação de Euler para a deflexão no meio do vão livre e do momento de inércia da seção retangular:")

    col2.markdown(r'''
    $$
            \begin{matrix}
                \Delta e=\dfrac{\Delta FL^{3}}{48E_{0}I} & I = \dfrac{b^{3}h}{12}
            \end{matrix}
    $$''', width="stretch")

    col2.write("seguindo o aparato experimental mostrado:")

    
    col2.container(horizontal_alignment="center").image(
        "imagens/flexao-3-pontos.png", 
        caption="Ensaio de 3 pontos de viga deitada.",
        width=650
    )

    col2.markdown("""
        Para que o ensaio seja considerado **não destrutivo** (ou minimamente destrutivo), a carga $\\Delta F$ aplicada deve ser limitada a **$10\\%$ a $40\\%$ da carga máxima de ruptura** da peça, a qual precisa ser estimada previamente. O módulo de elasticidade $E_{0}$ é então calculado a partir da deflexão máxima $\\Delta e$, obtida por sensores de deslocamento.
    """)

    col2.subheader("Método da propagação de ondas de tensão")

    col2.markdown("""
        O método de propagação de ondas de tensão envolve a transmissão de ondas ultrassônicas, seja por **impacto** (regime transiente) ou por **transdutores** que emitem feixes com frequências acima da audível (regime estacionário).

        Ambos os regimes são utilizados em diferentes contextos de ensaio: Cronometragem do Tempo de Propagação (ToF), Pulso-Eco e Pitch and Catch.
    """)

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col3.image(
        "imagens/curva-atenuacao.png", 
        caption="Curva de atenuação com decaimento exponencial.",
        width=350
    )

    col2.markdown("##### Barra viscoelástica submetida a um impacto")

    col2.write("""
        Para introduzir os métodos a seguir, considere uma barra viscoelástica submetida a um impacto (curta duração) em uma das extremidades. Uma onda de compressão é produzida e atravessa o material longitudinalmente até a interface madeira-ar na extremidade oposta.
        
        Devido à grande diferença de impedância acústica, a quase totalidade do feixe é refletida. A onda de compressão é convertida em onda de tração, mas a direção de vibração das partículas, na direção longitudinal, permanece inalterada.

        A intensidade do sinal ultrassônico decai exponencialmente com a distância percorrida ($x$), conforme a curva de atenuação:
    """)

    col2.markdown(r'''
    $$
            I(x)=I_{0}e^{-\alpha x}
    $$''', width="stretch")

    col2.markdown("em que o **coeficiente de atenuação ($\\alpha$)** (em dB/m) descreve o decaimento do sinal em função da distância percorrida. Esta sequência de eventos é fundamental para a compreensão dos próximos ensaios.")

    col2.markdown("##### Cronometragem do tempo de propagação da onda de tensão (ToF)")
    
    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col3.image(
        "imagens/cronometragem.png", 
        caption="Cronometragem do tempo de propagação da onda de tensão entre acelerômetros.",
        width=350
    )

    col2.write("""
        Neste ensaio (Time of Flight - ToF), os sensores (acelerômetros ou transdutores) são tipicamente posicionados nas faces laterais das extremidades da barra. O impacto ocorre na seção transversal.
        
        Um acelerômetro capta o sinal da onda de compressão e inicia a contagem do cronômetro. Ao alcançar a extremidade oposta, o pulso é detectado pelo segundo acelerômetro, que pausa a contagem.

        Com o tempo ($\\Delta t$) e o comprimento da barra ($L$), a velocidade de propagação ($V$) é determinada por cinemática do movimento retilíneo e uniforme:
    """)

    col2.markdown(r'''
    $$
            V=\dfrac{L}{\Delta t}
    $$''', width="stretch")

    col2.markdown("##### Método do pulso-eco")

    col2.write("""
        No método de pulso-eco, um sensor (geralmente um transdutor) é fixado na extremidade impactada da barra. A onda de tensão atinge o sensor, e sua amplitude é medida em função do tempo no osciloscópio.

        A distância temporal entre dois pulsos no osciloscópio representa o tempo que o pulso levou para percorrer o comprimento da barra duas vezes (ida e volta). Portanto, a velocidade de propagação é:
    """)

    col2.markdown(r'''
    $$
            V=\dfrac{2L}{\Delta t}
    $$''', width="stretch")

    col1, col2, col3 = st.columns([.25, 3, 1.5])

    col2.write("""
        Ao analisar a velocidade e a aceleração das partículas em função do tempo, nota-se que a velocidade decai exponencialmente, enquanto a aceleração se mantém constante até que a propagação seja atenuada.

        Os gráficos de sinal apresentam comportamentos distintos: as partículas, sujeitas à vibração longitudinal, oscilam em torno de um ponto de equilíbrio (metade do tempo no sentido de propagação, metade no sentido oposto). Já a aceleração das partículas concentra-se no primeiro quadrante do gráfico, indicando que a aceleração é maior ou igual a zero, sempre concordando com o sentido da onda de compressão.
    """)

    col3.image(
        "imagens/pulso-eco.png", 
        caption="Arranjo do aparato para ensaio de pulso-eco.",
        width=350
    )

    col1, col2, col3 = st.columns([.25, 3, 1.5])
    
    col2.markdown("##### *Pitch and catch*")

    col3.image(
        "imagens/pitch-and-catch.png", 
        caption="Arranjo do aparato para ensaio de pitch and catch.",
        width=350
    )

    # REVISÃO: Correção da frase incompleta
    col2.write("""
        No método *pitch and catch*, o aparato utiliza a associação de dois transdutores — um de emissão e outro de recepção do sinal acústico — conectados a um osciloscópio.
        
        Diferente dos métodos de impacto, a emissão se origina de um sinal elétrico enviado pelo osciloscópio, que é transmitido ao transdutor emissor e convertido em onda acústica. **Esta onda se propaga pelo espécime e é captada pelo transdutor receptor, que a converte de volta em sinal elétrico para análise no osciloscópio.**
    """)
    
    col2.markdown("##### Posicionamento dos acelerômetros")

    # REVISÃO: Melhoria na clareza e fluidez do parágrafo
    col2.write("""
        Durante os ensaios em barras de madeira, deve-se considerar o posicionamento dos acelerômetros na peça, pois a **intensidade e a qualidade do sinal dependem diretamente do local** em que são fixados e de quais faces são utilizados em relação à fonte de impacto. O arranjo dos sensores influencia o tipo de onda captada (longitudinal, flexural ou torsional) e a precisão da medição.
    """) 

    col2.info("""
        **Referências Bibliográficas**
              
        * **FALCÃO BAUER**, **L. A.** Materiais de Construção. 6. ed. Rio de Janeiro: LTC – Livros Técnicos e Científicos, 2019.
              
        * **17TH INTERNATIONAL NONDESTRUCTIVE TESTING AND EVALUATION OF WOOD SYMPOSIUM**. Proceedings. Vol. 2. [S.l.: s.n.], 2011. ISBN 978-963-98838-3-3.
        
        * **ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS**. NBR 7190:2022 — Projeto de estruturas de madeira. Rio de Janeiro: ABNT, 2022.      
    """)

if __name__ == "__main__":
    materiais_nao_metalicos_page()