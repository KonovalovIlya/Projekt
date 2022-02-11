import os.path


count = 0
path = os.path.abspath(os.path.join('..', '..', 'Module22'))
for i in os.listdir(path):
    if i.endswith('.py'):
        with open(os.path.join(path, i), 'r', encoding='UTF-8') as file:
            for string in file:
                if string[0].isalpha() or string[0] in ' ':
                    count += 1
print(count)
