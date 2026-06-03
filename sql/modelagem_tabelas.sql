CREATE OR REPLACE TABLE `seu-projecto-gcp.amarante_gold.ts_demanda_diaria`
AS
WITH
  dados_reserva_tratados AS (
    -- Tratando datas e filtrando dados válidos
    SELECT
      id_resort,
      DATE(data_checkin) AS data_checkin,
      DATE(data_checkout) AS data_checkout,
      valor_total,
      status,
      -- Calcula o tempo de permanência
      DATE_DIFF(DATE(data_checkout), DATE(data_checkin), DAY) AS num_diarias
    FROM `seu-projeto-gcp.amarante_raw.raw_reservas`
    WHERE
      status
      != 'CANCELADA'  -- Filtrando as canceladas para métricas de ocupação
  ),
  
-- Criando as lag features com as funções janela
SELECT
  id_resort,
  data,
  quartos_ocupados,
  receita_diaria,
  adr,
  cancelamentos,
  indice_busca_trends,
  precipitacao_chuva,
  -- lags de ocupação (7, 14, 30 e 45 dias para trás)
  COALESCE(
    LAG(quartos_ocupados, 7) OVER (PARTITION BY id_resort ORDER BY data), 0)
    AS lag_ocupacao_7,
  COALESCE(
    LAG(quartos_ocupados, 14) OVER (PARTITION BY id_resort ORDER BY data), 0)
    AS lag_ocupacao_14,
  COALESCE(
    LAG(quartos_ocupados, 30) OVER (PARTITION BY id_resort ORDER BY data), 0)
    AS lag_ocupacao_30,
  COALESCE(
    LAG(quartos_ocupados, 45) OVER (PARTITION BY id_resort ORDER BY data), 0)
    AS lag_ocupacao_45,

  -- variáveis cíclicas do dia da semana(0 a 6)
  ROUND(SIN(2 * ACOS(-1) * EXTRACT(DAYOFWEEK FROM data) / 7), 6)
    AS dia_semana_sin,
  ROUND(COS(2 * ACOS(-1) * EXTRACT(DAYOFWEEK FROM data) / 7), 6)
    AS dia_semana_cos,

  -- variáveis cíclicas do dia do ano (1 a 365)
  ROUND(SIN(2 * ACOS(-1) * EXTRACT(DAYOFYEAR FROM data) / 365), 6)
    AS dia_ano_sin,
  ROUND(COS(2 * ACOS(-1) * EXTRACT(DAYOFYEAR FROM data) / 365), 6)
    AS dia_ano_cos,

  -- Mapeamento dinâmico de feriados nacionais (flag)
  CASE
    -- feriados fixos nacionais
    WHEN EXTRACT(MONTH FROM data) = 1 AND EXTRACT(DAY FROM data) = 1
      THEN 1  -- Ano Novo
    WHEN EXTRACT(MONTH FROM data) = 4 AND EXTRACT(DAY FROM data) = 21
      THEN 1  -- Tiradentes
    WHEN EXTRACT(MONTH FROM data) = 5 AND EXTRACT(DAY FROM data) = 1
      THEN 1  -- Dia do Trabalho
    WHEN EXTRACT(MONTH FROM data) = 9 AND EXTRACT(DAY FROM data) = 7
      THEN 1  -- Independência
    WHEN EXTRACT(MONTH FROM data) = 10 AND EXTRACT(DAY FROM data) = 12
      THEN 1  -- Nossa Sra Aparecida
    WHEN EXTRACT(MONTH FROM data) = 11 AND EXTRACT(DAY FROM data) = 2
      THEN 1  -- Finados
    WHEN EXTRACT(MONTH FROM data) = 11 AND EXTRACT(DAY FROM data) = 15
      THEN 1  -- Proclamação da república
    WHEN EXTRACT(MONTH FROM data) = 12 AND EXTRACT(DAY FROM data) = 25
      THEN 1  -- Natal
    -- Simulação de feriados móveis para as datas do mock data (maio de 2026, ex: Corpus Christi)
    WHEN data IN ('2026-05-14', '2026-05-24') THEN 1
    ELSE 0
    END
    AS flag_feriado
FROM consolidado_base
ORDER BY id_resort, data;
