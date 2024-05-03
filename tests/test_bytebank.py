from codigo.bytebank import Funcionario


# O metodo tem que comecar com test_ e tem que ser verboso
class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_24(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 24

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_Leonardo_Coelho_deve_retornar_Coelho(self):
        entrada = 'Leonardo Chinelato Coelho'  # Given
        esperado = 'Coelho'

        leonardo = Funcionario(entrada, '08/06/2002', 1111)
        resultado = leonardo.sobrenome()  # When

        assert resultado == esperado  # Then

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100_000  # Given
        entrada_nome = 'Paulo Bragança'
        esperado = 90_000

        funcionario_teste = Funcionario(entrada_nome, '08/06/2002', entrada_salario)
        funcionario_teste.decrescimo_salario()  # When
        resultado = funcionario_teste.salario
        assert resultado == esperado  # Then
