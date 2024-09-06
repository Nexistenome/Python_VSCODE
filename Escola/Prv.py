# Esse documento só tá sendo utilizado para estudar para a prova do dia 6 de setembro de 2024 e nada mais.

# Assuntos a ser estudados: Variáveis, comentários, operadores lógicos, aritmétricos e relacionais.

# VARIÁVEIS.
def variaveis():
    # Inteiro (INT) = Utilizado para números inteiro sendo positivos ou negativos.
    idade = -226
    print(type(idade))
    # Float (FLOAT) = Utilizado para números racionais sendo positivos ou negativos.
    altura = 1.73
    print(type(altura))
    # Complexo (COMPLEX) = Utilizados em números complexos.
    a = 10+13j
    print(type(a))
    # String (STR) = Utilizados para textos, frases entre outros, basicamente utilizando caracteres.
    nome = "Kaique Lemos Carrenho"
    print(type(nome))
    # Boolean (BOOL) = Utilizado para dado lógico: true ou false.
    sexta_feira_prova = True
    print(type(sexta_feira_prova))
    # Lista (LIST) = Utilizado para conjuntos de elementos variados, como inteiros. floats, strings, entre outros.
    amor = ["Leticia", "Alice", "Leiliane", "Rita"]
    print(type(amor))
    # Tuplas (TUPLE) = Utilizado para conjuntos de elementos, porém não é possivél mudar valores dentro da variável.
    valores = (47, 38, 12, 45, 74)
    print(type(valores))
    # Dicionários (DICT) = Utilizado para agrupar elementos.
    altura2 = {"Felippe":1.73, "Nicolas":1.71, "Ono e Bololo":1.59}
    print(type(altura2))
variaveis()

# OPERADORES LÓGICOS
def op_logic():
    a = 3
    b = 4
    # Adição (+)
    soma = a + b
    # Subtração (-)
    sub = a - b
    # Multiplicação (*)
    multi = a * b
    # Divisão (/)
    divi = a / b
    # Divisão Inteira (//)
    divint = a//b
    # Modulo (%)
    mod = a%b
    # Exponenciação (**)
    exp = a**b
    print(soma, sub, multi, divi, divint, mod, exp)
op_logic()    

# OPERADORES RELACIONAIS    
def op_rel():
    a = 7
    # IGUAL (==)
    if (a == 7): 
        print("SETE")
    # DIFERENTE (=!)
    if a != 4:
        print("DIFERENTE DE SETE O QUATRO")
    # MAIOR OU MENOR (> ou <)
    if a > 4 :
        print("SETE MAIOR QUE QUATRO.")
    # MAIOR OU IGUAL (>=) MENOR OU IGUAL (<=)
op_rel()

# OPERADORES ATRIBUIÇÃO
def op_atrib():
    a = 5
    a += 7
    a -= 1
    a *= 24
    a /= 2
    # a %= 3 VTNC MODULO, N TE ENTENDO SEU MERDINHA FDP
    print(a)
op_atrib()

