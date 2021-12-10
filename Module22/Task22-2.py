zen = open('zen.txt', 'r')
l=[]
for _ in zen:
    if _.endswith('\n') or _.endswith(''):
        l.append(_[:-1])
for i in l[::-1]:
    print(i)