# Opening file
def fileOpen():  
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
    return lista



