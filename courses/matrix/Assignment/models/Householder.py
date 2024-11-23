import numpy as np

def householder(mat):
    m, n = mat.shape
    r = mat.copy()
    q = np.eye(m)

    for i in range(n):
        p1 = r[i:m, i].copy()
        e1 = np.zeros_like(p1)
        e1[0] = 1
        u = p1 - np.linalg.norm(p1) * e1

        # 检查 u 向量是否为零向量，避免归一化时除以零
        if np.linalg.norm(u) != 0:
            u = u / np.linalg.norm(u)

        q_tmp = np.eye(m - i) - 2 * np.outer(u, u)

        q_hat = np.eye(m)
        q_hat[i:m, i:m] = q_tmp

        r = np.matmul(q_hat, r)
        q = np.matmul(q, q_hat)

    return q, r
