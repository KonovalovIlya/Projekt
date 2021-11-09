file_name = input('Название файла: ')
wrong_symbols = '@№$%^&*()'
wrong_suffix = ['.txt', '.docx']
if file_name.startswith(tuple(wrong_symbols)):
# Название файла: @example.txt
    print('Ошибка: название начинается на один из специальных символов')
elif not file_name.endswith(tuple(wrong_suffix)):
# Название файла: example.ttx
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
# Название файла: example.txt
else:
    print('Файл назван верно.')
