def f(data, list_2 = [], list_3 = []):
    for i in data:
        if i >= list_2[0]:
            list_2.insert(0,data.pop(0))
            print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(
                i,
                data,
                list_2
            ))
        elif not i >= list_2[0]:
            list_3.insert(0, data.pop(0))



list_1 = [0,1,2,3,4,5,6,7,8,9]
res = f(list_1)
