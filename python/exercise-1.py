def duplicar_vocales(str):
    new_str = ""
    for letter in str:
        if is_a_vocal(letter):
            new_str += letter
        new_str += letter
    return new_str

def is_a_vocal(l):
    return l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u'

string_prueba = "gracias"
prueba = duplicar_vocales(string_prueba)

print(prueba)
