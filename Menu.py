print ("bienvenido al menu de la calculadora") 
def calcualdora():
        print("digite 1 si desea sumar")
        print("digite 2 si desea restar")
        print("digite 3 si desea multiplicacion")
        print("digite 4 se desea dividir")
opcion = (input ("Escoja una opcion: "))
if opcion in ["1","2"."3","4"]:
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

            
            
