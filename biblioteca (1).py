class Pessoa:

    def __init__(self, nome, peso, idade,falando = False, comendo = False, dormindo = False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo
        self.falando=falando
        self.dormindo=dormindo
    def comer(self):
        self.comendo == True
        if self.comendo == True:
            print(f"{self.nome} ainda está comendo")
        elif self.falando == True:
            print(f"{self.nome} não pode falar pois está comendo")
        elif self.dormindo == True:
            print(f"{self.nome} não pode dormir pois está dormindo")
        else:
            comida = input("Está comendo oque?: ")
            print(f"{self.nome} Começou a comer {comida}")
            self.comendo = True
    def falar(self):
        if self.falando == True:
            print(f"{self.nome} parou de falar")
        elif self.comendo == True:
            print(f"{self.nome} não pode falar pois está comendo")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar pois esta dormindo")
        else:
            print("Começou a falar")
            self.falando == True

    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} parou de dormir")
        elif self.falando == True:
            print(f"{self.nome} não pode dormir pois esta falando")
        elif self.comendo == True:
            print(f"{self.nome} não pode dormir pois está comendo")
        else:
            print("Começou a dormir")
            self.dormindo == True

    def apresentar(self):
        print(f"Olá meu nome é {self.nome} tenho {self.idade} anos e peso {self.peso}")


    def parar_dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} acordou")
            self.dormindo = False
        else:
            print(f"{self.nome} não está dormindo")
    def parar_comer(self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer")
            self.comendo = False
        else:
            print(f"{self.nome} não está comendo")

    def parar_falar(self):
        if self.falando == True:
            print(f"{self.nome} parou de falar")
            self.falando = False
        else:
            print(f"{self.nome} não está falando")