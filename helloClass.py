class Carro:


    def __init__(self,marca,cilindrada,kilometraje):
        self.marca = marca
        self.cilindrada=cilindrada
        self.kilometraje=kilometraje

    def encender(self):
        self._iniciarMotor()
        print("Rum Rum")

    def _iniciarMotor(self):
        print("iniciando motor...")

carro=Carro("Subaru",1500,9000)
carro.encender()

print(f"marca 1:{carro.marca}")

carro=Carro("Mercedes",3000,10000)
carro.encender()
print(f"marca 2:{carro.marca}")
