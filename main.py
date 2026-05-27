# Arquivo que carrega os módulos gradualmente
# Menu principal da calculadora

try:
    import calc_basico
except ImportError:
    calc_basico = None
    print("Módulo calc_basico não encontrado.")

try:
    import calc_potencia
except ImportError:
    calc_potencia = None
    print("Módulo calc_potencia não encontrado.")

try:
    import calc_percentual
except ImportError:
    calc_percentual = None
    print("Módulo calc_percentual não encontrado.")

try:
    import calc_estatistica
except ImportError:
    calc_estatistica = None
    print("Módulo calc_estatistica não encontrado.")

try:
    import calc_conversao
except ImportError:
    calc_conversao = None
    print("Módulo calc_conversao não encontrado.")


while True:
    print("\n====== CALCULADORA ======")
    print("1 - Operações Básicas")
    print("2 - Potência")
    print("3 - Percentual")
    print("4 - Estatística")
    print("5 - Conversão")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # ---------------- BÁSICO ----------------
    if opcao == "1":

        if calc_basico is None:
            print("Módulo não disponível.")
            continue

        print("\n--- Operações Básicas ---")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")

        escolha = input("Escolha a operação: ")

        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if escolha == "1":
            resultado = calc_basico.somar(a, b)

        elif escolha == "2":
            resultado = calc_basico.subtrair(a, b)

        elif escolha == "3":
            resultado = calc_basico.multiplicar(a, b)

        elif escolha == "4":
            resultado = calc_basico.dividir(a, b)

        else:
            print("Opção inválida.")
            continue

        print("Resultado:", resultado)

    # ---------------- POTÊNCIA ----------------
    elif opcao == "2":

        if calc_potencia is None:
            print("Módulo não disponível.")
            continue

        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))

        resultado = calc_potencia.potencia(base, expoente)

        print("Resultado:", resultado)

    # ---------------- PERCENTUAL ----------------
    elif opcao == "3":

        if calc_percentual is None:
            print("Módulo não disponível.")
            continue

        print("\n--- Percentual ---")
        print("1 - Calcular percentual")
        print("2 - Acréscimo percentual")
        print("3 - Desconto percentual")

        escolha = input("Escolha a operação: ")

        valor = float(input("Digite o valor: "))
        porcentagem = float(input("Digite a porcentagem: "))

        if escolha == "1":
            resultado = calc_percentual.percentual(
                valor,
                porcentagem
            )

        elif escolha == "2":
            resultado = calc_percentual.acrescimo(
                valor,
                porcentagem
            )

        elif escolha == "3":
            resultado = calc_percentual.desconto(
                valor,
                porcentagem
            )

        else:
            print("Opção inválida.")
            continue

        print("Resultado:", resultado)

    # ---------------- ESTATÍSTICA ----------------
    elif opcao == "4":

        if calc_estatistica is None:
            print("Módulo não disponível.")
            continue

        numeros = input(
            "Digite os números separados por espaço: "
        ).split()

        numeros = [float(n) for n in numeros]

        print("\n1 - Média")
        print("2 - Mediana")
        print("3 - Moda")

        escolha = input("Escolha: ")

        if escolha == "1":
            resultado = calc_estatistica.media(numeros)

        elif escolha == "2":
            resultado = calc_estatistica.mediana(numeros)

        elif escolha == "3":
            resultado = calc_estatistica.moda(numeros)

        else:
            print("Opção inválida.")
            continue

        print("Resultado:", resultado)

    # ---------------- CONVERSÃO ----------------
    elif opcao == "5":

        if calc_conversao is None:
            print("Módulo não disponível.")
            continue

        print("\n--- Conversão ---")
        print("1 - Celsius para Fahrenheit")
        print("2 - Kg para Libras")
        print("3 - Km para Milhas")

        escolha = input("Escolha: ")

        if escolha == "1":
            temperatura = float(input("Digite a temperatura em Celsius: "))

            resultado = calc_conversao.celsius_para_fahrenheit(temperatura)

        elif escolha == "2":
            kg = float(input("Digite o valor em kg: "))

            resultado = calc_conversao.kg_para_libras(kg)

        elif escolha == "3":
            km = float(input("Digite o valor em km: "))

            resultado = calc_conversao.km_para_milhas(km)

        else:
            print("Opção inválida.")
            continue

        print("Resultado:", resultado)

    # ---------------- SAIR ----------------
    elif opcao == "0":
        print("Calculadora encerrada.")
        break

    else:
        print("Opção inválida.")