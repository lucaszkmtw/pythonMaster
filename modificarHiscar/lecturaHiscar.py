import datetime
zise = 1000000
cantidad = 1
begin_time = datetime.datetime.now()
file1 = open('HISCARLARGA.2021-Aug-02.115001', 'r')
count = 0
for file in file1:
    count = count + 1
    
    if count > zise:
        
        hiscar = zise * cantidad
        tiempo= datetime.datetime.now() - begin_time
        print("tiempo en leer",hiscar, "hiscar: ", tiempo)
        cantidad = cantidad +1
        
        count = 0
file1.close()

