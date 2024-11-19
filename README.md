# Airline Flight Analysis 2015
### Descrição do Projeto
Este projeto realiza uma análise detalhada dos voos nos Estados Unidos durante o ano de 2015, utilizando um conjunto de dados contendo informações sobre voos, aeroportos, companhias aéreas, atrasos e cancelamentos. O objetivo principal é explorar padrões no tráfego aéreo, identificar fatores que influenciam atrasos e cancelamentos, e determinar quais companhias aéreas são mais confiáveis.

As análises são realizadas em SQL, com visualizações geradas para interpretar os resultados de forma clara e acessível. Este repositório pode ser útil para quem está aprendendo análise de dados ou deseja entender o impacto de fatores externos no setor de aviação.

### Objetivos do Projeto
- Entender como o volume de voos varia ao longo do ano e por dia da semana.
- Analisar atrasos na partida: frequência, causas e duração média.
- Explorar como atrasos variam geograficamente, com foco no aeroporto de Boston (BOS).
- Examinar padrões de cancelamento, identificando os principais motivos.
- Avaliar a confiabilidade de companhias aéreas em relação à pontualidade.

### Conjunto de Dados
Os dados utilizados neste projeto incluem informações detalhadas de voos, tais como:
- Aeroportos de origem e destino.
- Horários programados e reais de partida e chegada.
- Informações sobre atrasos e cancelamentos.
- Detalhes sobre companhias aéreas.
Os dados foram pré-processados e armazenados em um banco de dados relacional com múltiplas tabelas.

### Tecnologias Utilizadas
- SQL: Para consultas e manipulação dos dados.
- Power Bi: Para criação de gráficos.
- Python: Para visualizações e análises adicionais.
- Jupyter Notebook: Para documentar e apresentar as análises.
- Matplotlib/Seaborn/Plotly: Para criar gráficos e visualizações.
- GitHub: Para versionamento e compartilhamento do projeto.

### Estrutura do Projeto
- sql_queries/: Contém todas as consultas SQL criadas.
- notebooks/: Análises documentadas em formato de notebook interativo.
- visualizations/: Gráficos e visualizações geradas.
- data/: Scripts para carregar os dados ou exemplos de dados brutos.
- README.md: Descrição geral do projeto.

### Resultados e Descobertas
- Identificamos padrões sazonais e semanais no volume de voos.
- Atrasos são mais frequentes no verão e em certos dias da semana.
- Os motivos mais comuns para cancelamentos incluem condições climáticas e problemas operacionais.
- Algumas companhias aéreas apresentam melhores índices de pontualidade do que outras, destacando a importância de práticas operacionais eficientes.

### Dataset link:
- O dataset foi obtido no Kaggle
- Link: https://www.kaggle.com/datasets/usdot/flight-delays
