import os

def conectar_sistema():
    db_user = os.getenv("DB_USER", "usuario_padrao")
    db_password = os.getenv("DB_PASSWORD", "senha_padrao")

    print("Conectando ao sistema...")
    print(f"Usuário: {db_user}")
    print("Senha: ***OCULTA***")  # nunca mostrar senha real

    if db_password == "senha_padrao":
        print("⚠️ Senha não configurada!")
    else:
        print("✔ Sistema conectado com segurança!")

conectar_sistema()