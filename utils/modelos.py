class Pessoa:
    def __init__(self, nome, email, cpf, idade):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.idade = idade

class Registro(Pessoa):
    def __init__(self, id_registro, nome, email, cpf, idade):
        super().__init__(nome, email, cpf, idade)
        self.id = id_registro
