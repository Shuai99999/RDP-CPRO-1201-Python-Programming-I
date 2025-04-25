def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    width = len("   ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = "   ".join(str(x) for x in row)
        print(row_str.center(width))


pascal_triangle(5)
