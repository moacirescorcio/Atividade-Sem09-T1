impar = 0
par = 0

for c in range(1, 101):
    n = int(input())
    if n % 2 == 0:
        par += 1
    elif n % 2 != 0:
        impar += 1

print(par)
print(impar)