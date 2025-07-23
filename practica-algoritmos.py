edad_cliente = int(input('Por favor ingrese su edad: '))

permitido = True if edad_cliente >= 18 else False #Ternario
'''
if edad_cliente >= 18:
    permitido = True
else:
    permitido = False
'''
if permitido:
    print('¡Puedes ingresar a la discoteca!')
else:
    print('Lo sentimos mucho, no puedes ingresar a la discteca')