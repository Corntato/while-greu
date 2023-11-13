a = int(input("Introduceți primul etaj: "))
b = int(input("Introduceți al doilea etaj: "))
if a < b:
    pas = 1
else:
    pas = -1
while a != b:
    print(a, end=" ")
    a += pas

print(b)