import numpy as np


def modified_gram_schmidt(mat):
    """Modified Gram Schmidt Reduction"""
    m, n = mat.shape
    q = mat.copy()  # Using the shallow copy of mat

    for i in range(n):
        # normalization
        v = q[:, i]
        norm = np.linalg.norm(v)
        v = v / norm
        q[:, i] = v

        for j in range(i+1, n):
            u = q[:, j]
            u = u - np.matmul(u, v) * v
            q[:, j] = u

    # q = q.T
    r = np.matmul(q.T, mat)

    return q, r
