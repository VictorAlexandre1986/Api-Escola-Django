from django.urls import path,include

from .views import CursoViewSet

urlpatterns = [
    path('cursos/', CursoViewSet.as_view({'get': 'list'}), name='curso-list'),
    path('cursos/criar/', CursoViewSet.as_view({'post': 'create'}), name='curso-create'),
    path('cursos/<str:pk>/', CursoViewSet.as_view({'get': 'retrieve'}), name='curso-detail'),
    path('cursos/<str:pk>/atualizar/', CursoViewSet.as_view({'put': 'update'}), name='curso-update'),
    path('cursos/<str:pk>/deletar/', CursoViewSet.as_view({'delete': 'destroy'}), name='curso-delete'),
]

