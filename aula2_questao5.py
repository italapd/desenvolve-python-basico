# Lê gênero, idade e tempo de serviço
genero = input("Digite seu gênero (M/F): ").upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

# Verifica se pode se aposentar de acordo com as regras
aposentar = (
    (genero == "F" and idade > 60) or
    (genero == "M" and idade > 65) or
    (tempo_servico >= 30) or
    (idade >= 60 and tempo_servico >= 25)
)

# Exibe o resultado
print(aposentar)
