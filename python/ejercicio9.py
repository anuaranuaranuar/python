class Empleado:
    def __init__(self):
        self.codigo=""
        self.nombres=""
        self.apellidos=""
        self.salario_base=""

        
    def retencion (self):
        total=(self.salario_base*0.1)
        return total

        
    def datos(self):
        Dato=self.nombres+" "+self.apellidos+" ",self.codigo
        return Datos

    
    def salarioneto (self):
        if(self.salariobase <=828116):
            N=(self.salario_base+97032)-(self.salario_base*0.1)
        else:
            N=(self.salario_base)-(self.salario_base*0.1)
            return N

        
emp=Empleado()
emp.codigo=float(input("Ingrese el codigo "))
emp.nombres=input("Ingrese su nombre ")
emp.apellidos=input("Ingrese su apellido ")
emp.salariobase=float(input("Ingrese su salario base "))
print(emp.retencion())
print(emp.salarioneto())
print(emp.datos())


