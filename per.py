class Persona:  #Clase persona
    def __init__(self, nom, cate, hx, tar):
        self.nom = nom
        self.cate = cate
        self.hx = float(hx)
        self.tar = float(tar)
    def sueldo_basico(self): #Obtener sueldo basico a base de la categoria
        ca, cb, cc = 3000, 2500, 2000
        if self.cate == "A" or self.cate =="a":
            return ca # return acba la funcion y  el atributo se queda con el valor de la funcion
        elif self.cate == "B" or self.cate =="b":
            return cb
        else:
            return cc 
    def pago_hora(self): #obtener el pago por hora la formula es: ph= sueldo_basico / 240
        return self.sueldo_basico()/240
    def pago_min(self):
        return self.pago_hora()/60 #convertimos el pago de hora en minutos
    def descuento(self):
        return self.pago_min() * self.tar 
    def sueldo_neto(self):
        return (self.sueldo_basico() + self.pago_extra()) - self.descuento()
    def pago_extra(self):
        return self.pago_hora() * self.hx