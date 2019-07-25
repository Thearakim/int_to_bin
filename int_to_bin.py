def int_to_binary(a, b):
    sum = a + b
    temBi = ""
    while sum != 0:
        temBi = str(sum % 2) + temBi
        sum  //=  2
    return temBi


print(int_to_binary(12, 3))