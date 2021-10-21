"""
Pętla iterująca
"""
lista1 = [9,-10,11,-100,20,0,0.1,-1234]
lista_res = []
print(lista1)
for ix, x in enumerate(lista1, 1):
    if x<=0:
        lista_res.append(ix)
print(lista_res)