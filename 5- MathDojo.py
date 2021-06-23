import statistics

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        # tu código aquí
        self.result = self.result + num
        for n in nums:
            #print(v)
            self.result = self.result + n
        return self
    def subtract(self, num, *nums):
        self.result = self.result - num
        for n in nums:
            #print(v)
            self.result = self.result - n
        return self
    
md = MathDojo()
# para probar:
#x = md.add(200).add(2, 5, 10).add(33,12,7).result
#x = md.subtract(9).subtract(2, 50, 1).subtract(3,1,15).result

x = md.add(2).add(2, 5, 10).subtract(3, 2).result
print("El resultado es",x)  # debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!

d= statistics.pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
print("La Desviacion Estandar es:",d)

