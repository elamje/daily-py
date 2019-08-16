def combinations(mat):
    n = len(mat)
    k = len(mat[0])
    solution_matrix = [[0] * k]

    for r, row in enumerate(mat):
        row_cost = []
        for c, val in enumerate(row):
            row_cost.append(min(solution_matrix[r][i] for i in range(k) if i != c) + val)
        solution_matrix.append(row_cost)
    return min(solution_matrix[-1])
