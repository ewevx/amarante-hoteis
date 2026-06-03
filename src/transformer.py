import numpy as np
import torch
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src.interfaces import DataTransformerInterface

class AmaranteDataTransformer(DataTransformerInterface):
    def __init__(self, features: list, target_index: int = 0):
        self.features = features
        self.target_index = target_index
        self.scaler = MinMaxScaler()

    def fit_transform(self, df: pd.DataFrame) -> np.ndarray:
        data_filtered = df[self.features].values
        return self.scaler.fit_transform(data_filtered)

    def create_sequences(self, data: np.ndarray, window_size: int):
        X, y = [], []
        for i in range(len(data) - window_size):
            X.append(data[i:(i + window_size)])
            y.append(data[i + window_size, self.target_index])
        return torch.tensor(np.array(X), dtype=torch.float32), torch.tensor(np.array(y), dtype=torch.float32).unsqueeze(1)
