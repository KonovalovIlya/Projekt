import random

sticks = [(p * 0 + 1) * '|' for p in range(1, int(input('Кол-во палок: ')) + 1)]
shot_number = int(input('Количество бросков: '))
shot_list = [
        list(range(random.randint(1, len(sticks) // 2 - 1), random.randint(len(sticks) - (len(sticks) // 2),
        len(sticks)))) for i in range(shot_number)
]
shot_min = len(sticks)
shot_max = 0
for shot in range(shot_number):
    print('Бросок', shot + 1, 'Сбиты палки с номерами с', shot_list[shot][0], 'по', shot_list[shot][-1])
    shot_min = min(shot_list[shot]) - 1
    shot_max = max(shot_list[shot]) - 1
    sticks[shot_min:shot_max + 1] = [(stick * 0 + 1) * '.' for stick in range(shot_min, shot_max + 1)]
print(*sticks,)
