def next_tour_f(data, score = '', dict_members = {}):
    for string in data:
        if string.endswith('\n'):
            string = string[:-1]
        if string.isdigit():
            score = string
        else:
            members = string.split()
            if members[2] > score:
                dict_members[(members[0], members[1])] = members[2]
    for i, j in dict_members.items():

    print(dict_members)
    second_tour = open('second_tour.txt', 'w')
    second_tour.write(str(len(list(enumerate(dict_members))))+'\n')
    second_tour.close()
    for i, j in enumerate(dict_members):
        second_tour = open('second_tour.txt', 'a')
        second_tour.write(
        '{0}) {1}. {2} {3}\n'.format(
            i,
            j[1][0],
            j[0],
            dict_members.get(j)
        )

    )

    # return  dict_members


first_tour = open('first_tour.txt', 'w')
first_tour.write(
    '80\n'
    'Ivanov Serg 80\n'
    'Segeev Petr 92\n'
    'Petrov Vasiliy 98\n'
    'Vasiliev Maxim 78\n'
)
first_tour.close()

first_tour = open('first_tour.txt', 'r')
# next_tour_f(first_tour)
print(next_tour_f(first_tour))