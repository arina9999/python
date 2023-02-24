# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной 
# и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random
n = int(input("Введите количество подбрасываемых монет: "))
side_1 = 0
side_2 = 0
for i in range(n):
     side = random.randint(0,1)
     print(f"side of {i + 1} coin = {side}")
     if side == 1:
        side_1 +=1
     else:
        side_2 +=1
if side_1 < side_2:
    print (f"Минимальное количество монет, которое нужно перевернуть = {side_1}")
else:
    print (f"Минимальное количество монет, которое нужно перевернуть = {side_2}")

