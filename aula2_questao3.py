# Lê as informações do participante
idade = int(input("Digite sua idade: "))
jogou_3_ou_mais = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ") == "True"
vitorias = int(input("Quantos jogos já venceu? "))

# Verifica as condições para ingresso
apto = (16 <= idade <= 18) and jogou_3_ou_mais and (vitorias >= 1)

# Exibe o resultado
print("Apto para ingressar no clube de jogos de tabuleiro:", apto)
