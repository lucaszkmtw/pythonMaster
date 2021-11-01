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