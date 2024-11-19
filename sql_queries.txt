-- 1. Qual a quantidade total de voos em 2015?

SELECT COUNT(*) AS TotalVoos
FROM dbo.flights
WHERE YEAR = 2015;
-- O total de vôos em 2015 foi de 5819079


-- 2. Como o volume geral de voos varia por mês? Por dia da semana?

SELECT MONTH, COUNT(*) AS TOTAL_VOOS_MES
FROM flights
GROUP BY MONTH
ORDER BY MONTH;
          -- Janeiro -> 469968
          -- Fevereiro -> 429191
          -- Março -> 504312
          -- Abril -> 485151
          -- Maio -> 496993
          -- Junho -> 503897
          -- Julho -> 520718
          -- Agosto -> 510536
          -- Setembro -> 464946
          -- Outubro -> 486165
          -- Novembro -> 467972
          -- Dezembro -> 479230

SELECT DAY_OF_WEEK, COUNT(*) AS TOTAL_VOOS_SEMANA
FROM flights
GROUP BY DAY_OF_WEEK
ORDER BY DAY_OF_WEEK;
          -- Domingo -> 865543
          -- Segunda -> 844600
          -- Terça -> 855897
          -- Quarta -> 872521
          -- Quinta -> 862209
          -- Sexta -> 700545
          -- Sábado -> 817764


-- 3. Qual a porcentagem de voos que tiveram atraso na partida em 2015? Entre esses voos, qual foi o tempo médio de atraso, em minutos?

SELECT 
    COUNT(*) AS TOTAL_VOOS,
    SUM(CASE WHEN DEPARTURE_DELAY > 0 THEN 1 ELSE 0 END) AS TOTAL_ATRASOS,
    (SUM(CASE WHEN DEPARTURE_DELAY > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS TOTAL_ATRASOS_PORCENTAGEM,
    AVG(CASE WHEN DEPARTURE_DELAY > 0 THEN DEPARTURE_DELAY END) AS MEDIA_ATRASO
FROM
    flights
WHERE 
    YEAR = 2015;
            -- O TOTAL DE VOOS EM 2015 FORAM DE 5819079
            -- O TOTAL DE VOOS EM ATRASO É DE 2125618
            -- O TOTAL DE VOOS SEM ATRASO É DE 3693461
            -- A MÉDIA DE ATRASO É DE 32,67 MINUTOS
            -- A PORCENTAGEM DE VOOS COM ATRASO É DE 36,53%


-- 4. Como a % de voos atrasados ​​varia ao longo do ano? E quanto aos voos que saem de Boston (BOS) especificamente? 

-- Variação dos voos geral
SELECT 
    MONTH,
    COUNT(*) AS Total_Flights,
    SUM(CASE WHEN DEPARTURE_DELAY > 0 THEN 1 ELSE 0 END) AS Delayed_Flights,
    (SUM(CASE WHEN DEPARTURE_DELAY > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS Percentage_Delayed
FROM 
    flights
WHERE 
    YEAR = 2015
GROUP BY 
    MONTH
ORDER BY 
    MONTH;
       -- Month Total_Flight  Delayed_Flights  Percentage_Delayded
          -- 1	  469968	        176627	       37.582771592959
          -- 2	  429191	        173442	       40.411378616979
          -- 3	  504312	        193817	       38.431962753216
          -- 4	  485151	        167314	       34.486994770700
          -- 5	  496993	        178856	       35.987629604441
          -- 6  	503897	        215381         42.743060585794
          -- 7	  520718	        209619	       40.255762235989
          -- 8  	510536	        190840         37.380321857812
          -- 9	  464946	        132591	       28.517505258675
          -- 10	  486165	        145102	       29.846245616200
          -- 11  	467972	        152690	       32.628020479857
          -- 12	  479230        	189339	       39.509004027293


-- Variação dos voos em atraso de Boston
SELECT 
    MONTH,
    COUNT(*) AS Total_Flights,
    SUM(CASE WHEN DEPARTURE_DELAY > 0 THEN 1 ELSE 0 END) AS Delayed_Flights,
    (SUM(CASE WHEN DEPARTURE_DELAY > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS Percentage_Delayed
FROM 
    flights
WHERE 
    YEAR = 2015 AND ORIGIN_AIRPORT = 'BOS'
GROUP BY 
    MONTH
ORDER BY 
    MONTH;
       -- Month Total_Flight  Delayed_Flights  Percentage_Delayded
          -- 1	  8837	          3016	          34.129229376485
          -- 2	  8380	          4076	          48.639618138424
          -- 3	  9971	          3732	          37.428542774044
          -- 4	  10000	          3329	          33.290000000000
          -- 5	  10241	          3228	          31.520359339908
          -- 6	  10544	          3942	          37.386191198786
          -- 7	  10837	          4295	          39.632739688105
          -- 8	  10727	          4279	          39.889997203318
          -- 9	  9726	          2905	          29.868393995476
          -- 11	  9464	          2729	          28.835587489433
          -- 12	  9120	          3562	          39.057017543859


-- 5. Quantos voos foram cancelados em 2015? Qual a % de cancelamentos devido ao clima? Qual a % devido à companhia aérea/transportadora?

SELECT 
    COUNT(*) AS Total_Flights,
    SUM(CANCELLED) AS Total_Cancelled,
    (SUM(CANCELLED) * 100.0 / COUNT(*)) AS Cancellation_Rate,
    (SUM(CASE WHEN CANCELLATION_REASON = 'B' THEN 1 ELSE 0 END) * 100.0 / SUM(CANCELLED)) AS Weather_Cancellation_Percentage,
    (SUM(CASE WHEN CANCELLATION_REASON = 'A' THEN 1 ELSE 0 END) * 100.0 / SUM(CANCELLED)) AS Carrier_Cancellation_Percentage
FROM 
    flights
WHERE 
    YEAR = 2015;
          -- O TOTAL DE VOOS CANCELADOS EM 2015 FOI DE 89884 
          -- QUE EQUIVALE A 1.54%
          -- 54,35% FORAM POR CAUSA DO CLIMA
          -- 28,11% FORAM POR CAUSA DA COMPANHIA AÉRA/TRANSPORTADORA


-- 6. Quais companhias aéreas parecem ser mais e menos confiáveis ​​em termos de partida pontual?

SELECT 
    AIRLINE,
    COUNT(*) AS Total_Flights,
    SUM(CASE WHEN DEPARTURE_DELAY <= 0 THEN 1 ELSE 0 END) AS On_Time_Flights,
    (SUM(CASE WHEN DEPARTURE_DELAY <= 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS On_Time_Percentage
FROM 
    flights
WHERE 
    YEAR = 2015
GROUP BY 
    AIRLINE
ORDER BY 
    On_Time_Percentage DESC;

          -- A companhia mais confiável é a AS (Alaska Airlines Inc.) com 74.75% dos vôos dentro do horário
          -- A companhia MENOS confiável é a UA (United Air Lines Inc.) com apenas 50% dos vôos dentro do horário
