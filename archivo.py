
 
# Opening file
file1 = open('prueba.txt', 'r')
count = 0
lista = []
# Using for loop

for line in file1:
    count += 1
    linea = "{}".format(line.strip())
    
    lista.append(linea)

# Closing files
file1.close()

# nuevo = lista[1]
# nuevo1 = nuevo[4:8]
# print(nuevo1)



def modificar(list_of_lines, nuevalinea):
    # a_file = open("prueba.txt", "r")
    # list_of_lines = a_file.readlines()

    # list_of_lines[1] = "Line2"
    for linea in range(0, len(list_of_lines)):
    
        if list_of_lines[linea][0:4] == 'M006':
            list_of_lines[linea] = list_of_lines[linea].replace('M006' ,nuevalinea) + '\n'
    a_file = open("myfile.txt", "w")
    a_file.writelines(list_of_lines)  
    a_file.close()

nuevo = input('ingrese porque cambiar')


modificar(lista, nuevo)

