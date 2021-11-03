
count = 0
lista= []
fileNumber = 0
file1 = open('myfile.txt', 'r')

for file in file1:
    linea = "{}".format(file.strip())
    if linea[4] == 'S':

        linea = linea + '\n'
        lista.append(linea)
        count= count + 1
    ultimo = 1
    if count > 99:   
    #creando un nuevo archivo
        ultimo = 0 
        outFile = open("archivos/archivo_jerarquizado{}.txt".format(fileNumber), "w")
        outFile.writelines(lista)
        outFile.close() 
        fileNumber= fileNumber + 1
        lista= []  
        count = 0
    if count < 99 and ultimo == 1:
        outFile = open("archivos/archivo_jerarquizado{}.txt".format(fileNumber), "w")
        outFile.writelines(lista)
        outFile.close() 

    


