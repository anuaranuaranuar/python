edad=int (input("digite edad"))
genero= input("Digite sexo, h hombre, m mujer") 
if edad>=18:
    if genero in 'Hh':
        print("Señor, usted es mayor de edad")
    elif  genero in 'Mm':
        print("Señorita, usted es mayor de edad")
    else:
        print("dto inocrrecto")

else:
    if genero in 'Mm':
        print('Señorita, Usted es menor de edad')
    elif genero in 'Hh':
        print("señor, usted es menor de edad")
    else:
        print("dato, incorrecto")
