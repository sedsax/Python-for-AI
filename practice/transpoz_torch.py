import torch

# 1. Veri seti oluşturma (örnek giriş ve hedef değerler)
# Giriş verileri (features): 3 özellikli 5 örnek
X = torch.tensor([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0],
                  [7.0, 8.0, 9.0],
                  [10.0, 11.0, 12.0],
                  [13.0, 14.0, 15.0]])

# Hedef değerler (labels): 5 örnek için tek bir çıktı
y = torch.tensor([[10.0], [20.0], [30.0], [40.0], [50.0]])

# 2. Ağırlık matrisi ve bias (rastgele başlatılır)
# Ağırlık matrisi: 3 giriş özelliği -> 1 çıktı
weights = torch.randn((3, 1), requires_grad=True)  # Boyut: (3, 1)
bias = torch.randn((1,), requires_grad=True)       # Boyut: (1,)

# 3. Lineer regresyon modeli
def linear_regression(X, weights, bias):
    """
    Lineer regresyon modeli: y = X * W + b
    """
    # Transpoz işlemi burada gerekmez çünkü PyTorch matris çarpımını otomatik olarak yapar.
    # Ancak, giriş verilerinin transpozu gerekirse şu şekilde yapılabilir:
    # X_transposed = X.T
    return torch.mm(X, weights) + bias

# 4. Kayıp fonksiyonu (Mean Squared Error - MSE)
def mse_loss(y_pred, y_true):
    """
    Ortalama kare hatası (MSE) kayıp fonksiyonu
    """
    return torch.mean((y_pred - y_true) ** 2)

# 5. Eğitim döngüsü
learning_rate = 0.001
epochs = 1000

for epoch in range(epochs):
    # İleri yayılım (forward propagation)
    y_pred = linear_regression(X, weights, bias)

    # Kayıp hesaplama
    loss = mse_loss(y_pred, y)

    # Geri yayılım (backpropagation)
    loss.backward()

    # Ağırlıkları ve bias'ı güncelleme
    with torch.no_grad():
        weights -= learning_rate * weights.grad
        bias -= learning_rate * bias.grad

        # Gradients sıfırlanır
        weights.grad.zero_()
        bias.grad.zero_()

    # Her 100 epoch'ta kaybı yazdır
    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss.item()}")

# 6. Sonuçları yazdırma
print("\nEğitim tamamlandı!")
print(f"Ağırlıklar (weights):\n{weights}")
print(f"Bias (bias):\n{bias}")

# Yeni bir veri ile tahmin yapma
new_data = torch.tensor([[16.0, 17.0, 18.0]])  # Yeni giriş verisi
prediction = linear_regression(new_data, weights, bias)
print(f"Yeni veri için tahmin: {prediction.item()}")

"""
output

Epoch 100/1000, Loss: 0.05320547893643379
Epoch 200/1000, Loss: 0.0409797765314579
Epoch 300/1000, Loss: 0.031562916934490204
Epoch 400/1000, Loss: 0.024309996515512466
Epoch 500/1000, Loss: 0.018723737448453903
Epoch 600/1000, Loss: 0.014420988969504833
Epoch 700/1000, Loss: 0.011107388883829117
Epoch 800/1000, Loss: 0.008555009961128235
Epoch 900/1000, Loss: 0.00658912118524313
Epoch 1000/1000, Loss: 0.005075028631836176

Eğitim tamamlandı!
Ağırlıklar (weights):
tensor([[0.6140],
        [1.2100],
        [1.4945]], requires_grad=True)
Bias (bias):
tensor([2.6047], requires_grad=True)
Yeni veri için tahmin: 59.89932632446289
PS C:\Users\Seda\Desktop\pyProjects\algoritmalar>
"""