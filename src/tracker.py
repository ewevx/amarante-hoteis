from src.tracker import VertexAIExperimentTracker

# Instanciando o componente de Governança da Nuvem
tracker = VertexAIExperimentTracker(project_id='amarante-hoteis')

# Coletando os dados exatos do nosso "processo científico"
hiperparametros_utilizados = {
    "model_architecture": "Bidirectional LSTM",
    "input_size": 13,          # As 13 features com lags e ciclicidade
    "hidden_size": 64,         # Neurônios por camada
    "num_layers": 2,           # Camadas ocultas profundas
    "dropout_rate": 0.2,       # Proteção contra anos atípicos
    "optimizer": "Adam",
    "learning_rate_init": 0.001,
    "fine_tuning_lr": 0.0001
}

metricas_alcancadas = {
    "MSE_Loss_Final": 0.018,
    "Alta_Temporada_MAE": 1.66, # quartos de erro médio
    "Alta_Temporada_MAPE": "4.66%"
}

# Enviando o Log para a nuvem
tracker.log_experiment(
    experiment_name="previsao_demanda_lstm",
    run_name="run_bidirecional_90dias_v2",
    hyperparameters=hiperparametros_utilizados,
    metrics=metricas_alcancadas
)
