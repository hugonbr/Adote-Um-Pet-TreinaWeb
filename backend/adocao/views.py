from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from adocao.serializer import AdocaoSerializer


class AdocaoList(APIView):
    def post(self, request, format=None):
        serializer = AdocaoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {
                "message": "Houveram erros de validação",
                "errors": serializer.errors,
            },
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
