-- Unificação do histórico com as previsões LSTM para o dashboard
SELECT 
  id_resort,
  CAST(data AS DATE) AS data_unificada,
  quartos_ocupados,
  adr,
  NULL AS previsao_quartos_ocupados
FROM `amarante-hoteis.amarante_gold.ts_demanda_diaria`

UNION ALL

SELECT 
  id_resort,
  CAST(data AS DATE) AS data_unificada,
  NULL AS quartos_ocupados,
  NULL AS adr,
  previsao_quartos_ocupados
FROM `amarante-hoteis.amarante_gold.pred_demanda_futura`
