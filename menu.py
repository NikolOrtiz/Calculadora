def calcualdora():
     print("1.Suma")
     print("2.Resta")
opcion = (input ("Escoja una opcion: "))
if opcion in ["1","2"]:
        if opcion == "1":
             
            num1=float(input("ingrese su primer numero: "))
            num2=float(input("ingrese su segundo numero: "))           
            operacion = num1+num2
            print("el resultado de la suma es : ", operacion)
    
        if opcion == "2":
            num1=float(input("ingrese su primer numero: "))
            num2=float(input("ingrese su segundo numero: "))
            operacion = num1 - num2
            print("el resultado de la resta es : ", operacion)

print("Fin del proceso gracias por usar la calculadora")