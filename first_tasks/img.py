import numpy as np

x = []
y = []
for i in range(1, 3):
    file_path = 'img' + str(i) + '.txt'
    data = np.loadtxt(file_path, comments='#', skiprows=1)

    for row_index, row in enumerate(data):
      for col_index, value in enumerate(row):
        if data[row_index, col_index] == 1:
            x.append(row_index)
            y.append(col_index)
            break

print('смещение равно ' + str(x[0] - x[1]) + ' по X и ' + str(y[0] - y[1]) + ' по Y второй картинки относительно первой')