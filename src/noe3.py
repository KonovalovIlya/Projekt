cell_efficiency_bad = []
cell_number = int(input('Кол-во клеток: '))
for cell in range(1, cell_number + 1):
    cell_efficiency = int(input(f'Эффективность {cell}-й клетки: '))
    if cell_efficiency < cell:
        cell_efficiency_bad.append(cell_efficiency)
print(f'Неподходящие значения: {cell_efficiency_bad}')
