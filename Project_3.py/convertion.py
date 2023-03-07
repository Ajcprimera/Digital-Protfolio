from grid import Matrix

def convertion_r (rows, colums):
    matrix = Matrix()
    matrix_r = matrix.generate_random_value(rows,colums)
    return matrix_r

def convertion_u(rows, colums):
    matrix = Matrix()
    matrix_u = matrix.generate_user_values(rows, colums)
    return matrix_u