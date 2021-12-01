def site_consruct(number, structure):
    brend = input('Введите название продукта для нового сайта: ')
    site_list = {i: search_function(structure, brend, 'title', 'h2') for i in range(number)}
    print(site_list)


def search_function(structure, brend, *args):
    for arg in args:
        if arg in structure.keys():
            structure[arg] = structure[arg].replace('{}', brend, 1)
        for substructure in structure.values():
            if isinstance(substructure, dict):
                result = search_function(substructure, brend, *args)
    return structure


site_amount = int(input('Сколько сайтов: '))

site_list = []
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {}',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

site_consruct(site_amount, site)