def poista(paramlista):
    lista = []
    for n in paramlista:
        if n % 2 == 0:
            lista.append(n)
    return lista


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45, 24, 67, 75, 522, 8501, 1000]
lista2 = [2, 3, 4, 5]
lista3 = [5, 6, 7, 10]

print( poista(lista) )
print( poista(lista2) )
print( poista(lista3) )

uusilista = poista([11, 12, 13])
print(uusilista)