def site_consruct(number, structure):
    for i in range(number):
        brend = input('Введите название продукта для нового сайта: ')
        site_list[i] = search_function(structure, brend, 'title', 'h2')
        print(site_list)


def search_function(structure, brend, *args):
    for arg in args:
        if arg in structure.keys():
            if arg == 'title':
                structure[arg] = structure.get(arg).replace(structure.get(arg)[13:-9], brend, 1)
            elif arg == 'h2':
                structure[arg] = structure.get(arg).replace(structure.get(arg)[27:], brend, 1)
        for substructure in structure.values():
            if isinstance(substructure, dict):
                search_function(substructure, brend, *args)
    return structure


site_list = {}
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

site_amount = int(input('Сколько сайтов: '))
site_consruct(site_amount, site)
