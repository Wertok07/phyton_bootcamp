lista = [4,1,10,12,3,20,5]

print(lista)
# m = [lista.index(max(lista)), lista.index(min(lista))]
# lista[lista.index(min(lista))] = lista[lista.index(max(lista))]
# lista[m[0]] = m[1]

lista[lista.index(min(lista))], lista[lista.index(max(lista))] = lista[lista.index(max(lista))], lista[lista.index(min(lista))]
print(lista)