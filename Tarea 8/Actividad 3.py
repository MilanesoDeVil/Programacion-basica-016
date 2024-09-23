def invertir_cadena(cadena):
    # Caso base: si la cadena está vacía o tiene un solo carácter
    if len(cadena) <= 1:
        return cadena
    # Caso recursivo: invertir la cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

texto = input("Ingrese una cadena de texto: ")
texto_invertido = invertir_cadena(texto)
print(f"La cadena invertida es: {texto_invertido}")