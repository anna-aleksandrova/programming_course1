import matrices as m
matrix = m.matrix_input()
matrix_det = matrix.copy()

print("\nUpper triangular matrix:")
m.matrix_output(m.upper_triangular(matrix.copy()))

print(f"\nRank of the matrix: {m.rank(matrix)}")

print(f"\nDeterminant of the matrix: {m.det(matrix_det):.2f}")