import numpy as np

def givens(mat):
    """Performs givens qr Decomposition."""
    m, n = mat.shape
    q = np.eye(m)
    r = mat.copy()
    
    for i in range(n):
        for j in range(i + 1, m):
            if r[j, i] != 0:
                r_ = np.hypot(r[i, i], r[j, i])
                c = r[i, i] / r_
                s = r[j, i] / r_

                g = np.eye(m)
                g[i, i] = c
                g[j, j] = c
                g[i, j] = s
                g[j, i] = -s
                r = g @ r
                q = q @ g
    return q, r