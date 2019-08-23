import matplotlib.pyplot as plt
#TextoCifrado
ciphertext = "PBFPVYFBQXZTYFPBFEQJHDXXQVAPTPQJKTOYQWIPBVWLXTOXBTFXQWAXBVCXQWAXFQJVWLEQNTOZQGGQLFXQWAKVWLXQWAEBIPBFXFQVXGTVJVWLBTPQWAEBFPBFHCVLXBQUFEVWLXGDPEQVPQGVPPBFTIXPFHXZHVFAGFOTHFEFBQUFTDHZBQPOTHXTYFTODXQHFTDPTOGHFQPBQWAQJJTODXQHFOQPWTBDHHIXQVAPBFZQHCFWPFHPBFIPBQWKFABVYYDZBOTHPBQPQJTQOTOGHFQAPBFEQJHDXXQVAVXEBQPEFZBVFOJIWFFACFCCFHQWAUVWFLQHGFXVAFXQHFUFHILTTAVWAFFAWTEVOITDHFHFQAITIXPFHXAFQHEFZQWGFLVWPTOFFA"
#Funcion para contar el numero de veces que se repite un caracter
def frequency(ciphertext):
    all_freq = {} 
    for i in ciphertext: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    #Mostrar resultados
    print ("Numero de repeticiones por caracater:\n "+ str(all_freq))
    plt.bar(range(len(all_freq)), list(all_freq.values()), align='center')
    plt.xticks(range(len(all_freq)), list(all_freq.keys()))
    plt.show()
    return 0
#Lllamdo de la funcion
frequency(ciphertext)
intab = "ABCDEFGHIJKLNOPQTUVWXYZ"
key=input("Inserte llave, notese que los valores introducidos seran relacionados con los caracteres en orden alfabetico y la llave debe ser de la misma extension del numero de caracteres en el texto cifrado\n"+intab+"\n")
#Datos para crear tabla de traduccion

outtab = key#Clave para descifrar "DHPUWEBRYLKGXFTAOVINSMC"
#Crear tabla de traduccion
trantab = str.maketrans(intab, outtab)
#Texto a traducir
str = "PBFPVYFBQXZTYFPBFEQJHDXXQVAPTPQJKTOYQWIPBVWLXTOXBTFXQWAXBVCXQWAXFQJVWLEQNTOZQGGQLFXQWAKVWLXQWAEBIPBFXFQVXGTVJVWLBTPQWAEBFPBFHCVLXBQUFEVWLXGDPEQVPQGVPPBFTIXPFHXZHVFAGFOTHFEFBQUFTDHZBQPOTHXTYFTODXQHFTDPTOGHFQPBQWAQJJTODXQHFOQPWTBDHHIXQVAPBFZQHCFWPFHPBFIPBQWKFABVYYDZBOTHPBQPQJTQOTOGHFQAPBFEQJHDXXQVAVXEBQPEFZBVFOJIWFFACFCCFHQWAUVWFLQHGFXVAFXQHFUFHILTTAVWAFFAWTEVOITDHFHFQAITIXPFHXAFQHEFZQWGFLVWPTOFFA"
#Mostrar texto traducido
print (str.translate(trantab))
