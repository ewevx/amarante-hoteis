from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
import torch

class DataLoaderInterface(ABC):
    @abstractmethod
    def load_data(self) -> pd.DataFrame:
        pass

class DataTransformerInterface(ABC):
    @abstractmethod
    def fit_transform(self, df: pd.DataFrame) -> np.ndarray:
        pass
    @abstractmethod
    def create_sequences(self, data: np.ndarray, window_size: int):
        pass

class PredictorInterface(ABC):
    @abstractmethod
    def predict_future(self, model: torch.nn.Module, initial_sequence: torch.Tensor, steps: int) -> list:
        pass

class DataExporterInterface(ABC):
    @abstractmethod
    def export(self, df_predictions: pd.DataFrame):
        pass
