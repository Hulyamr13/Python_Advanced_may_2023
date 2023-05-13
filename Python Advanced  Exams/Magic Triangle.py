def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    for i in range(2, n):
        row = [1] + [triangle[i-1][j] + triangle[i-1][j+1] if j+1 < len(triangle[i-1]) else triangle[i-1][j] for j in range(len(triangle[i-1]))]
        triangle.append(row)
    return triangle

print(get_magic_triangle(5))
