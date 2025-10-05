usuarioCorreto = "admin"
senhaCorreta = "senha1234"

usuarioInput = input("Nome do usuário: ").lower().strip()
senhaInput = input("Senha: ").lower().strip()

if usuarioInput == usuarioCorreto and senhaInput == senhaCorreta:
    print("Login bem-sucedido!")

elif usuarioInput != usuarioCorreto:
    print("Usuário inválido.")
    
else:
    print("Senha incorreta.")