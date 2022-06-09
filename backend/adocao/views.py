from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from adocao.serializer import AdocaoSerializer
from .models import Adocao
from .email_service import enviar_email_confirmacao


class AdocaoList(APIView):
    def get(self, request, format=None):
        adocoes = Adocao.objects.all()
        serializer = AdocaoSerializer(adocoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = AdocaoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            enviar_email_confirmacao(adocao)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {
                "message": "Houveram erros de validação",
                "errors": serializer.errors,
            },
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
