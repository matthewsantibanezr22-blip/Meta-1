if __name__ == "__main__":
    from holaMundo import Mensaje
    from ejercicio import OperacionesMatematicas
    from persona import Alumno
    from triangulo import Triangulo
    from rectangulo import Rectangulo
    from cuadrado import Cuadrado

    print("¡Hola! Este es el programa principal.")
    print("Selecciona la opcion que deseas ejecutar:")
    print("1. Imprimir mensaje")
    print("2. Operaciones Matematicas") 
    print("3. Calcular la edad de un alumno")
    print("4. Figuras Geometricas")

    opcion = int(input("Ingrese el número de la opción: "))

    if opcion == 1:
        mensaje = Mensaje("¡Hola Mundo, Ciencia de Datos!")
        mensaje.mostrar()

    elif opcion == 2:
        operaciones = OperacionesMatematicas()

        a=int(input("Ingrese el primer número: "))
        b=int(input("Ingrese el segundo número: "))
        
        print("Los resultados son:")
        print(a, "+", b, "=", operaciones.suma(a, b))
        print(a, "-", b, "=", operaciones.resta(a, b))
        print(a, "x", b, "=", operaciones.multiplicacion(a, b))
        print(a, "%", b, "=", operaciones.division(a, b))

    elif opcion == 3:        
        persona1 = Alumno("", 0, 0)

        persona1.nombre = input("Ingrese el nombre de la persona: ")
        persona1.anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
        persona1.edad = persona1.calcular_edad(persona1.anio_nacimiento, 2026)
        print(f"El alumno {persona1.nombre} tiene {persona1.edad} años.")

    elif opcion == 4:

        print("Selecciona una figura geométrica:")
        print("1. Triángulo")
        print("2. Rectángulo")
        print("3. Cuadrado")

        figura = int(input("Ingresa el número de la figura que deseas calcular: "))

        if figura == 1:
            calcular= Triangulo()
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))

            print("Área del triángulo:", calcular.area(base, altura))
            print("Perímetro del triángulo:", calcular.perimetro(base, altura))

        elif figura == 2:
            calcular= Rectangulo()
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))

            print("Área del rectángulo:", calcular.area(base, altura))
            print("Perímetro del rectángulo:", calcular.perimetro(base, altura))
        
        elif figura == 3:
            calcular= Cuadrado()
            lado = float(input("Ingresa el lado del cuadrado: "))

            print("Área del cuadrado:", calcular.area(lado))
            print("Perímetro del cuadrado:", calcular.perimetro(lado))
            
        else:
                print("Opción no válida. Por favor, selecciona una opción correcta.")  

    else:
        print("Opción no válida. Por favor, selecciona una opción correcta.")