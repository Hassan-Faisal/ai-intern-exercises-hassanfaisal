import numpy as np
from typing import Tuple


def softmax(x: np.ndarray) -> np.ndarray:
    exp_values = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_values / np.sum(exp_values, axis=-1, keepdims=True)

def scaled_dot_product_attention(
    Q: np.ndarray,
    K: np.ndarray,
    V: np.ndarray
) -> np.ndarray:
    d_k = Q.shape[-1]

    scores = np.matmul(Q, K.T)
    scaled_scores = scores / np.sqrt(d_k)

    attention_weights = softmax(scaled_scores)

    output = np.matmul(attention_weights, V)

    return output


if __name__ == "__main__":
    np.random.seed(42)

    Q = np.random.rand(3, 4)
    K = np.random.rand(3, 4)
    V = np.random.rand(3, 4)

    result = scaled_dot_product_attention(Q, K, V)

    print("Attention Output:\n", result)