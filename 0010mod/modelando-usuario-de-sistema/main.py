from Usuario import Usuario

# Instanciando valores dos objetos Usuários
UsuarioUm = Usuario(1, "ThalesL", "thalesliscano@gmail.com")
UsuarioDois = Usuario(2, "ViniciusL", "viniciusgliscano@gmail.com")

# Imprimindo suas informações
print(f"Nome de usuário: {UsuarioUm.get_nome_usuario()}\nemail: {UsuarioUm.get_email()}")
print(f"Nome de usuário: {UsuarioDois.get_nome_usuario()}\nemail: {UsuarioDois.get_email()}")

# Modificando para visualizar mudanças
UsuarioUm.set_email("thalesdliscano@gmail.com")
UsuarioDois.set_email("viniliscano@gmail.com")

print("\n")
print(f"Nome de usuário: {UsuarioUm.get_nome_usuario()}\nemail: {UsuarioUm.get_email()}")
print(f"Nome de usuário: {UsuarioDois.get_nome_usuario()}\nemail: {UsuarioDois.get_email()}")

# Testando a ativação e desativação de conta da Classe usuário
UsuarioUm.desativar_conta()
print(f"Conta do usuárioUm está: {UsuarioUm.get_ativo()}")
UsuarioUm.ativar_conta()
print(f"Conta do usuárioUm está: {UsuarioUm.get_ativo()}")

# Testando a verificação de seha
print(f"A senha digitada está:{UsuarioUm.verificar_senha("1234568")}")