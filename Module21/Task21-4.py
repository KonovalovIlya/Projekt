def search_function(key, structure, depth_search = 0, depth = 0):
    if depth_search == 0:
        if key in structure.keys():
            return structure[key]
        for substructure in structure.values():
            if isinstance(substructure, dict):
                result = search_function(key, substructure)
                if result:
                    break
        else:
            result = None
            return result
    else:
        if depth == depth_search and key in structure.keys():
            return structure[key]
    for substructure in structure.values():
        if isinstance(substructure, dict):
            depth += 1
            result = search_function(key, substructure, depth_search, depth)
            if result:
                break
            else:
                depth -= 1
    else:
        result = None
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

search = input('Что ищем: ')
depth = int(input('Укажите глубину поиска(0 - по всей глубине структоры): '))
if depth == 0:
    out = search_function(search, site)
else:
    out = search_function(search, site, depth)
if out:
    print(out)
else:
    print('Такого ключа нет')