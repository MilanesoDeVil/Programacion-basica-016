def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivote = arr[-1]
    izquierda = []
    derecha = []

    for elemento in arr[:-1]: 
        if elemento < pivote:
            izquierda.append(elemento)
        else:
            derecha.append(elemento)

    return quick_sort(izquierda) + [pivote] + quick_sort(derecha)

if __name__ == "__main__":
    lista = [20, 69, 80, 65, 8, 44, 78]
    print("Lista original:", lista)
    lista_ordenada = quick_sort(lista)
    print("Lista ordenada:", lista_ordenada)