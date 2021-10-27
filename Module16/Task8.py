import random
N = list(range(1,10))
K = int(input('Количество бросков: '))
l = [[random.randint(1, 10)] for i in range(K)]
print(l)