
from archivo import fileOpen

codigos = fileOpen
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