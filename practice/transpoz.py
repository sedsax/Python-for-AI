def transpose_matrix(matrix):
    """
    Verilen bir matrisin transpozunu döndürür.
    """
    return [list(row) for row in zip(*matrix)]

try:
    rows = int(input("Matrisin satır sayısını giriniz: "))
    cols = int(input("Matrisin sütun sayısını giriniz: "))

    print("Matrisi eleman eleman giriniz (ör: 1 2 3):")
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            raise ValueError("Girilen sütun sayısı yanlış!")
        matrix.append(row)

    transposed = transpose_matrix(matrix)
    print("Matrisin transpozu:")
    for row in transposed:
        print(row)

except ValueError as e:
    print(f"Hata: {e}")
except Exception as e:
    print(f"Beklenmeyen bir hata oluştu: {e}")