import numpy as np


np.set_printoptions(precision=4, suppress=True)


# 打印矩阵
def print_matrix(mat):
    """Print the Matrix"""
    m, n = mat.shape
    for i in range(m):
        for j in range(n):
            print("%8.4f" % mat[i, j], end=',')
        print()


# 从文件中获得矩阵
def load_matrix(file_name):
    """Load Matrix from file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        mat = []

        for line in lines:
            line = line.strip()
            line = line.split(' ')
            line = list(map(eval, line))  # 读文件行
            mat.append(line)

        file.close()

        mat = np.array(mat, dtype=np.float64)
        b = mat[:, -1]
        mat = mat[:, :-1]

        return mat, b