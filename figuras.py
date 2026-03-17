class Triangulo:

    def area(self, base, altura):   
        return (base * altura) / 2
    
    def perimetro(self, base, altura):
        return altura * altura + base
    
class Rectangulo:

    def area(self, base, altura):
        return base * altura
    
    def perimetro(self, base, altura):
        return 2 * (base + altura)
    
class Cuadrado:

    def area(self, lado):
        return lado * lado
    
    def perimetro(self, lado):
        return 4 * lado