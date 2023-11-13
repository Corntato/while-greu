n = int(input("Introduceți un număr între 1 și 10: "))
while n < 1 or n > 10:
    print("Valoarea introdusă nu este în intervalul specificat.")
    n = int(input("Introduceți un număr între 1 și 10: "))
i = 1
while i <= 10:
    rezultat = n * i
    print(n,'*',i,'=',n * i)
    i += 1