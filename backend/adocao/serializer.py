from rest_framework import serializers

from adocao.models import Adocao
from pet.serializers import pet_serializer
from pet.models import Pet


class AdocaoSerializer(serializers.ModelSerializer):
    pet = pet_serializer.PetSerializer(many=False, read_only=True)
    pet_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=Pet.objects.all
    )

    class Meta:
        model = Adocao
        fields = "__all__"

    def create(self, validated_data):
        validated_data["pet"] = validated_data.pop("pet_id")
        return super().create(validated_data)

    def validate_valor(self, value):
        if value < 10:
            raise serializers.ValidationError("Deve ser maior que 10")
        if value > 100:
            raise serializers.ValidationError("Deve ser maior que 100")
        return value
