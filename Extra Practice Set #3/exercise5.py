def generate_multiples(n, count):
    multiples = []
    i = 1
    while len(multiples) < count:
        multiples.append(n * i)
        i += 1
    return multiples


print(generate_multiples(3, 6))
