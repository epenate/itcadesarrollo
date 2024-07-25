import  random

def Cargar():
    list = []
    for x in range(10):
        list.append(random.randint(0,1000))
    return list

def Imprimir(lista):
    print(lista)


def  Mover(lista):
    random.shuffle(lista)

miLista = Cargar()

print("La lista es :")
Imprimir(miLista)
print("Lista Mezclada :")
Mover(miLista)
print(miLista)