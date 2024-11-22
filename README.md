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
- Horários programados reais de partida e chegada.
- Informações sobre atrasos e cancelamentos.
- Detalhes sobre companhias aéreas.
Os dados foram pré-processados e armazenados em um banco de dados relacional com múltiplas tabelas.

### Tecnologias Utilizadas
- SQL: Para consultas e manipulação dos dados.
- Power Bi: Para criação de gráficos.
- Python: Para visualizações e análises adicionais.
- Jupyter Notebook: Para documentar e apresentar as análises.
- GitHub: Para versionamento e compartilhamento do projeto.

### Estrutura do Projeto
- sql_queries: Contém todas as consultas SQL criadas.
- notebooks/: Análises documentadas em formato de notebook interativo.
- images/: Gráficos e visualizações geradas.
- data/: Scripts para carregar os dados ou exemplos de dados brutos.
- README.md: Descrição geral do projeto.
- business_quetins: Perguntas respondidas

### Resultados e Descobertas
1. Como o volume geral de voos varia por mês? Por dia da semana?
- Por mês: Existe uma variação sazonal, com maior volume de voos nos meses de verão (junho-agosto)
<div align="center"
  <p>Este gráfico mostra o volume geral de voos por mês.</p>
  <img src="https://github.com/maxwellsantos94/Airline-Data-Analysis/blob/main/images/volume_geral_por_mes_colunas.png?raw=true">
</div>

- Por dia da semana: Os dias entre segunda e quinta (1-5) têm mais voos que as sextas e sábados (6 e 7)
<div align="center"
  <p>Este gráfico mostra o volume geral de voos por semana.</p>
  <img src="https://github.com/maxwellsantos94/Airline-Data-Analysis/blob/main/images/volume_geral_por_semana_colunas.png?raw=true">
</div>

2. Qual a porcentagem de voos que tiveram atraso na partida em 2015? Entre esses voos, qual foi o tempo médio de atraso, em minutos?
<div align="center">
  A análise dos dados de voo
  <p>Este gráfico mostra a porcentagem geral de voos atrasados e no horário correto.</p>
  <img src="https://github.com/maxwellsantos94/Airline-Data-Analysis/blob/main/images/atrasos_horario_pizza.png?raw=true">
  <p>Tempo Médio de Atraso (minutos)  32.67</p>
</div>

3. Como a % de voos atrasados ​​varia ao longo do ano? E quanto aos voos que saem de Boston (BOS) especificamente?
- Para analisar como a porcentagem de voos atrasados ​​varia ao longo do ano e especificamente para voos partindo de Boston (BOS), vou agrupar os dados por mês e calcular a porcentagem de voos atrasados ​​para cada mês, tanto no geral quanto para BOS.

4. Quantos voos foram cancelados em 2015? Qual a % de cancelamentos devido ao clima? Qual a % devido à companhia aérea/transportadora?
- Os motivos mais comuns para cancelamentos incluem condições climáticas e problemas operacionais.


5. Quais companhias aéreas parecem ser mais e menos confiáveis ​​em termos de partida pontual?
- Algumas companhias aéreas apresentam melhores índices de pontualidade do que outras, destacando a importância de práticas operacionais eficientes.


### Dataset link:
- O dataset foi obtido no Kaggle
- Link: https://www.kaggle.com/datasets/usdot/flight-delays
