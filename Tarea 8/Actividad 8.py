def busqueda_binaria(arr, objetivo, inicio, fin):
    if inicio > fin:
        return -1  

    medio = (inicio + fin) // 2

    if arr[medio] == objetivo:
        return medio
    elif arr[medio] > objetivo:
        return busqueda_binaria(arr, objetivo, inicio, medio - 1)
    else:
        return busqueda_binaria(arr, objetivo, medio + 1, fin)

def buscar(arr, objetivo):
    return busqueda_binaria(arr, objetivo, 0, len(arr) - 1)

if __name__ == "__main__":
    lista_ordenada = [4, 7, 10, 22, 34, 52, 64, 90]
    objetivo = 22
    resultado = buscar(lista_ordenada, objetivo)

    if resultado != -1:
        print(f"Elemento {objetivo} encontrado en el índice {resultado}.")
    else:
        print(f"Elemento {objetivo} no encontrado en la lista.")