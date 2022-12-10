def histogram(lista):
    hg = ''
    for i in range(len(lista)):
        if type(lista[i]) != int:
            return
        for j in range(lista[i]):
            hg += '#'
        if i < len(lista)-1:
            hg += '\n'
    return hg


h = histogram([1.5, 2, 8])
print(h)
