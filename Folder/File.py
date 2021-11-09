family_member = {}
#    "name": "Jane",
#    "surname": "Doe",
#    "hobbies": ["running", "sky diving", "singing"],
 #   "age": 35,
#    "children": [
 #       {
 #           "name": "Alice",
#            "age": 6
#        },
#        {
#            "name": "Bob",
#            "age": 8
#        }
 #   ]
#}
string = input('Введите через пробел: ').split()
family_member['name'] = string[0]
family_member['surname'] = string[1]
family_member['hobbies'] = []
for j in string[2:]:
    if not j.isdigit():
        family_member['hobbies'].append(j)
    else:
        break
family_member['age'] = string[string.index(j)]
family_member['children'] = []
count = -1
k = string.index(j) + 1

for f in range(len(string[k:])):

    if f % 2 == 0:
        family_member['children'].append({})
        count += 1
        family_member['children'][count]['name'] = string[k + f]
    else:
        family_member['children'][count]['age'] = string[k + f]
for f_info in family_member:
    print(f_info, '-', family_member[f_info])
