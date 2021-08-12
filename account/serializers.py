from rest_framework import serializers
from rest_framework.exceptions import APIException
from .models import *
from .utils import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def validate_email(self, value):

        if is_valid_email(value):
            if User.objects.filter(email=value).exists():
                raise ValidationErrorCustom('E-mail ja cadastrado', 'email', 409)
            return value
        raise ValidationErrorCustom('E-mail invalido','email',406)

    def validate_document(self, value):
        if is_cpf_valido(value):
            if User.objects.filter(document=limpa_numeros(value)).exists():
                raise ValidationErrorCustom('CPF ja cadastrado', 'document', 400)
            return limpa_numeros(value)
        raise ValidationErrorCustom('CPF invalidos','document',400)


    def validate_birthDate(self, value):
        if is_valid_age(value):
            return value
        raise ValidationErrorCustom('Idade invalida', 'birthDate', 400)

    def validate_phone(self, value):
        if is_valid_phone(value):
            return limpa_numeros(value)
        raise ValidationErrorCustom('Telefone invalido', 'phone', 400)



class ValidationErrorCustom(APIException):

    status_code = 500

    def __init__(self,detail,field,code):

        if code is not None:
            self.status_code = code

        if detail is not None:
            self.detail = {field:detail}
        else:
            self.detail = {field:self.default_detail}

