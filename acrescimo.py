from datetime import datetime, timedelta

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano (com 4 dígitos): "))
hora = int(input("Digite a hora: "))
minuto = int(input("Digite o minuto: "))
segundo = int(input("Digite o segundo: "))

data = datetime(ano, mes, dia, hora, minuto, segundo)

print("Data e hora atual:")
print(f"{dia:02}/{mes:02}/{ano} {hora:02}:{minuto:02}:{segundo:02}")

acrescimo = int(input("Digite a quantidade de tempo a acrescentar: "))
print("Escolha o que deseja acrescentar:")
print("1 – Acrescentar dias")
print("2 – Acrescentar horas")
print("3 – Acrescentar minutos")
print("4 – Acrescentar segundos")
opcao = int(input("Digite o código da opção desejada: "))

if opcao == 1:
    novad = data + timedelta (days=acrescimo)
    print("Atualização: ", novad)
elif opcao == 2:
    novad = data + timedelta (hours=acrescimo)
    print("Atualização: ", novad)
elif opcao == 3:
    novad = data + timedelta (minutes=acrescimo)
    print("Atualização: ",novad)
elif opcao == 4:
    novad = data + timedelta(seconds=acrescimo)
    print("Atualização: ", novad)
else:
    print("Tipo de acrésimo inválido!")
