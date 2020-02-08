import turtle

turtle.setup(600,600)

t = turtle.Pen()

t.hideturtle()

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(""))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Opcion 1 Traslación")
    print ("2. Opcion 2 Rotación")
    print ("3. Opcion 3 Escalamiento")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
    t.clear()
    if opcion == 1:
            
      
        
        print ("1.- Una línea")
        print ("2.- Un cuadrado")
        
        opciones = pedirNumeroEntero()
        t.clear()
        if opciones == 1:
                print("Linea")
                longitud = int(input("Longitud de la linea "))

                t.forward(longitud)
                x = int(input("Cambio en X "))
                y = int(input("Cambio en Y "))           
                t.penup()
                t.goto(x,y)
                t.pendown()
                t.color(0,0,1)
                t.forward(longitud)
                t.penup()
                t.goto(0,0)
                t.pendown()
                t.color(0,0,0)                           
        if opciones == 2:
                print("Cuadrado")
                longitudC = int(input("Longitud del cuadrado"))
                t.forward(longitudC)
                t.left(90)
                t.forward(longitudC)
                t.left(90)
                t.forward(longitudC)
                t.left(90)
                t.forward(longitudC)
                xC = int(input("Cambio en X "))
                yC = int(input("Cambio en Y "))
                t.penup()
                t.goto(xC,yC)
                t.pendown()
                t.color(0,0,1)
                t.backward(longitudC)
                t.right(90)
                t.backward(longitudC)
                t.right(90)
                t.backward(longitudC)
                t.right(90)
                t.backward(longitudC)
                t.penup()
                t.goto(0,0)
                t.pendown()
                t.color(0,0,0)
        
        print ("")    
    elif opcion == 2:
        print ("1.- Una línea")
        print ("2.- Un cuadrado")
        opciones2 = pedirNumeroEntero()
        t.clear()

        if opciones2 == 1:
                print("Linea")
                longitud = int(input("Longitud de la linea "))

                t.forward(longitud)
                Rotar = int(input("Rotación de grados: "))
                t.penup()
                t.goto(0,0)
                t.left(Rotar)
                t.color(1,0,1)
                t.pendown()
                t.forward(longitud)
                t.penup()
                t.right(Rotar)
                t.goto(0,0)
                t.pendown()
                t.color(0,0,0)
                                           
        if opciones2 == 2:
                print("Cuadrado")
                longitudC = int(input("Longitud del cuadrado"))
                t.forward(longitudC)
                t.left(90)
                t.forward(longitudC)
                t.left(90)
                t.forward(longitudC)
                t.left(90)
                t.forward(longitudC)
                RotarC = int(input("Rotación de grados: "))
                t.penup()
                t.goto(0,0)
                t.left(RotarC)
                t.color(1,0,1)
                t.pendown()
                t.backward(longitudC)
                t.right(90)
                t.backward(longitudC)
                t.right(90)
                t.backward(longitudC)
                t.right(90)
                t.backward(longitudC)
                t.penup()
                t.right(RotarC)
                t.goto(0,0)
                t.pendown()
                t.color(0,0,0)
        print ("")    
                 
    elif opcion == 3:
        print ("1.- Una línea")
        print ("2.- Un cuadrado")
        opciones3 = pedirNumeroEntero()
        t.clear()
        
        if opciones3 == 1:
                print("Linea")
                longitud = float(input("Longitud de la linea "))

                t.forward(longitud)
                Escala = float(input("Cambio de escala "))
                t.penup()
                t.goto(0,0)
                t.pendown()
                t.color(1,0,0)
                t.forward(longitud*Escala)
                t.penup()
                t.goto(0,0)
                t.pendown()
                t.color(0,0,0)
                                           
        if opciones3 == 2:
                print("Cuadrado")
                longitudC = int(input("Longitud del cuadrado"))
                t.forward(longitudC)
                t.left(90)
                t.forward(longitudC)
                t.left(90)
                t.forward(longitudC)
                t.left(90)
                t.forward(longitudC)
                EscalaC = float(input("Cambio de escala "))
                t.penup()
                t.goto(0,0)
                t.color(1,0,0)
                t.pendown()
                t.backward(longitudC*EscalaC)
                t.right(90)
                t.backward(longitudC*EscalaC)
                t.right(90)
                t.backward(longitudC*EscalaC)
                t.right(90)
                t.backward(longitudC*EscalaC)
                t.penup()
                t.goto(0,0)
                t.pendown()
                t.color(0,0,0)
        print ("")     
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
