from .modelos import Registro

class SistemaCRUD:
    def __init__(self):
        self.registros = []  # agregação: SistemaCRUD possui vários Registro
        self.id_counter = 1

    def criar_registro(self, nome, email, cpf, idade):
        # Verifica unicidade de email e cpf
        for r in self.registros:
            if r.email.lower() == email.lower():
                raise ValueError('Email já cadastrado!')
            if r.cpf == cpf:
                raise ValueError('CPF já cadastrado!')
        novo = Registro(self.id_counter, nome, email, cpf, idade)
        self.registros.append(novo)
        self.id_counter += 1
        return novo

    def listar_registros(self):
        return self.registros

    def atualizar_registro(self, id_registro, nome=None, email=None, cpf=None, idade=None):
        for r in self.registros:
            if r.id == id_registro:
                if nome:
                    r.nome = nome
                if email and all(r2.email.lower() != email.lower() or r2.id == id_registro for r2 in self.registros):
                    r.email = email
                elif email:
                    raise ValueError('Email já cadastrado!')
                if cpf and all(r2.cpf != cpf or r2.id == id_registro for r2 in self.registros):
                    r.cpf = cpf
                elif cpf:
                    raise ValueError('CPF já cadastrado!')
                if idade:
                    r.idade = idade
                return r
        raise ValueError('Registro não encontrado!')

    def deletar_registro(self, id_registro):
        for i, r in enumerate(self.registros):
            if r.id == id_registro:
                del self.registros[i]
                return True
        raise ValueError('Registro não encontrado!')
