tupla = ('a', 'b', 'c','d')
print(type(tupla).__name__)
lista = list(tupla)
lista[1] = 'Me han cambiado'
tupla = tuple(lista)
print(tupla)
print(type(tupla).__name__)
r=list(range(6))
print(r)
print(sum(range(6)))