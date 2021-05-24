class Cuenta:
	def __init__(self,titular,cantidad):
		self.titular=titular
		self.cantidad=cantidad
 
	def imprimir(self):
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)
 
 
class Caja(Cuenta):
	def __init__(self,titular,cantidad):
		super().__init__(titular,cantidad)
 
	def print(self):
		print("Cuenta de caja de ahorros")
		super().imprimir()
 
 

class Plazo(Cuenta):
	def __init__(self,titular,cantidad,plazo,interes):
		super().__init__(titular,cantidad)
		self.plazo=plazo
		self.interes=interes
 
 
	def ganancia(self):
		ganancia=self.cantidad*self.interes/100
		print("El importe de interés es: ",ganancia)
 
 
	def print(self):
		print("Cuenta a plazo fijo")
		super().imprimir()
		print("Plazo disponible en días: ",self.plazo)
		print("Interés: ",self.interes)
		self.ganancia()
 
a=(input(print("¿Cual es el nombre de esta persona?")))
b=int(input(print("¿Cuanto dinero tiene esta persona?")))
c=int(input(print("¿Cuantos dias estara el plazo?")))
d=float(input(print("¿Cual es el porcentaje del interes?")))
caja1=Caja(a,b)
caja1.print()
 
plazo1=Plazo(a,b,c,d)
plazo1.print()
