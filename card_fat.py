#Crie um programa que:

# - Solicite valores das compras e pergunte ao usuario se e a ultima compra. Caso nao seja, solicite o valor da proxima.
# - Pergunte ao final o dia do pagamento da fatura.
# - Se o pagamento for ate o dia 25, nao aplique juros. Caso contrario, aplique 3% sobre o valor total da fatura, mais 1% adicional por dia apos o dia 25.

# variavel para somar os valores das compras
soma_compras = 0

while True:  # Inicia um loop ate a condicao ser atendida
    valor_compra = float(input("Digite o valor da compra: "))  # Pede ao cliente o valor da compra
    soma_compras += valor_compra  # Adiciona o valor da compra a soma total

    ultima_compra = input("E a ultima compra? Digite 's' ou 'n': ")  # Pergunta se e a ultima compra

    if ultima_compra.lower() == 's':
        print("Voce confirmou que e a ultima compra.")
        dia_pagamento = int(input("Digite o dia do pagamento (1 a 31): "))
            
        if dia_pagamento <= 25:
            juros = 0 # Pagamento sem juros
            print("Pagamento sem juros")
    
        else:
            dias_atraso = dia_pagamento - 25
            juros = 5 + dias_atraso # Pagamento com juros de 5% + 1% para cada dia de atraso
            print("Pagamento com juros")

        #Calculo do total de juros
        total_compras = soma_compras * (1 + juros/ 100)
        print(f"Valor da fatura: R${total_compras:.2f}")

        print("Seu pagamento foi reconhecido, obrigada.")  # Mensagem final
        break  #Encerra se for a ultima compra

    elif ultima_compra.lower() == 'n': #Voce pode pedir o valor da proxima compra
        print("Voce ainda tem limite disponivel. ")

