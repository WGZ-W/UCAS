
import numpy as np
import os
import sys
import argparse
from utils import auxiliary

from models.Givens import givens
from models.Householder import householder
from models.Modified_Gram_Schmidt import modified_gram_schmidt

np.set_printoptions(suppress=True)

# 获取当前工作路径
path = os.getcwd()

ap = argparse.ArgumentParser(description="Three Reduction Methods")

# 选择使用的分解算法，可选项 'MGS', 'HR', 'GR'
ap.add_argument("--model", type=str,
                choices=['MGS', 'HR', 'GR'], default='HR',
                help="3 choices in ['MGS, 'HR', 'GR'], "
                     "MGS -> Modified Gram Schmidt, "
                     "HR -> Householder Reduction "
                     "GR -> Givens Reduction")

# 选择输入的文件
ap.add_argument("--input", type=str,
                default="./data/input.txt",
                help="input example file path.")

args = ap.parse_args()


if __name__ == '__main__':
    input_file = path + '/' + args.input

    matrix, b = auxiliary.load_matrix(input_file)
    m, n = matrix.shape
    if matrix.size == 0:
        print("Input Error!")
        sys.exit()
    print("The Input Matrix: ")
    auxiliary.print_matrix(matrix)

    # Initial Q, R variable
    Q, R = matrix, matrix

    if args.model == "MGS":
        Q, R = modified_gram_schmidt(matrix)
    elif args.model == "HR":
        Q, R = householder(matrix)
    elif args.model == "GR":
        Q, R = givens(matrix)

    # Print results
    print("\nThe factorization Results：")
    print("\nMatrix Q: ")
    auxiliary.print_matrix(Q)
    print("\nMatrix R:")
    auxiliary.print_matrix(R)

    # Compute x through QR
    y = Q.T @ b
    x = np.linalg.solve(R, y)
    print("\nSolution x = ", x)
