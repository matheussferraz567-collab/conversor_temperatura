nome = input("Digite seu nome: ") # Variável Nome, irá receber um texto em Input(), para armazenar o nome do usário
temperatura = float(input("Digite a temperatura em Celsius: ")) # Temperatura irá receber em float para converter o Input(), pois é uma cadeia de texto
resultado = (9.0/5.0 * temperatura) + 32 # Fórmula de Conversão de Temperatura
print(f"Ola", nome, " Resultado da conversão é: ", resultado, "graus Fahrenheit") # Mensagem para mostrar na tela com o resultado final