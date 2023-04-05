matrix = []
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the matrix elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        print("Enter element", [i+1],[j+1], end=" ")
        num = int(input())
        row.append(num)
    matrix.append(row)
print("Original matrix:")
for row in matrix:
    print(row)
transpose = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)
print("Transpose of the matrix:")
for row in transpose:
    print(row)
