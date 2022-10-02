def dot_product(N, vector1, vector2):
    sum_product = 0
    for i in range(N):
        sum_product += vector1[i] * vector2[i]
    return sum_product