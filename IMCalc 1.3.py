print('CALCULADORA DE IMC v1.3 BETA - by jncque')

nome = input('Digite seu nome: ')
print(f'Olá {nome}')

idade = int(input('Digite sua idade (xx): '))
peso = float(input('Digite seu peso (xx.x): '))
altura = float(input('Digite sua altura (x.xx): '))

resultado = peso / (altura * altura)

if resultado <= 18.5:
    print(f"Seu IMC é de {resultado:.1f}. Você está abaixo do peso.")
elif resultado > 18.5 and resultado <= 24.9:
    print(f"Seu IMC é de {resultado:.1f}. Seu peso está normal.")
elif resultado > 24.9 and resultado <= 29.9:
    print(f"Seu IMC é de {resultado:.1f}. Você está no sobrepeso.")
else:
    print(f"Seu IMC é de {resultado:.1f}. Você está no quadro de obesidade.")