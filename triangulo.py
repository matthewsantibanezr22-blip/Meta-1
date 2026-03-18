class Triangulo:   
    def area(self, base, altura):
        return (base * altura) / 2

    def perimetro(self, base, altura):
        return base + altura + (base ** 2 + altura ** 2) ** 0.5