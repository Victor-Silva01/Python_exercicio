def inverter_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida

texto = input("Informe uma string: ")

texto_invertido = inverter_string(texto)
print(f"String invertida: {texto_invertido}")
