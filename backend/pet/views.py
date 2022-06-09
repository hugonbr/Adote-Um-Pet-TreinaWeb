from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from pet.models import Pet
from pet.serializers import pet_serializer


class PetList(APIView):
    def get(self, request, format=None):
        pets = Pet.objects.all()
        serializer = pet_serializer.PetSerializer(pets, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = pet_serializer.PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {
                "message": "Houveram erros de validação",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
