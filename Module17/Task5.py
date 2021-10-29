s_l = list(input())
h_1 = s_l.index('h')
h_2 = s_l[h_1+1:].index('h') + h_1+1
s_l[h_1:h_2] = s_l[h_2:h_1:-1]
print(*s_l,)