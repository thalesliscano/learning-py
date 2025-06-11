class Usuario:
    def __init__(self,id, nome_usuario,email):
        self.__id = id
        self._nome_usuario = nome_usuario
        self._senha_hash = "12345678"
        self._email = email
        self._ativo = True
    def get_nome_usuario(self):
        return self._nome_usuario
    
    def get_email(self):
        return self._email
    def set_email(self, novo_email):
        self._email = novo_email
    def get_ativo(self):
        return self._ativo
    def desativar_conta(self):
        self._ativo = False
    def ativar_conta(self):
        self._ativo = True
    def verificar_senha(self,senha_digitada):
        if(senha_digitada == self._senha_hash):
            return True
        return False


