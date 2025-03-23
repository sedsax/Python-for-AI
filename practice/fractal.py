import numpy as np
import matplotlib.pyplot as plt

# Julia kümesini hesaplayan fonksiyon
def julia(width, height, max_iter, c):
    # Gerçek ve sanal eksenlerin sınırları
    re_min, re_max = -1.5, 1.5
    im_min, im_max = -1.5, 1.5

    # Karmaşık düzlemdeki piksel noktalarını oluşturma
    real = np.linspace(re_min, re_max, width)
    imag = np.linspace(im_min, im_max, height)
    real, imag = np.meshgrid(real, imag)
    z = real + imag * 1j

    # Julia kümesi için iterasyon
    julia_set = np.full(z.shape, max_iter, dtype=int)

    for i in range(max_iter):
        mask = np.abs(z) <= 2
        z[mask] = z[mask] ** 2 + c
        julia_set[mask] = i

    return julia_set

# Görselleştirme ve kaydetme
def plot_julia(image, filename):
    plt.imshow(image, extent=(-1.5, 1.5, -1.5, 1.5), cmap="inferno")
    plt.colorbar()
    plt.title("Julia Set")
    plt.savefig(filename)
    plt.show()

# Çözünürlük, iterasyon ve sabit c değeri
width, height, max_iter = 800, 800, 300
c = -0.7 + 0.27015j  # Julia kümesi için sabit değer
julia_image = julia(width, height, max_iter, c)

# Fraktalı görselleştirme ve kaydetme
plot_julia(julia_image, "julia.png")