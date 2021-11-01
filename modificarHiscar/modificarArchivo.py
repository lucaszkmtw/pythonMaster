
from archivo import fileOpen
def modificar(list_of_lines, nuevalinea):

    for linea in range(0, len(list_of_lines)):
    
        if list_of_lines[linea][0:4] == 'M006':
            list_of_lines[linea] = list_of_lines[linea].replace('M006' ,nuevalinea).upper() + '\n'
    a_file = open("myfile.txt", "w")
    a_file.writelines(list_of_lines)  
    a_file.close()


nuevo = input("Enter your value: ")
lista = fileOpen()
print(lista)
modificar(lista, nuevo)