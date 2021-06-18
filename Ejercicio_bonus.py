class Caja:
    def __init__(self,largo,ancho,alto,costo=30):
        self.largo= largo
        self.ancho= ancho
        self.alto=  alto
        self.costo = costo
    
    def tamCaja(self):
        return (self.largo * self.ancho * self.alto)


    def ObtenerPrecio(self):
        tam = self.tamCaja()
        return tam * self.costo



caja1= Caja(5,2,8)

print("El  volumen de la caja es:" , caja1.tamCaja(),"cm, y su precio es de:" , caja1.ObtenerPrecio(),"pesos")