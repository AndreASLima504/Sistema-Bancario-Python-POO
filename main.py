from abc import ABC, abstractmethod
import uuid

class Historico:
    def init(self, historico=None):
        self._historico = historico

    def adicionar_transacao(transacao):
        pass


class Conta:
    def __init__(self, numero, cliente) -> None:
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico("Conta inicializada")


    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> str:
        return self.numero
    
    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    

    def sacar(self, valor):
        if self._saldo == 0.0:
            print("Você não tem saldo para fazer saques")
            return False
        elif self.saldo < valor:
            print("Você não tem saldo suficiente para esse saque")
            return False
        elif self._saldo >= valor:
            self._saldo -= valor
            print("Saque realizado!")
            return True
        else:
            print("Você não tem saldo para fazer saques")
            return False


    def depositar(self, valor):
        pass
        
    


class ContaCorrente(Conta):
    def __init__(self, limite, limite_saque) -> None:
        self._limite = limite
        self._limite_saque = limite_saque



class Cliente:
    def __init__(self, endereco) -> None:
        self._endereco = endereco
        self._contas = []
    

    def registrar_transacao(self, conta, transacao):
        transacao.registrar(conta)


    def adicionar_conta(self, conta):
        conta = ContaCorrente.nova_conta(self, str(uuid.uuid4()))
        self._contas.append(conta)
        



class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco) -> None:
        super().__init__(endereco)
        self._cpf = cpf
        self.nome = nome
        self._data_nascimento = data_nascimento



class Transacao(ABC):
    @abstractmethod
    def registrar(conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor

    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor

    def registrar(self, conta):
        pass

