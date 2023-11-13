a = int(input("Introduceți valoarea pentru a: "))
n = int(input("Introduceți valoarea pentru n: "))
rezultat = a
while n > 0:
    rezultat *= 10
    n -= 1

print(rezultat)