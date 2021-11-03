import datetime
begin_time = datetime.datetime.now()
count = 0
lista= []
fileNumber = 0
file1 = open('HISCARLARGA.2021-Aug-02.115001', 'r')

for file in file1:
    linea = "{}".format(file.strip())
    # filtrando los de 2021
    if linea[0:4] == '2021' and linea[6]== 'M':
       linea = linea + '\n'
       lista.append(linea)
       count= count + 1
     
    
    if count > 399999:   
    #creando un nuevo archivo
        
        outFile = open("MUNICIPIO2021/hiscarMUN_{}.txt".format(fileNumber), "w")
        outFile.writelines(lista)
        outFile.close() 
        fileNumber= fileNumber + 1
        lista= []  
        hiscar= count * fileNumber
        tiempo= datetime.datetime.now() - begin_time
        print("tiempo en leer",hiscar, "hiscar: ", tiempo)
        count = 0
    #fin for
if count < 399999:
    outFile = open("MUNICIPIO2021/hiscarMUN_ultima.txt", "w")
    outFile.writelines(lista)
    tiempo= datetime.datetime.now() - begin_time
    print("proceso finalizado en : " ,tiempo)
    outFile.close() 
    #creando el archivo final , donde esta el remanente

    


