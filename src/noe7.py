container_list = []
container_amount = int(input('Кол-во контейнеров: '))

for _ in range(container_amount):
    container_number = int(input('Введите вес контейнера: '))
    container_list.append(container_number)

container_number_new = int(input('Введите вес нового контейнера: '))

for index in range(len(container_list)):
    if container_list[index] <= container_number_new:
        container_list.insert(index, container_number_new)

        break
print(container_list)

print('Номер, куда встанет новый контейнер:', index+1)
