import numpy as np


def rand_sym_matrix(n, val_range=10 ** 6):
    m = np.random.uniform(-val_range, val_range, size=(n, n))
    return (m + m.T) / 2


def lib_solution(matrix):
    w, v = np.linalg.eig(matrix)
    i = np.argmax(abs(w))
    return v[:, i], w[i]


def norm(vector):
    return vector / abs(np.linalg.norm(vector, axis=0))


def check_correct(vector, dominant, lib_vector, lib_dominant, eps=10 ** -5):
    print("Vector correct: ", np.all(abs(abs(vector) - abs(lib_vector)) < eps), ", Dominant correct: ",
          (abs(dominant - lib_dominant) < eps))
