import math

def search(x,y,r):
    hipotenusa = math.sqrt(x**2 + y**2)
    if hipotenusa <= r:
        print('Монетка где-то рядом')
    else:
        print('Монетки поблизости нет')


x = float(input('''Координата 'X' '''))
y = float(input('''Координата 'y' '''))
r = float(input('Радиус '))

search(x,y,r)