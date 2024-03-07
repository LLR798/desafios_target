def inverte_string(original):
    invertida = ""

    for i in range(len(original) - 1, -1, -1):
        invertida += original[i]

    return invertida

string_original = input("Digite uma string: ")  
string_invertida = inverte_string(string_original)

print(f"A string invertida é: {string_invertida}")
