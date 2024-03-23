
a= 'A LAS ENTIDADES FINANCIERAS:  Ref.: Circular  REMON 1-1103:  Notas del Banco Central de la República Argentina en dólares estadounidenses con opción de rescate para importadores de bienes y servicios pendientes de pago – Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) Nos dirigimos a Uds. para comunicarles que el Banco Central de la República Argentina podrá ofrecer al mercado Notas del Banco Central de la República Argentina en dólares estadounidenses con opción de rescate para importadores de bienes y servicios pendientes de pago, de acuerdo con el siguiente detalle:  Suscriptores: podrán participar en las suscripciones de estos instrumentos sólo importadores de bienes y servicios por hasta las importaciones que tengan pendientes de pago.  Plazo máximo: hasta el 31 de octubre de 2027.  Moneda de suscripción:  pesos al tipo de cambio de referencia publicado por el BCRA en función de la Comunicación "A" 3500 correspondiente al día hábil previo a la fecha de licitación.  Moneda de pago:  dólar estadounidense a la amortización y/o con opción/es de rescate anticipado en favor de los Titulares. La cancelación de dicho ejercicio de opción solo podrá ser en pesos dollar linked.  Amortización: dólar estadounidense, con la posibilidad de amortización íntegra al vencimiento o con esquema de amortizaciones parciales según se defina oportunamente.  Opción de rescate a favor del inversor: se podrá considerar la alternativa de incluir cláusulas de rescate anticipado en favor de los Titulares. En ese caso, de manera simultánea a la licitación del título se incluirán derechos de rescate sobre dichos instrumentos en los plazos y en las proporciones que defina oportunamente el BCRA, los cuales solo podrán ser ejercidos a valor nominal pagadero en pesos a Tipo de Cambio de Referencia de la Comunicación “A” 3500. Para viabilizar las opciones de rescate en favor del inversor se prevé un strip de dichas proporciones del total nominal un mes antes de cada fecha de ejercicio de opción. Estos strips pagarán dólares estadounidenses al vencimiento o pueden ejecutarse contra pesos dollar linked al BCRA en la fecha establecida de la opción de rescate. Si el tenedor decidiese ejercer la opción de rescate, deberá informar con una antelación de 5 días hábiles previos al vencimiento de dicha opción.  Intereses: Devengarán intereses sobre la base de un año de TRESCIENTOS SESENTA (360) días integrado por DOCE (12) meses de TREINTA (30) días cada uno, a una tasa anual máxima del 5% a definir en el anuncio de la licitación, que podrá ser pagadera en forma trimestral o semestral en dólares estadounidenses.  Subastas: precio único o múltiple.  Agente de liquidación y registro: CRyL.   -2-     Integración de la suscripción y el pago de los servicios financieros: se efectuará mediante el débito o crédito según corresponda de la cuenta de la entidad financiera en este Banco Central.  Mercado secundario: en el anuncio de la subasta se definirá si estos instrumentos se negociarán o no en los ámbitos de BYMA/MAE, y mercados euroclearables. Al igual de que si podrán o no ser utilizadas como colaterales para operaciones de REPO.  Saludamos a Uds. atentamente.   BANCO CENTRAL DE LA REPÚBLICA ARGENTINA      María Florencia Schuster Diego J. López Airaghi Gerenta de Análisis de Operaciones Gerente Ppal. de Operaciones de Mercado'

a = a.lower()

b = a.split()

c= {}
'''
for palabra in b:
    if palabra in c:
        c[palabra] += 1
    else:
        c[palabra] = 1
'''

for palabra in b:
    c[palabra] = c.get(palabra, 0) +1

ordenada = dict(sorted(c.items(), key=lambda x: x[1], reverse= True))

#print(ordenada)


lista_ordenada = [f'{k} = {v}\n' for k, v in ordenada.items()]

'''string = ''

for item in lista_ordenada:
    string += item
'''

string = ''.join(lista_ordenada)

print(string)




'''
a1 = c.pop('de')
a2 = c.pop('la')
a3 = c.pop('en')
a4 = c.pop('a')
'''
'''max_value = max(c.values())

print('Max value is: ' ,max_value)


mmmm = {}

for key, value in c.items():
    if value == max_value:
        mmmm[key] = value
    
print(mmmm)
x = {}

m = []
'''
'''m = 0

for val in c.values():
    if val > m:
        m = val
        
print(m)
    
max_value= {}

for k, v in c.items:
    if v == m:
        max_value[k] = v
        
print(max_value)

'''
