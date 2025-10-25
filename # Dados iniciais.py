# Dados iniciais
salario_por_hora = 20
horas_trabalhadas = 40

# Cálculos
salario_bruto = salario_por_hora * horas_trabalhadas
desconto_inss = salario_bruto * 0.10
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (desconto_inss + desconto_sindicato)

# Resultados
print("Salário semanal bruto: R$", salario_bruto)
print("Desconto INSS (10%): R$", desconto_inss)
print("Desconto Sindicato (5%): R$", desconto_sindicato)
print("Salário semanal líquido: R$", salario_liquido)

salario_bruto = 20 * 40
salario_liquido = 20 * 40 - (20 * 40 * 0.10) - (20 * 40 * 0.05)

print("Salário semanal bruto: R$", salario_bruto)
print("Salário semanal líquido: R$", salario_liquido)

# Taxa de câmbio: 1 CNY = 0.69 BRL
valor_em_reais = 100  # você pode mudar este valor
valor_em_yuan = valor_em_reais / 0.69

print(valor_em_reais, "reais equivalem a", round(valor_em_yuan, 2), "yuans chineses.")
