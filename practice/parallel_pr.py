# matrix_perf_test.py

import numpy as np
import time
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count


# ---------------- Seri Matris Çarpımı ----------------
def serial_matrix_multiplication(A, B):
    return np.dot(A, B)


# ---------------- Paralel Matris Çarpımı ----------------
def parallel_worker(args):
    row, B = args
    return np.dot(row, B)

def parallel_matrix_multiplication(A, B):
    with Pool(processes=cpu_count()) as pool:
        result = pool.map(parallel_worker, [(row, B) for row in A])
    return np.array(result)


# ---------------- Performans Testi ----------------
def test_performance(matrix_sizes):
    serial_times = []
    parallel_times = []
    speedups = []

    for size in matrix_sizes:
        print(f"Testing {size}x{size} matrix...")

        A = np.random.rand(size, size)
        B = np.random.rand(size, size)

        start = time.time()
        serial_matrix_multiplication(A, B)
        serial_time = time.time() - start

        start = time.time()
        parallel_matrix_multiplication(A, B)
        parallel_time = time.time() - start

        serial_times.append(serial_time)
        parallel_times.append(parallel_time)
        speedups.append(serial_time / parallel_time)

    return serial_times, parallel_times, speedups


# ---------------- Grafik ----------------
def plot_results(sizes, serial_times, parallel_times, speedups):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(sizes, serial_times, label='Serial', marker='o')
    plt.plot(sizes, parallel_times, label='Parallel', marker='o')
    plt.xlabel("Matrix Size (N x N)")
    plt.ylabel("Time (s)")
    plt.title("Execution Time")
    plt.yscale('log')  # Logaritmik ölçek
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(sizes, speedups, marker='o')
    plt.axhline(1, color='red', linestyle='--', label='No Speed-up')
    plt.xlabel("Matrix Size (N x N)")
    plt.ylabel("Speed-up (Serial / Parallel)")
    plt.title("Speed-up")
    plt.legend()

    plt.tight_layout()
    plt.show()


# ---------------- Ana Fonksiyon ----------------
if __name__ == "__main__":
    matrix_sizes = [100, 300, 500, 800, 1000]  # Sistemine göre daha büyük boyutlar da ekleyebilirsin
    serial_times, parallel_times, speedups = test_performance(matrix_sizes)
    plot_results(matrix_sizes, serial_times, parallel_times, speedups)
