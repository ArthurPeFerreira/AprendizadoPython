numero1 = ""
numero2 = ""
operador = ""
sair1while = True
sair2while = True
sair3while = True
contador1 = 0
contador2 = 0
contador3 = 0
testenumero1 = None
testenumero2 = None
testenumero3 = None
resultado = None
sair = ""

while True:
    while sair1while:
        contador1 = 0
        numero1 = input("Digite o primeio número da calculadora: ")

        while ((contador1 + 1) <= len(numero1)):
            testenumero1 = (numero1[contador1].isnumeric())
            contador1 += 1
            if (not (numero1.isnumeric())):
                print("Por favor, Digite um número.")
                break
            if (((contador1) == len(numero1)) and testenumero1 == True):
                sair1while = False

    while sair2while:
        contador2 = 0
        numero2 = input("Digite o segundo número da calculadora: ")

        while ((contador2 + 1) <= len(numero2)):
            testenumero2 = (numero2[contador2].isnumeric())
            contador2 += 1
            if (not (numero2.isnumeric())):
                print("Por favor, Digite um número.")
                break
            if (((contador2) == len(numero2)) and testenumero2 == True):
                sair2while = False

    while sair3while:
        operador = input("Digite o operador (+,-,*,/) da calculadora: ")

        if (operador == "+" or operador == "-" or operador == "/" or operador == "*"):
            sair3while = False
            break
        else:
            print("Por favor, Digite um operador (+,-,*,/) valido.")

    if (operador == "+"):
        resultado = float(numero1) + float(numero2)
    elif(operador == "-"):
        resultado = float(numero1) - float(numero2)
    elif(operador == "/"):
        resultado = float(numero1) / float(numero2)
    elif(operador == "*"):
        resultado = float(numero1) * float(numero2)

    print(f"O resultado é {resultado}")

    sair = input("Você quer [s]air? ")
    sair = sair.lower()
    if (sair.startswith("s")):
        break