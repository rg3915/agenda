from django import forms
from .models import Cadastro


class CadastroForm(forms.ModelForm):
    widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control col-sm-12 form-control-lg',
                'type': 'text', }),
            'email': forms.TextInput(attrs={
                'class': 'form-control col-sm-12 form-control-lg',
                'type': 'text', }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control col-sm-12 form-control-lg',
                'type': 'text', }),
            'sexo': forms.Select(attrs={
                'class': 'custom-select form-control-lg', }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control col-sm-12 form-control-lg',
                'type': 'text', }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control col-sm-12 form-control-lg',
                'type': 'text', }),
            'cargo': forms.TextInput(attrs={
                'class': 'form-control col-sm-12 form-control-lg',
                'type': 'text', }),
        }
    class Meta:
        model = Cadastro
        fields = '__all__'
