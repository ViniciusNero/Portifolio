# -*- coding: utf-8 -*-

def somar(x, y):
  """Esta função soma dois números"""
  return x + y

def subtrair(x, y):
  """Esta função subtrai dois números"""
  return x - y

def multiplicar(x, y):
  """Esta função multiplica dois números"""
  return x * y

def dividir(x, y):
  """Esta função divide dois números"""
  if y == 0:
    return "Erro! Divisão por zero não é permitida."
  return x / y

# --- Programa Principal ---

print("Selecione a operação desejada:")
print("1. Somar (+)")
print("2. Subtrair (-)")
print("3. Multiplicar (*)")
print("4. Dividir (/)")
print("========================================")


while True:
  # Pede a entrada do usuário
  escolha = input("Digite sua escolha (1/2/3/4) ou o símbolo (+/-/*//): ")

  # Verifica se a escolha é válida
  if escolha in ['1', '2', '3', '4', '+', '-', '*', '/']:
    try:
      num1 = float(input("Digite o primeiro número: "))
      num2 = float(input("Digite o segundo número: "))
    except ValueError:
      print("Entrada inválida. Por favor, digite apenas números.")
      continue # Volta para o início do loop

    resultado = 0
    operador = ''

    if escolha in ['1', '+']:
      resultado = somar(num1, num2)
      operador = '+'
    elif escolha in ['2', '-']:
      resultado = subtrair(num1, num2)
      operador = '-'
    elif escolha in ['3', '*']:
      resultado = multiplicar(num1, num2)
      operador = '*'
    elif escolha in ['4', '/']:
      resultado = dividir(num1, num2)
      operador = '/'

    # Exibe o resultado formatado
    if isinstance(resultado, str): # Verifica se o resultado é uma mensagem de erro
        print(resultado)
    else:
        print(f"O resultado de {num1} {operador} {num2} é: {resultado}")

  else:
    print("Opção inválida. Por favor, escolha uma operação válida.")

  # Pergunta se o usuário quer fazer outro cálculo
  proximo_calculo = input("\nDeseja fazer outro cálculo? (s/n): ")
  if proximo_calculo.lower() != 's':
    print("Encerrando a calculadora...")
    break # Encerra o loop e o programa
  
  print("----------------------------------------")