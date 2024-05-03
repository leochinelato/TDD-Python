from bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('teste','16/07/2002', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()