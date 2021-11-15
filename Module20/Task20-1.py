def data(dict):
    list_ = []
    string = ''
    for elem in dict:
        list_ += (dict.get(elem).get('interests'))
        string += dict.get(elem).get('surname')
    count = len(string)
    return list_, count


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

for student_number, student_info in students.items():
        print(student_number, student_info.get('name'))

student_interests_lst, surname_all = data(students)
print('Список интересов всех студентов: {interests}\nОбщая длина всех фамилий студентов: {surname_length}'.format(
    interests = student_interests_lst,
    surname_length = surname_all
))
