def f(s, structure):
    if s in structure.keys():
        return structure[s]
    for i, j in structure.items():
        if isinstance(j, dict):
            k = f(s, j)
            return k
    return 'takogo klucha net'


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

s = 'div'
res = f(s, site)
print(res)