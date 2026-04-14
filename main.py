def analisar_numero(num): # "def" serve para criar um "atalho" para um bloco de código que pretendes usar várias vezes.
    paridade = "par" if num % 2 == 0 else "ímpar"
    sinal = "positivo" if num >= 0 else "negativo"
    tipo = "inteiro" if num % 1 == 0 else "decimal"

    print(f"Propriedades: {paridade}, {sinal}, {tipo}")

while True:
    try:
        v1 = float(input("\nValor 1: "))
        v2 = float(input("Valor 2: "))
    except ValueError:
        print("Erro: Digite apenas números!")
        continue

    operacao = input('Operação (+, -, *, /) ou "sair": ').lower().strip() # O ".lower()" é para garantir que tanto 'A' quanto 'a' sejam reconhecidos e o ".strip()" é para elimiar os espaços em branco.

    resultado = None # Necessário indicar que o resultado está vazio para não erro ao dividir por "0".

    if operacao == "sair": # Criando a saida do programa
        print("Até logo!")
        break

    if operacao in ['soma', '+']:
        resultado = v1 + v2
    elif operacao in ['subtracao', 'subtração', '-']:
        resultado = v1 - v2
    elif operacao in ['multiplicacao', 'multiplicação', '*', 'x']:
        resultado = v1 * v2
    elif operacao in ['divisao ', 'divisão', '/']:
        if v2 != 0:
            resultado = v1 / v2
        else:
            print("Erro: Divisão por zero não permitida")
    else:
        print("Operacação inválida")

    if resultado is not None:
        print(f"--- Resultado: {resultado} ---")
        analisar_numero(resultado)
                        
    pergunta = input("\nDeseja fazer outro cáculo? (s/n): ").lower()
    if pergunta != 's':
        print("Até logo!")
        break

