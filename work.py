A
====
a = float(input())
b = float(input())
c = (a ** 2 + b ** 2) ** 0.5
print(c)

B
====
a = str(input())
print('Hello,',a)

C
====
a = int(input())
b = a + 1
c = a - 1
print('Следующее число после', a,'число', b)
print('Предыдущее числу', a,'число', c)

D
====
n = int(input())  # школьники
m = int(input())  # яблоки
c = m // n
o = m - c * n  # остаток
print('Достанется каждому', c)
print('Останется в корзине', o)

F
====
v = int(input())
t = int(input())
s = v * t  # расстояние
if v >= 0:
    if s <= 109:
        print(s)
    elif s > 109:
        n = abs(108 - s)
        print(n)
elif v < 0:
    if s <= 109:
        n = abs(109 - s)
        print(n)
    elif s > 109:
        n = abs(109 - s)
        print(n)

G
====
a = int(input())
b = a % 10
print(b)

H
====
a = int(input())
print(a // 10)

J
====
a = int(input())
print(a % 10 + a // 10 + a // 100)

