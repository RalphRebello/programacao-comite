class Veiculo:
    def acelerar(self):
        pass


class Motos(Veiculo):
    def __init__(self, modelo):
        self.modelo = modelo

    def acelerar(self):
        print('Acelerando MOTO!')


moto1 = Motos('Twister')
moto1.acelerar()
# type(moto1)
