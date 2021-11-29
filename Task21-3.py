def f(n, l = [0, 1]):
    if len(l) == n+1:
        return l[-1]
    l.append(l[-2] + l[-1])
    d = f(n, l)    
    return l[-1]
    
r=f(10)
print(r)