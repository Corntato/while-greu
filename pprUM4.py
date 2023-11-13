n = int(input("Introduceți valoarea pentru n: "))
s1 = 0
i = 1
while i <= n:
    s1 += i
    i += 1
s2 = 0
i = 1
while i < n:
    s2 += i * (i + 1)
    i += 1
s3 = 0
f = 1
i = 1
while i <= n:
    f *= i
    s3 += f
    i += 1
s5 = 0
i = 1
while i <= n:
    s5 += i / (i + 1)
    i += 1
s6 = 0
i = 2
while i <= 100:
    if i % 2 == 0:
        s6 += i
    else:
        s6 -= i
    i += 1
print('s1=',s1)
print('s2=',s2)
print('s3=',s3)
print('s5=',s5)
print('s6=',s6)