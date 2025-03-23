def Celsius_to_Fahrenheit(cel):
    return [(c * 9 / 5) + 32 for c in cel]


print(Celsius_to_Fahrenheit([32, 40]))
