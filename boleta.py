from per import Persona
class Boleta(Persona):
    def __init__(self):
        print("****DATOS DE ENTRADA****")
        nombre = input("NOMBRE: ") #hacemos entrda de datos desde teclado
        categoria = input("CATEGORIA: ")
        horas = input("HORAS EXTRA: ")
        tardanza = input("TARDANZA: (min)")
        Persona.__init__(self, nombre, categoria, horas, tardanza) #los atributos de la clase boleta pasa a la clase persona
    def boleta(self):
        print("****DATOS DE BOLETA ****")
        print("NOMBRE: ", self.nom)
        print("CATEGORIA: ", self.cate)
        print("SUELDO BASICO: ", self.sueldo_basico())
        print("DESCUENTO DE TARDANZAS: ", self.descuento())
        print("PAGO HORAS EXTRAS: ", self.pago_extra())
        print("SUELDO NETO: ", self.sueldo_neto())
prueba1 = Boleta()
prueba1.boleta()