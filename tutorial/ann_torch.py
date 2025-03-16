import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset

# 1. Veri Hazırlığı
# Örnek veri seti (X: girişler, y: hedefler)
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# TensorDataset ve DataLoader kullanarak veri yükleme
dataset = TensorDataset(X, y)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# 2. Model Tanımlama
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(1, 10)
        self.fc2 = nn.Linear(10, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = SimpleNN()

# 3. Kayıp Fonksiyonu ve Optimizasyon
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 4. Model Eğitimi
num_epochs = 100
for epoch in range(num_epochs):
    for inputs, targets in dataloader:
        # İleri yayılım
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        
        # Geri yayılım ve optimizasyon
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# 5. Model Değerlendirme
with torch.no_grad():
    test_input = torch.tensor([[5.0]])
    test_output = model(test_input)
    print(f'Test Input: 5.0, Predicted Output: {test_output.item():.4f}')