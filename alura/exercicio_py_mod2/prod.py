#exercicio_1

numero = int(input ("Digite um número: "))

if numero %2 == 0:
    print("o número é par.")

else: 
    print("o número é ímpar")

idade = int(input("Digite sua idade: "))

#exercicio_2

if 0 < idade <= 12:
    print("Criança")

elif 12 <idade < 18:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")
else:
    print("Valor inválido!")

#exercicio_3

usuario_correto = "alura"
senha_correta = "alura123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido")
else:
    print("Credenciais inválidas. Tente novamente")

#exercicio_4

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
        print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
        print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
        print("O ponto está no quarto quadrante.")
else:
        print("O ponto estásobre um eixo ou na origem.")