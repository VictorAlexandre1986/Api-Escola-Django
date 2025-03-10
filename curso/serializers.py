from rest_framework import serializers
from .models import Curso

class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


    def validate_id(self, value):
        # Opcional: validação personalizada para o 'id'
        if len(value) != 4:
            raise serializers.ValidationError("O ID deve ter exatamente 4 caracteres.")
        return value

    def validate_carga_horaria(self, value):
        if value <= 0:
            raise serializers.ValidationError("A carga horária deve ser maior que zero.")
        return value

    def validate_preco(self, value):
        if value < 0:
            raise serializers.ValidationError("O preço não pode ser negativo.")
        return value