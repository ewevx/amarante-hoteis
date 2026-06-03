import torch
import torch.nn as nn

class ModelTrainer:
    def __init__(self, model: nn.Module, criterion, optimizer, device: torch.device):
        self.model = model.to(device)
        self.criterion = criterion
        self.optimizer = optimizer
        self.device = device

    def fit(self, X_train: torch.Tensor, y_train: torch.Tensor, epochs: int):
        X_train, y_train = X_train.to(self.device), y_train.to(self.device)
        print(f"Iniciando treinamento na: {self.device}")
        for epoch in range(epochs):
            self.model.train()
            self.optimizer.zero_grad()

            outputs = self.model(X_train)
            loss = self.criterion(outputs, y_train)

            loss.backward()
            self.optimizer.step()

            if (epoch + 1) % 10 == 0:
                print(f"Época [{epoch+1}/{epochs}], MSE Loss: {loss.item():.6f}")

    def save_model_weights(self, path: str):
        torch.save(self.model.state_dict(), path)
        print(f"Pesos salvos em: {path}")
