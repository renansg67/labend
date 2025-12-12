import streamlit as st
import pandas as pd

st.title("Links Auxiliares do LabEND")

# Definição dos dados com colunas renomeadas e categorias revisadas
data = {
    "Ferramenta": [ # Renomeado de 'Descrição'
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
        "Bases teóricas - Propagação de ondas acústicas em sólidos ortotrópicos",
        "Imagens vetorizadas"
    ],
    "Tipo de Input/Output": [ # Renomeado de 'Tipo de Arquivos'
        "N/A", # Alterado de "" para N/A
        ":gray-badge[CSV]",
        ":gray-badge[CSV]",
        ":gray-badge[CSV]",
        ":green-badge[XLSX]",
        "N/A", # Alterado de "" para N/A
        ":gray-badge[CSV]",
        ":blue-badge[PY] / :gray-badge[CSV]", # Adicionado CSV para input
        ":blue-badge[PY] / :gray-badge[CSV]", # Adicionado CSV para input
        ":violet-badge[GIT]",
        ":yellow-badge[TEX]",
        ":yellow-badge[TEX]",
        ":red-badge[IPE]/:orange-badge[PDF]"
    ],
    "Objetivo Principal": [ # Renomeado de 'Função'
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
        "Documento apresentando as bases teóricas para propagação de ondas ultrassônicas em espécimes poliédricas",
        "Múltiplas imagens relacionadas aos tópicos de pesquisa do LabEND"
    ],
    "Categoria": [ # Rótulos revisados para maior clareza
        ":violet-badge[:material/assignment: Logística / Formulários]",
        ":red-badge[:material/timeline: Processamento de Dados]",
        ":red-badge[:material/timeline: Processamento de Dados]",
        ":red-badge[:material/timeline: Processamento de Dados]",
        ":red-badge[:material/timeline: Processamento de Dados]",
        ":red-badge[:material/timeline: Processamento de Dados]",
        ":red-badge[:material/timeline: Processamento de Dados]",
        ":yellow-badge[:material/waves: END - Ultrassom / Cálculo]",
        ":yellow-badge[:material/waves: END - Ultrassom / Cálculo]",
        ":green-badge[:material/book: Guia Rápido / Referência]",
        ":green-badge[:material/book: Guia Rápido / Referência]",
        ":green-badge[:material/book: Guia Rápido / Referência]",
        ":green-badge[:material/book: Guia Rápido / Referência]"
    ],
    "Código-fonte (GitHub)": [ # Renomeado de 'Repositório'
        "N/A", # Alterado de "" para N/A
        "[`/downsampling`](https://github.com/renansg67/downsampling)",
        "[`/concat-csv`](https://github.com/renansg67/processador-csv)",
        "[`/processador-csv`](https://github.com/renansg67/processador-csv)",
        "[`/processador-xlsx`](https://github.com/renansg67/processador-xlsx)",
        "[`/csv-file-lister`](https://github.com/renansg67/csv-file-lister)",
        "[`/hunter`](https://github.com/renansg67/hunter)",
        "[`/sensivity`](https://github.com/renansg67/matriz-de-rigidez)",
        "[`/matriz-de-rigidez`](https://github.com/renansg67/matriz-de-rigidez)",
        "[`/git-guia`](https://github.com/renansg67/git-guia)",
        "N/A", # Alterado de "" para N/A
        "N/A",  # Alterado de "" para N/A
        "[`vetores`](https://github.com/renansg67/vetores)"
    ],
    "Acesso (App/Doc)": [ # Renomeado de 'Link'
        "[`forms`](https://forms.gle/bZvLQF5eLDx3da1i8)",
        "[`/streamlit/downsampling`](https://downsampling-csv.streamlit.app/)",
        "[`/streamlit/concat-csv`](https://concat-csv.streamlit.app/)",
        "[`/streamlit/processador-csv`](https://processador-csv.streamlit.app/)",
        "[`/streamlit/processador-xlsx`](https://processador-xlsx.streamlit.app/)",
        "N/A", # Alterado de "" para N/A
        "[`/streamlit/hunter-csv`](https://hunter-csv.streamlit.app/)",
        "N/A", # Alterado de "" para N/A
        "N/A", # Alterado de "" para N/A
        "N/A", # Alterado de "" para N/A
        "[`Overleaf Doc`](https://www.overleaf.com/9556632885xxjbjbjcswmr#0405e3)", # Link text alterado
        "[`Overleaf Doc`](https://www.overleaf.com/read/jmcwjfypgpnk#4302fd)",  # Link text alterado
        "N/A"
    ]
}

# st.dataframe() é mais moderno, mas st.table() funciona bem com Markdown/Badges.
# Mantenho st.table() conforme o original, mas com uma sugestão de migração para o dataframe abaixo.
st.table(data)

# Sugestão alternativa: usar st.dataframe para permitir filtros e ordenação, 
# embora exija conversão prévia dos dados para o tipo DataFrame.
# df = pd.DataFrame(data)
# st.dataframe(df, hide_index=True)