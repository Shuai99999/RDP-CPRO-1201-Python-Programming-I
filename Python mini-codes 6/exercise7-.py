def is_pythagorean_triple(a, b, c):
    # 确保 a, b, c 是正整数
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # 检查是否满足勾股定理
    return a**2 + b**2 == c**2


def main():
    # 从用户输入三个数字
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))

    # 判断是否为毕达哥拉斯三元组
    if is_pythagorean_triple(a, b, c):
        print(f"The numbers {a}, {b}, and {c} form a Pythagorean triple.")
    else:
        print(f"The numbers {a}, {b}, and {c} do not form a Pythagorean triple.")


main()
