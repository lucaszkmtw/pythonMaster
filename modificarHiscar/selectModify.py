from archivo import fileOpen



codigo = {
    'reparticion': {'dd':0, 'ht': 3},
    'cargo': {'dd':4, 'ht': 8},
    'basico': {'dd':9, 'ht': 16},
    }

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

#busqueda= input('ingrese el cargo :  ')

#visualizar(busqueda,cargos,codigos)

viejo = input('que cargo modifico')
nuevo = input(' porque lo modifico')
modificar(codigos, viejo, nuevo)