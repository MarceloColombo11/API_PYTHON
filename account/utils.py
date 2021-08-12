import re
from datetime import date

def is_valid_email(email):
    parameter = '^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(parameter,email):
        return True
    return False

def limpa_numeros(documento):
    documento_limpado = re.sub(r"[^0-9]", '', documento)  # Remove todos os digitos não numéricos
    return documento_limpado

def is_cpf_valido(cpf):
    cpf = limpa_numeros(cpf)
    #Valida a quantidade de digitos
    if len(cpf) == 11:
        #Elimina os numeros inválidos conhecidos
        if len(set(cpf)) != 1:
            #Calcula o primeiro digito verificador do cpf
            soma = 0
            peso = 10
            for n in range(9):
                soma = soma + int(cpf[n]) * peso

                # Decrement peso
                peso = peso - 1

            verifyingDigit = 11 -  soma % 11

            if verifyingDigit > 9 :
                firstVerifyingDigit = 0
            else:
                firstVerifyingDigit = verifyingDigit

            #Calcula o segundo digito verificador do cpf
            soma = 0
            peso = 11
            for n in range(10):
                soma = soma + int(cpf[n]) * peso

                # Subtrai o peso
                peso = peso - 1

            verifyingDigit = 11 -  soma % 11

            if verifyingDigit > 9 :
                secondVerifyingDigit = 0
            else:
                secondVerifyingDigit = verifyingDigit

            if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
                return True
    return False

def is_valid_phone(phone):
    default = '^(?:(?:\+|00)?(55)\s?)?(?:(?:\(?[1-9][0-9]\)?)?\s?)?(?:((?:9\d|[2-9])\d{3})-?(\d{4}))$'
    if re.search(default,phone):
        return True
    return False

def is_valid_age(birthDate):
    if (date.today().year - birthDate.year - ((date.today().month,date.today().day)<(birthDate.month,birthDate.day))) >= 18:
        return True
    return False