class Conta:
    _tipo_de_conta = "corrente"
    __id_interno = 985645

    def __init__(self, cliente):
        print(self)
        self.cliente = cliente
        self._saldo = 0

    @property  # getter
    def saldo(self):
        if self._saldo < 0:
            print("AVISO: Você está devendo")
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo += value

    @saldo.deleter
    def saldo(self):
        self._saldo = 0


conta = Conta(cliente="Felipe")
conta.saldo = 100
conta.saldo = -10
print(conta.saldo)
del conta.saldo
print(conta.saldo)
