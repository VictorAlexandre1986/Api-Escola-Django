from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Curso
from .serializers import CursoSerializers

class CursoViewSet(viewsets.ViewSet):
    """
    ViewSet completo para gerenciar cursos com operações CRUD.
    """

    # Listar todos os cursos
    @swagger_auto_schema(
        operation_description="Lista todos os cursos disponíveis",
        responses={200: CursoSerializers(many=True)}
    )
    def list(self, request):
        """
        Retorna uma lista de todos os cursos.
        """
        cursos = Curso.objects.all()
        serializer = CursoSerializers(cursos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Criar um novo curso
    @swagger_auto_schema(
        operation_description="Cria um novo curso",
        request_body=CursoSerializers,
        responses={
            201: CursoSerializers,
            400: openapi.Response("Erro de validação", examples={"application/json": {"id": ["O ID deve ter exatamente 4 caracteres."]}})
        }
    )
    def create(self, request):
        """
        Cria um novo curso com os dados fornecidos.
        """
        serializer = CursoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Detalhar um curso específico
    @swagger_auto_schema(
        operation_description="Retorna os detalhes de um curso específico pelo ID",
        responses={
            200: CursoSerializers,
            404: openapi.Response("Curso não encontrado", examples={"application/json": {"detail": "Not found."}})
        }
    )
    def retrieve(self, request, pk=None):
        """
        Retorna os detalhes de um curso com base no ID (pk).
        """
        try:
            curso = Curso.objects.get(pk=pk)
            serializer = CursoSerializers(curso)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Curso.DoesNotExist:
            return Response({"detail": "Curso não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    # Atualizar um curso existente
    @swagger_auto_schema(
        operation_description="Atualiza um curso existente pelo ID",
        request_body=CursoSerializers,
        responses={
            200: CursoSerializers,
            400: openapi.Response("Erro de validação", examples={"application/json": {"preco": ["O preço não pode ser negativo."]}}),
            404: openapi.Response("Curso não encontrado")
        }
    )
    def update(self, request, pk=None):
        """
        Atualiza um curso existente com base no ID (pk).
        """
        try:
            curso = Curso.objects.get(pk=pk)
            serializer = CursoSerializers(curso, data=request.data, partial=True)  # partial=True permite atualizações parciais
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Curso.DoesNotExist:
            return Response({"detail": "Curso não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    # Deletar um curso
    @swagger_auto_schema(
        operation_description="Deleta um curso existente pelo ID",
        responses={
            204: openapi.Response("Curso deletado com sucesso"),
            404: openapi.Response("Curso não encontrado")
        }
    )
    def destroy(self, request, pk=None):
        """
        Deleta um curso com base no ID (pk).
        """
        try:
            curso = Curso.objects.get(pk=pk)
            curso.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Curso.DoesNotExist:
            return Response({"detail": "Curso não encontrado."}, status=status.HTTP_404_NOT_FOUND)