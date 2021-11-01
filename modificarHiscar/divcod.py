from archivo import fileOpen
codigo = {
    'reparticion': {'dd':0, 'ht': 4},
    'cargo': {'dd':4, 'ht': 8},
    'basico': {'dd':9, 'ht': 16},
    }

codigos = fileOpen()
cargos =[]
reparticion= []
basico = []

for x in codigos:
    reparticion.append(x[0:4])
    cargos.append(x[4:8])
    basico.append(x[8:15])

for cod in range(0, len(codigos)):
    print(reparticion[cod],cargos[cod] , basico[cod])
    