import streamlit as st

st.title("Links")

data = {
    "Descrição": [
        "Formulário de empréstimos",
        "Downsampling de arquivos",
        "Concatenar arquivos",
        "Renomear e reordenar colunas",
        "Exportação de abas do arquivo",
        "Listar arquivos locais",
        "Caçador de linearidade",
        "Análise de sensibilidade",
        "Calculadora de propriedades mecânicas",
        "Comandos do Git",
        "Ensaio de compressão paralela às fibras",
        "Bases teóricas - Propagação de ondas acústicas em sólidos ortotrópicos"
    ],
    "Tipo de Arquivos": [
        "",
        ":gray-badge[CSV]",
        ":gray-badge[CSV]",
        ":gray-badge[CSV]",
        ":green-badge[XLSX]",
        "",
        ":gray-badge[CSV]",
        ":blue-badge[PY]",
        ":blue-badge[PY]",
        ":violet-badge[GIT]",
        ":yellow-badge[TEX]",
        ":yellow-badge[TEX]",
    ],
    "Função": [
        "Formalizar empréstimos de equipamentos e materiais do LabEND",
        "Reduzir densidade de pontos de dados amostrais visando otimizar consumo de memória e renderização de gráficos",
        "Compilar múltiplos arquivos em somente um",
        "Renomear, reordenar e padronizar exportação de arquivos com cabeçalho bem definido",
        "Carregar múltiplos arquivos XLSX, categorizar conforme a estrutura do intervalo definido e exportação de ZIP dos agrupamentos",
        "Listar nomes de arquivos locais de diferentes diretórios",
        "Obter múltiplos parâmetros de regressão linear a partir de um conjunto de dados",
        "Analisar impacto da diferença de tempos recíprocos nas propriedades mecânicas no ensaio de propagação de ondas acústicas em materiais ortotrópicos",
        "Obter propriedades mecânicas de materiais ortotrópicos a partir do ensaio de propagação de ondas ultrassônicas",
        "Guia rápido de comandos básicos do Git",
        "Documento com instruções para o ensaio de compressão",
        "Documento apresentando as bases teóricas para propagação de ondas ultrassônicas em espécimes poliédricas"
    ],
    "Categoria": [
        ":violet-badge[:material/assignment: Formulários Google]",
        ":red-badge[:material/timeline: Tratamento de dados] :green-badge[:material/circle: Otimização]",
        ":red-badge[:material/timeline: Tratamento de dados] :green-badge[:material/circle: Otimização]",
        ":red-badge[:material/timeline: Tratamento de dados] :green-badge[:material/circle: Otimização]",
        ":red-badge[:material/timeline: Tratamento de dados] :green-badge[:material/circle: Otimização]",
        ":red-badge[:material/timeline: Tratamento de dados] :green-badge[:material/circle: Otimização]",
        ":red-badge[:material/timeline: Tratamento de dados] :green-badge[:material/circle: Otimização]",
        ":yellow-badge[:material/waves: Ultrassom] :orange-badge[:material/apps: Matriz de Rigidez]",
        ":yellow-badge[:material/waves: Ultrassom] :orange-badge[:material/apps: Matriz de Rigidez]",
        ":green-badge[:material/assignment: Documentação]",
        ":green-badge[:material/assignment: Documentação]",
        ":green-badge[:material/assignment: Documentação]",
    ],
    "Repositório": [
        "",
        "[`/downsampling`](https://github.com/renansg67/downsampling)",
        "[`/concat-csv`](https://github.com/renansg67/processador-csv)",
        "[`/processador-csv`](https://github.com/renansg67/processador-csv)",
        "[`/processador-xlsx`](https://github.com/renansg67/processador-xlsx)",
        "[`/csv-file-lister`](https://github.com/renansg67/csv-file-lister)",
        "[`/hunter`](https://github.com/renansg67/hunter)",
        "[`/sensivity`](https://github.com/renansg67/matriz-de-rigidez)",
        "[`/matriz-de-rigidez`](https://github.com/renansg67/matriz-de-rigidez)",
        "[`/git-guia`](https://github.com/renansg67/git-guia)",
        "",
        ""
    ],
    "Link": [
        "[`forms`](https://forms.gle/bZvLQF5eLDx3da1i8)",
        "[`/streamlit/downsampling`](https://downsampling-csv.streamlit.app/)",
        "[`/streamlit/concat-csv`](https://concat-csv.streamlit.app/)",
        "[`/streamlit/processador-csv`](https://processador-csv.streamlit.app/)",
        "[`/streamlit/processador-xlsx`](https://processador-xlsx.streamlit.app/)",
        "",
        "[`/streamlit/hunter-csv`](https://hunter-csv.streamlit.app/)",
        "",
        "",
        "",
        "[`/overleaf/modulo-compressao`](https://www.overleaf.com/9556632885xxjbjbjcswmr#0405e3)",
        "[`/overleaf/bases-teoricas`](https://www.overleaf.com/read/jmcwjfypgpnk#4302fd)",
    ]
}

st.table(data, border="horizontal")