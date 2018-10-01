from django.urls import path
from . import views
from .views import AgendaListView, CriaCadastroCreateView

urlpatterns = [
    path('', AgendaListView.as_view(), name='lista'),
    path('cadastrar/', CriaCadastroCreateView.as_view(), name='cadastrar'),
]
