from django import forms
from .models import Cadastro


class CadastroForm(forms.ModelForm):

    class Meta:
        model = Cadastro
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'sexo': forms.Select(attrs={
                'class': 'custom-select form-control', }
            ),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'cargo': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
        }
