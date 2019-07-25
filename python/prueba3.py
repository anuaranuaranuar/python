num1=int(input("digite 1er numero: "))
num2=int(input("digite 2do numero: "))
op=int(input("digite tipo de operacion 1:suma, 2:resta, 3:multiplicar, 4:dividir"))

if op==1:
    print("la suma es: ", (num1+num2))
elif op==2:
    print("la resta es: ", (num1-num2))
elif op==3:
    print("la multiplicacion es: ", (num1*num2))
elif op==4:
    print("la division es: ", (num1/num2))
else:
    print("por favor digite un valor correcto para la operacion")
