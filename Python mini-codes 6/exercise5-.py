def find_roots(a, b, c):
    # 计算判别式
    discriminant = b**2 - 4 * a * c

    # 判断判别式的值
    if discriminant > 0:
        # 有两个实数根
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        # 有一个实数根
        root = -b / (2 * a)
        return (root,)
    else:
        # 没有实数根
        real_part = -b / (2 * a)
        imaginary_part = (abs(discriminant) ** 0.5) / (2 * a)
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))


def factor_quadratic(a, b, c):
    roots = find_roots(a, b, c)

    # 如果根是实数
    if all(isinstance(root, (int, float)) for root in roots):
        factorized_form = f"(x - {roots[0]}) * (x - {roots[1]})"
    else:
        factorized_form = f"(x - {roots[0]}) * (x - {roots[1]})"

    return factorized_form, roots


# 接受用户输入的多项式系数
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

factorized_form, roots = factor_quadratic(a, b, c)

print(f"Factorized form of the polynomial is: {factorized_form}")
print(f"Roots of the polynomial are: {roots}")
