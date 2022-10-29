import math
def mate():
    contador_c = 0
    contador_i = 0
    mensaje = ("Las preguntas incorrectas fueron: ")
    
    r1= float(input("1. Obtén la hipotenusa de un triángulo rectángulo con lado a = 23 cm y b= 18 cm (deje a una decimal): "))
    if r1 == round (math.sqrt(23**2 + 18**2),1):
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "1, "
        print("Incorrecto")
        
    r2= float(input("2. Un círculo tiene un diámetro de 16 cm. Calcula el perímetro de esta figura (deje a una decimal): "))
    if r2 == round(math.pi*16,1):
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "2, "
        print("Incorrecto")
        
    r3= float(input("3.Utilizando el problema anterior, calcule el área del círculo (deje a una decimal): "))
    if r3 == round(math.pi*(16/2)**2,1):
        contador_c = contador_c + 1
        print("Correcto")
    
    else:
        mensaje = mensaje + "3, "
        print("Incorrecto")
        
    r4=  int(input("4. Redondea 569.04958 a tres cifras significativas: "))
    if r4 == 569 :
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "4, "
        print("Incorrecto")
        
    r5= int(input("5. Halle el complemento de 49°: "))
    if r5 == (90-49):
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "5, "
        print("Incorrecto")
        
    r6= int(input("6.Halle el suplemento de 126°: "))
    if r6 == (180-126):
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "6, "
        print("Incorrecto")
    
    r7= int(input("7.Observe la siguiente sucesión numérica: 2, 4, 16, 256, 65536,__. Encuentre la sexta posición: "))
    if r7 == 65536**2:
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "7, "
        print("Incorrecto")
        
    r8= int(input("8.Calcule pi radianes en grados: "))
    if r8 == math.degrees(math.pi):
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "8, "
        print("Incorrecto")
        
    r9= int(input("9.Marcelo tiene 4 pantalones, 2 pares de zapatos y 3 camisas. ¿De cuántas maneras se puede vestir? : "))
    if r9 == 4*2*3:
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "9, "
        print("Incorrecto")
    
    r10= int(input("10.Redondea a la milésima el número 2656565: "))
    if r10 ==2657:
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "10, "
        print("Incorrecto")
    
    r11= input("11.Se lanza simultáneamente una moneda y un dado. Calcule la probabilidad de obtener cara y un número par: ")
    if r11 == "3/12":
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "11, "
        print("Incorrecto")
        
    r12= input("12.Se lanzan dos dados al mismo tiempo. Calcule la probabilidad de que la suma de ambos sea 8: ")
    if r12 == "5/36":
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "12, "
        print("Incorrecto")
        
    
    suma=0
    for x in range(100,0,-2):
        x=x-95
        suma=suma+x
    r13 = int(input("13.Indique la suma de los 50 primeros números de la siguiente sucesión. 5, 3, 1, -1 , -3, -5: "))
    if r13 == suma:
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "13, "
        print("Incorrecto")
    
    r14 = float(input("14.Las calificaciones de 7 alumnos fueron las siguientes: 95, 89, 75, 100, 77, 89, 93: Calcule la media (deje una decimal): ")) 
    calif=[95,89,75,100,77,89,93]
    if r14 == round((sum(calif)/len(calif)),1):
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "14, "
        print("Incorrecto")
    
    r15 = int(input("15.Utilizando los datos del problema 14, obtenga la mediana: "))
    calif.sort()
    mediana=calif[3]
    if r15 == mediana:
        contador_c = contador_c + 1
        print("Correcto")
    else:
        mensaje = mensaje + "15"
        print("Incorrecto")
    
    print ('Sacaste ' + str(contador_c) + ' respuestas correctas')
    print (mensaje)



mate()