import torch

# 1. Tensör Oluşturma
# Bir tensör oluşturma
tensor_a = torch.tensor([1.0, 2.0, 3.0])
print("Tensor A:", tensor_a)

# Rastgele bir tensör oluşturma
tensor_b = torch.rand(3, 3)
print("Tensor B (random):", tensor_b)

# 2. Tensör İşlemleri
# Tensör toplama
tensor_sum = tensor_a + tensor_a
print("Sum of Tensor A:", tensor_sum)

# Tensör çarpma
tensor_mul = tensor_a * 2
print("Tensor A multiplied by 2:", tensor_mul)

# Matris çarpımı
tensor_c = torch.tensor([[1, 2], [3, 4]])
tensor_d = torch.tensor([[5, 6], [7, 8]])
tensor_matmul = torch.matmul(tensor_c, tensor_d)
print("Matrix multiplication of Tensor C and D:", tensor_matmul)

# 3. Tensör Özellikleri
# Tensör boyutu
print("Shape of Tensor B:", tensor_b.shape)

# Tensör tipi
print("Data type of Tensor A:", tensor_a.dtype)

# 4. Tensör Dönüşümleri
# Numpy dizisine dönüştürme
numpy_array = tensor_a.numpy()
print("Numpy array from Tensor A:", numpy_array)

# Numpy dizisinden tensör oluşturma
new_tensor = torch.from_numpy(numpy_array)
print("Tensor from Numpy array:", new_tensor)

# 5. GPU Kullanımı (Eğer GPU varsa)
if torch.cuda.is_available():
    tensor_gpu = tensor_a.to('cuda')
    print("Tensor A on GPU:", tensor_gpu)
else:
    print("CUDA is not available. Running on CPU.")

# 6. Tensörlerin Gradients Özelliği
# Tensörlerin otomatik türevlenmesi için requires_grad=True ayarı
tensor_e = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
print("Tensor E with gradients:", tensor_e)

# Basit bir hesaplama ve geri yayılım (backpropagation)
result = tensor_e.sum()
result.backward()
print("Gradients of Tensor E:", tensor_e.grad)