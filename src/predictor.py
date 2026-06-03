import torch
import torch.nn as nn
from src.interfaces import PredictorInterface

class AmaranteDemandPredictor(PredictorInterface):
    def __init__(self, scaler, window_size: int, device: torch.device):
        self.scaler = scaler
        self.window_size = window_size
        self.device = device

    def predict_future(self, model: nn.Module, initial_sequence: torch.Tensor, steps: int) -> list:
        model.eval()
        predictions = []
        current_seq = initial_sequence.clone().to(self.device)

        with torch.no_grad():
            for _ in range(steps):
                pred = model(current_seq)
                pred_value = pred.item()
                predictions.append(pred_value)

                next_step = current_seq[:, 1:, :].clone()
                new_features = current_seq[:, -1, :].clone()
                new_features[0, 0] = pred_value

                current_seq = torch.cat((next_step, new_features.unsqueeze(1)), dim=1)

        return predictions
