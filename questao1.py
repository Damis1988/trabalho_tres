
lista = []

lista.append("1")
lista.append("2")
lista.append("3")
lista.append("4")
lista.append("5")
print(lista)
print(len(lista))

# Criei uma funçao que busca na lista se existe e apaga, se caso não encontrado informa ao usuario e se o numero não existe
def encontrar():

    n = input("Insira o numero a ser deletado : ")
    if  n  in lista :
        lista.remove(n)
        print("numero deletado com sucesso")
    else :
        print("numero nao existe")
        return n

encontrar()
print(lista)
lista.insert(5,"6")
print(lista)