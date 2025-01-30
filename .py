def calcular_imc(peso, altura_cm):
    """Calcula o Índice de Massa Corporal (IMC) e retorna a classificação."""
    altura = altura_cm / 100  # Convertendo cm para metros
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    
    imc = peso / (altura ** 2)
    
    # Classificação do IMC
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc < 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 34.9:
        classificacao = "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        classificacao = "Obesidade Grau 2"
    else:
        classificacao = "Obesidade Grau 3 (mórbida)"
    
    return round(imc, 2), classificacao

# Entrada do usuário
try:
    peso = float(input("Digite seu peso (kg): "))
    altura_cm = float(input("Digite sua altura (cm): "))
    imc, classificacao = calcular_imc(peso, altura_cm)
    print(f"Seu IMC é: {imc} - {classificacao}")
except ValueError as e:
    print(f"Erro: {e}")
