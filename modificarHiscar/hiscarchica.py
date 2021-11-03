import datetime
count = 0
lista= []
fileNumber = 0
file1 = open('hiscar_2021_0.txt', 'r')
begin_time = datetime.datetime.now()
for file in file1:
    linea = "{}".format(file.strip())
    # filtrando los de 2021
    if linea[0:4] == '2021':
       linea = linea + '\n'
       lista.append(linea)
       count= count + 1
     
    
    if count > 1000:   
    #creando un nuevo archivo
        
        outFile = open("archivochico/hiscar_2021_{}.txt".format(fileNumber), "w")
        outFile.writelines(lista)
        outFile.close() 
        fileNumber= fileNumber + 1
        lista= []  
        count = 0

if count < 1000:
    outFile = open("archivochico/hiscar_2021_ultima.txt", "w")
    outFile.writelines(lista)
    outFile.close() 

    


