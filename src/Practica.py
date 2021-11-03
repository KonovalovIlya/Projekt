string = input('Введите данные человека'
               '\n(имя, фамилия, хобби, кол-во лет и дети) \n').split()
family_member = dict()
family_member["name"] = string[0]
family_member["surname"] = string[1]
family_member["hobbies"] = []
for elem in string[2:]:
    if elem.isalpha():
        family_member["hobbies"].append(elem)
    else:
        break
family_member["age"] = string[len(family_member["hobbies"]) + 2]
family_member["children"] = list()
for n in range(int(string[string.index(family_member["age"]) + 1])):
    family_member["children"].append({"name": string[string.index(family_member["age"]) + 2 + n*2],
                                      "age": string[string.index(family_member["age"]) + 3 + n*2]}
                                     )
print(family_member)
print(family_member.get("children",{}).get("name", {}))