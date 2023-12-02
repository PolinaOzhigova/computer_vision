import numpy as np

for i in range(1, 7):
    file_path = 'figure' + str(i) + '.txt'
    data = np.loadtxt(file_path, comments='#', skiprows=1)

    mm = 0
    with open(file_path, 'r') as file:
      mm = int(file.read(1))

    max_one = max(data.tolist(), key=lambda row: row.count(1))
    pixel = max_one.count(1)
    if pixel == 0:
      print(f"Изображение {file_path}: Номинальное разрешение = 0")
      break
    result = mm / pixel
    print(f"Изображение {file_path}: Номинальное разрешение = {result} мм/пиксель")