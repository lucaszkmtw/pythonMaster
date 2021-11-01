from archivo import fileOpen
codigos = fileOpen()

cargos =[]
reparticion= []
basico = []

for x in codigos:
    reparticion.append(x[0:3])
    cargos.append(x[4:8])
    basico.append(x[9:16])


def visualizar(buscar, cargo,  cod):
    existe= None
    count = 0
    for x in cod:
        if buscar == cargo[count]:
            existe = cargo[count]
        count = count +1 
    if cargo == None:
        print('no existe')
    else:
        print('el cargo ', existe, ' existe')
    return existe

def modificar(lineas, vie, act):
    lista_nueva = []
    vie.split()
    act.split()
    for linea in range(0, len(lineas)):
        lineas[linea] = lineas[linea].replace(vie.upper() ,nuevo.upper()).upper() + '\n'
     
        
        lista_nueva.append(lineas[linea])
    
    a_file = open("myfile.txt", "w")
    a_file.writelines(lista_nueva)  
    a_file.close()
viejo = input('que cargo modifico')
nuevo = input(' porque lo modifico')
modificar(codigos, viejo, nuevo)
#manjear keys en dicccionario
#attr = linea[pos['dd']:pos['ht']]
