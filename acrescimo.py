dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano (com 4 dígitos): "))
hora = int(input("Digite a hora: "))
minuto = int(input("Digite o minuto: "))
segundo = int(input("Digite o segundo: "))

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
    nova_data = datetime.datetime(ano, mes, dia) + datetime.timedelta(days=acrescimo)
    nova_hora = datetime.time(hora, minuto, segundo)
elif opcao == 2:
    nova_data = datetime.datetime(ano, mes, dia)
    nova_hora = datetime.datetime.combine(datetime.date.today(), datetime.time(hora, minuto, segundo)) + datetime.timedelta(hours=acrescimo)
elif opcao == 3:
    nova_data = datetime.datetime(ano, mes, dia)
    nova_hora = datetime.datetime.combine(datetime.date.today(), datetime.time(hora, minuto, segundo)) + datetime.timedelta(minutes=acrescimo)
elif opcao == 4:
    nova_data = datetime.datetime(ano,)