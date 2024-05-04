from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nasc_formatada = self._data_nascimento.split('/')
        ano_nasc = data_nasc_formatada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nasc)

    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_quebado = nome_completo.split(' ')
        return nome_quebado[-1]

    def _e_socio(self):
        sobrenomes = [
            'Bragança',
            'Windsor',
            'Bourbon',
            'Yamato',
            'Al Saud',
            'Khan',
            'Tudor',
            'Ptolomeu',
        ]
        return self._salario >= 100_000 and (self.sobrenome() in sobrenomes)

    def decrescimo_salario(self):
        if self._e_socio():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("O salário é muito alto para receber bônus.")
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
