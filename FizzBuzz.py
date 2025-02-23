import random
FizzDiv = random.randint(2,5)
BuzzDiv = random.randint(2,5)
print("Fizz : ", FizzDiv)
print("Buzz : ", BuzzDiv)
lista = []
for i in range(0, 9):
    i = random.randint(0, 19)
    lista.append(i)
lista.sort()
print("Before : ", lista)
for x in range(len(lista)):
    if lista[x] % FizzDiv == 0 and lista[x] % BuzzDiv == 0:
        lista[x] = "FizzBuzz"
    elif lista[x] % FizzDiv == 0:
        lista[x] = "Fizz"
    elif lista[x] % BuzzDiv == 0:
        lista[x] = "Buzz"
print("After : ", lista)
