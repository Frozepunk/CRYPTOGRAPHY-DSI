import numpy as np

def minor(matrix, i, j):
    sub_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
    return np.linalg.det(sub_matrix)

def cofactor_matrix(matrix):
    cofactors = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            cofactors[i][j] = ((-1) ** (i + j)) * minor(matrix, i, j)
    return cofactors

def transpose(matrix):
    return matrix.T

def get_matrix_input():
    matrix = []
    print("Enter the elements of a 3x3 matrix (row by row):")
    for i in range(3):
        row = list(map(float, input(f"Enter row {i+1} elements (separated by spaces): ").split()))
        if len(row) != 3:
            print("Please enter exactly 3 elements for each row.")
            return None
        matrix.append(row)
    return np.array(matrix)

matrix = get_matrix_input()

if matrix is not None:
    det = np.linalg.det(matrix)
    
    if det == 0:
        print("\nThe determinant is zero, so the matrix is singular and does not have an inverse.")
    else:
        print(f"\nDeterminant of the matrix: {det}")
        
        cofactor_mat = cofactor_matrix(matrix)
        adjugate = transpose(cofactor_mat)
        inverse_matrix = adjugate / det

        inverse_matrix_int = np.rint(inverse_matrix).astype(int)
        inverse_mod_26 = (inverse_matrix_int % 26 + 26) % 26

        print("\nOriginal Matrix:")
        print(matrix)
        print("\nCofactor Matrix:")
        print(np.rint(cofactor_mat).astype(int))
        print("\nAdjugate (Transpose of Cofactor Matrix):")
        print(np.rint(adjugate).astype(int))
        print("\nInverse Matrix before applying Mod 26 (rounded to nearest integer):")
        print(inverse_matrix_int)
        print("\nInverse Matrix after applying Mod 26 (integer values between 0 and 25):")
        print(inverse_mod_26)
else:
    print("Matrix input was invalid.")
