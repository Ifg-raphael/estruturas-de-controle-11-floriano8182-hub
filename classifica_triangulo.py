a = int(input())
b = int(input())
c = int(input())

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print("equilátero")
    elif a == b or b == c or a == c:
        print("isósceles")
    else:
        print("escaleno")
else:
    print("Não forma triângulo")