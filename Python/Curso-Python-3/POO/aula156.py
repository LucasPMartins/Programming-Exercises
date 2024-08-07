# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

@dataclass(frozen=True) # (init=False) serve para desativar metodos e configurações
class Pessoa:
    nome: str
    sobrenome: str
    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self): # Com a def de init o post_init não é executado
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # # @property
    # # def nome_completo(self):
    # #     return f'{self.nome} {self.sobrenome}'

    # # @nome_completo.setter
    # # def nome_completo(self, valor: str):
    # #     nome, *sobrenome = valor.split()
    # #     self.nome = nome
    # #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Lucas', 'Martins')
    # p1.nome_completo = 'Maria Helena'
    # p1.nome = 'Tiago' não é possivel quando @dataclass(frozen=True)
    print(p1)
    # print(p1.nome_completo)
