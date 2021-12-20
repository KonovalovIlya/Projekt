def analysis_f(data, dict_ = {}, alphabet ='abcdefghijklmnopqrstuvwxyz'):
    total = 0
    for string in data:
        for symbol in string.lower():
            if symbol in alphabet:
                total += 1
                if symbol in dict_.keys():
                    dict_[symbol] += 1
                else:
                    dict_[symbol] = 1
    list_ = sorted([(i, round(j / total, 3)) for i, j in dict_.items()], key= lambda symbol: symbol[0])
    for i, j in enumerate(list_):
        if i > 0 and j[1] > list_[i-1][1]:
            list_.insert(i-1, list_.pop(i))
    analysis = open('analysis.txt', 'w')
    analysis.close()
    analysis = open('analysis.txt', 'a')
    for i in list_:
        analysis.write('{0} - {1}\n'.format(i[0],i[1]))
    analysis.close()


text = open('text.txt', 'w')
text.write('Mama myla ramu.\n')
text.close()
text = open('text.txt', 'r')
analysis_f(text)
