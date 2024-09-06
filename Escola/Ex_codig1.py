# Função para explicar declaração de variáveis e interação com o usuário 
def explicar_variavel_interacao():
    print('Vamos aprender sobre declaração de variável e interação com o usuário em Python!')
    # Declaração de variáveis
    nome = "João"   # A variável 'nome' armazena uma string.
    idade = 25      # A variável 'idade' armazena um número inteiro.
    altura = 1.75   # A variável 'altura' armazena um número de ponto flutuante.
    # Mostra o valor das variáveis.
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f'Altura: {altura} metros.')
    # Interação com o usuário.
    print('\nAgora, vamos interagir com o usuário.')
    # Solicita o nome do usuário.
    nome_user = input('Qual é seu nome: ')
    print(f'Olá, {nome_user}.')
    # Solicita a idade do usuário.
    idade_user = int(input('Qual é sua idade: '))
    print(f'Você tem {idade_user} anos.')
    # Solicita a altura do usuário.
    altura_user = float(input('Qual é sua altura em metros: '))
    print(f'Sua altura é {altura_user} metros.')
    # Mostra todos os dados fornecidos pelo usuário.
    print('\nAqui estão as informações que você forneceu ') 
    print(f'Nome: {nome_user}')
    print(f'Idade: {idade_user}')
    print(f'Altura: {altura_user} metros.')
# Executa a função
explicar_variavel_interacao()
