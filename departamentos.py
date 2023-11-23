#crear una clase departamento para complementar la clase empleados
#la clase departamento deberá tener dos atributos: nombre departamento y una lista con empleados
#Además deberá agregar dos métodos de instancia: agregar empleado y mostrar empelados
#Luego, agregar un método de clase que pueda crear un nuevo departamento y un método
#estático que calcule el salario promedio en un departamento 

from empleados import *

class Departamento:
    def __init__(self, nombre) :
        self.nombre = nombre
        self.empleados = []
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    #método mostrar empleados
    def mostrar_empleados(self):
        print(f'Empleados en el departamento: {self.nombre}: \n')
        for empleado in self.empleados:
            print(f'- {empleado.nombre}')
    @classmethod
    def crear_departamento(cls, nombre):
        return cls(nombre)
    
#CRear departamento
departamento_ti = Departamento('TI')

#Asociar empleado a un departamento existente
departamento_ti.agregar_empleado(empleado1)
departamento_ti.agregar_empleado(empleado2)
departamento_ti.agregar_empleado(empleado3)

departamento_ti.mostrar_empleados()

#crear departamento con método de clase
departamento_hr =  Departamento.crear_departamento('Recursos humanos')