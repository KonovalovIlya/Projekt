def next_tour_f(data, score = '', tuple_members = tuple()):
    for string in data:
        if string.endswith('\n'):
            string = string[:-1]
        if string.isdigit():
            score = string
        else:
            members = string.split()
            if members[2] > score:
                tuple_members += (((members[0], members[1]),members[2]),)
    tuple_members = tuple(sorted(tuple_members, key= lambda member: member[1], reverse=True))
    second_tour = open('second_tour.txt', 'w')
    second_tour.write(str(len(list(enumerate(tuple_members)))) + '\n')
    second_tour.close()
    second_tour = open('second_tour.txt', 'a')
    for i, j in enumerate(tuple_members):
        second_tour.write(
            '{0}) {1}. {2} {3}\n'.format(
                i+1,
                j[0][1][0],
                j[0][0],
                j[1]
            )
        )
    second_tour.close()


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
next_tour_f(first_tour)
