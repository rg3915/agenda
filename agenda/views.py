from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CadastroForm
from .models import Cadastro

class CriaCadastroCreateView(CreateView):
    form_class = CadastroForm
    template_name = "cadastrar.html"
    model = Cadastro
    success_url = reverse_lazy("lista")

class AgendaListView(ListView):
    template_name = "lista.html"
    model = Cadastro
    context_object_name = "cadastro"
    query_results = Cadastro.objects.all()