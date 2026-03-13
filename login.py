"Login"

usuario = "douglas"
senha = "1234"

tentativa = 0
tentativa_restante = 3

while tentativa != 3:

    usuario_n = input("Digite o seu Usuario: ")
    senha_n = input("Digite a sua senha: ")

    if usuario_n == usuario and senha_n == senha:
        print("Acesso permitido")
        break

    else:
        print("Usuário ou senha incorretos")
        tentativa = tentativa + 1
        print(f"Tentativa {tentativa} de 3")

        tentativa_restante = tentativa_restante - 1
        print(f"Você ainda tem {tentativa_restante} tentativas")

print("Conta bloqueada")
