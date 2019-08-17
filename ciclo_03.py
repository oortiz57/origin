respuesta = 'SI'
while respuesta == 'SI':
    a = input ("introduzca el 1er valor:")
    b = input ("introduzca el 2do valor:")
    c = float(a) + float(b)
    print ("la suma de ",a,"mas ",b, "es: ", c)
    respuesta = input ("desea continuar? (SI/NO):")
print ("fin")