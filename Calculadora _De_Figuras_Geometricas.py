import math


def main():
    # Função principal aonde o usuário escolhe qual figura geométrica deseja realizar os cálculos.
    opcao = True

    while opcao:
        print("""
        1 - Triângulo    3 - Retãngulo
        2 - Quadrado     4 - Círculo
        """)

        poligono = str(input("Digite qual fígura geométrica deseja calcular: "))

        # Dependendo da escolha do usuário a função chama as classes para realisar os cálculos.
        # Depois retorna os valores calculados para o visualização do usuário.
        if poligono == "1":
            triangulo = Triangulo()
            triangulo.imprimir_calculos()
            opcao = False
        elif poligono == "2":
            quadrado = Quadrado()
            quadrado.imprimir_calculos()
            opcao = False
        elif poligono == "3":
            retangulo = Retangulo()
            retangulo.imprimir_calculos()
            opcao = False
        elif poligono == "4":
            circulo = Circulo()
            circulo.imprimir_calculos()
            opcao = False
        else:
            print("Opção inválida, digíte o número correspondente a figura que deseja calcular!")
            opcao = True


class Triangulo:

    def __init__(self):
        self.lado_1 = float(input("Digíte o valor do 1° lado do triângulo: "))
        self.lado_2 = float(input("Digíte o valor do 2° lado do triângulo: "))
        self.lado_3 = float(input("Digíte o valor do 3° lado do triângulo: "))

    def calcular_perimetro(self):
        return self.lado_1 + self.lado_2 + self.lado_3

    def calcular_area(self):
        # Cáculo para Triângulo equilátero.
        if self.lado_1 == self.lado_2 and self.lado_1 == self.lado_3:
            return ((self.lado_1 * self.lado_1) * math.sqrt(3)) / 4
        # Cáculo para Triângulo escaleno.
        elif self.lado_1 != self.lado_2 and self.lado_1 != self.lado_3 and self.lado_2 != self.lado_3:
            semiperimetro = (self.lado_1 + self.lado_2 + self.lado_3) / 2
            return math.sqrt(semiperimetro * (semiperimetro - self.lado_1) *
                             (semiperimetro - self.lado_2) * (semiperimetro - self.lado_3))
        # Cáculo para Triângulo isósceles.
        else:
            if self.lado_1 == self.lado_2:
                base = self.lado_3
                lado = self.lado_1
                altura = math.sqrt((lado * lado) - ((base / 2) * (base / 2)))
                return (base * altura) / 2
            elif self.lado_1 == self.lado_3:
                base = self.lado_2
                lado = self.lado_1
                altura = math.sqrt((lado * lado) - ((base / 2) * (base / 2)))
                return (base * altura) / 2
            elif self.lado_2 == self.lado_3:
                base = self.lado_1
                lado = self.lado_2
                altura = math.sqrt((lado * lado) - ((base / 2) * (base / 2)))
                return (base * altura) / 2

    def imprimir_calculos(self):
        # 1° Forma de chamar um método dentro de uma classe.
        return print(f"O perímetro do triângulo é: {self.calcular_perimetro()}\n",
                     # 2° Forma de chamar um método dentro de uma classe.
                     f"A área do triângulo é: {Triangulo.calcular_area(self)}", sep="")


class Quadrado:

    def __init__(self):
        self.lado = float(input("Digíte o valor de um lado do quadrado: "))

    def calcular_perimetro(self):
        return self.lado * 4

    def calcular_area(self):
        return self.lado * 2

    def imprimir_calculos(self):
        # 1° Forma de chamar um método dentro de uma classe.
        return print(f"O perímetro do quadrado é: {self.calcular_perimetro()}\n",
                     # 2° Forma de chamar um método dentro de uma classe.
                     f"A área do quadrado é: {Quadrado.calcular_area(self)}", sep="")


class Retangulo:

    def __init__(self):
        self.lado_1 = float(input("Digíte o valor do 1° lado do retângulo: "))
        self.lado_2 = float(input("Digíte o valor do 2° lado do retângulo: "))

    def calcular_perimetro(self):
        return self.lado_1 * 2 + self.lado_2 * 2

    def calcular_area(self):
        return self.lado_1 * self.lado_2

    def imprimir_calculos(self):
        # 1° Forma de chamar um método dentro de uma classe.
        return print(f"O perímetro do retângulo é: {self.calcular_perimetro()}\n",
                     # 2° Forma de chamar um método dentro de uma classe.
                     f"A área do retângulo é: {Retangulo.calcular_area(self)}", sep="")


class Circulo:

    def __init__(self):
        self.raio = float(input("Digíte o valor do raio do Circulo: "))

    def calcular_perimetro(self):
        return self.raio * 2 * 3.14

    def calcular_area(self):
        return self.raio * self.raio * 3.14

    def imprimir_calculos(self):
        # 1° Forma de chamar um método dentro de uma classe.
        return print(f"O perímetro do círculo é: {self.calcular_perimetro()}\n",
                     # 2° Forma de chamar um método dentro de uma classe.
                     f"A área do Circulo é: {Circulo.calcular_area(self)}", sep="")


if __name__ == "__main__":
    main()
