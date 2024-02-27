import re
from django.contrib.messages import constants
from django.contrib import messages

# Validadores de cadastro
class Validar_Cadastro:
    
    msg1 = 'Nome incorreto'
    msg2 = 'Nome deve ter entre 4 e 200 caracteres'
    msg3 = 'Sobrenome incorreto'
    msg4 = 'Sobrenome deve ter no mínimo 4 e no máximo 200 letras'
    msg5 = 'Email inválido'
    msg6 = 'Senha inválida'
    msg7 = 'Senha deve ter no mínimo 3 caracteres'
    msg8 = 'Confirmar Senha é inválida'
    msg9 = 'As senhas digitadas não são iguais'
    msg10 = 'Username incorreto'
    msg11 = 'Username deve ter entre 4 e 200 caracteres'

    @staticmethod
    def validar_nome(request, nome: str):
        if not isinstance(nome, str) or not nome:
            return messages.add_message(request, constants.ERROR, Validar_Cadastro.msg1)

        if len(nome) < 4 or len(nome) > 200:
            return messages.add_message(request, constants.ERROR, Validar_Cadastro.msg2)

        return nome

    @staticmethod
    def validar_sobrenome(request, sobrenome: str):
        if not isinstance(sobrenome, str) or not sobrenome:
            return messages.add_message(request, constants.ERROR, Validar_Cadastro.msg3)

        if len(sobrenome) < 4 or len(sobrenome) > 200:
            return messages.add_message(request, constants.ERROR, Validar_Cadastro.msg4)

        return sobrenome

    @staticmethod
    def validar_email(request, email: str):
        padrao = r"\b[\w.]+@(bol|outlook|gmail|terra|yahoo|uol|hotmail).*"
        result = re.search(padrao, email)
        return email if result else messages.add_message(request, constants.ERROR, Validar_Cadastro.msg5)

    @staticmethod
    def validar_senha(request, senha: str):
        if not senha:
            return messages.add_message(request, constants.ERROR, Validar_Cadastro.msg6)

        if len(senha) < 3:
            return messages.add_message(request, constants.ERROR, Validar_Cadastro.msg7)

        return senha

    @staticmethod
    def validar_confirmar_senha(request, senha, confirm_senha):
        if not confirm_senha:
            return messages.add_message(request, constants.ERROR, Validar_Cadastro.msg8)

        if confirm_senha != senha:
            return messages.add_message(request, constants.ERROR, Validar_Cadastro.msg9)
        
        return confirm_senha

    @staticmethod
    def validar_username(request, username: str):
        if not isinstance(username, str) or not username:
            return messages.add_message(request, constants.ERROR, Validar_Cadastro.msg10)

        if len(username) < 4 or len(username) > 200:
            return messages.add_message(request, constants.ERROR, Validar_Cadastro.msg11)

        return username
