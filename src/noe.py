for a in range(11):
    for b in range(11):
        b = b * a
        print(b, end = '\t')
    print()

print()

for a in range(11):
    for b in range(a, 11):
        b = b * a
        print(b, end='\t')
    print()