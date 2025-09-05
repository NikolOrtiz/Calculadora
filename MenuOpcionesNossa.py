def calcualdora():
     print("3.multiplicacion")
     print("4.division")
opcion = (input ("Escoja una opcion: "))
if opcion in ["3","4"]:
        if opcion == "3":
             
            num1=float(input("ingrese su primer numero: "))
            num2=float(input("ingrese su segundo numero: "))           
            operacion = num1*num2
            print("el resultado de la multiplicacion es : ", operacion)
    
        if opcion == "4":
            num1=float(input("ingrese su primer numero: "))
            num2=float(input("ingrese su segundo numero: "))
            operacion = num1 / num2
            print("el resultado de la divion es : ", operacion)

print("Fin del proceso gracias por usar la calculadora")

            
            