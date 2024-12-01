from django import forms
from .models import Noticia
from .models import Categoria
from usuarios.models import UserBlog  # Importe o modelo de usuário personalizado

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields= '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome'].lower()  # Normaliza para minúsculas
        if Categoria.objects.filter(nome=nome).exists():
            raise forms.ValidationError('Essa categoria já existe.')
        return nome
    
class CategoriaFilterForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        required=False,
        label='Nome da Categoria',
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o nome da categoria',
            'class': 'form-control',
            'id': 'id_nome'  
        })
    )


class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = '__all__'
        widgets = {
            'data_publicacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
            'texto': forms.Textarea(attrs={'class': 'form-control'}),  
            'titulo': forms.TextInput(attrs={'class': 'form-control'}), 
            'image': forms.FileInput(attrs={'class': 'form-control'}), 
            'categoria': forms.Select(attrs={'class': 'form-control'}),

        }

class NoticiaFilterForm(forms.Form):
    titulo = forms.CharField(
        max_length=200,
        required=False,
        label='Título',
        widget=forms.TextInput(attrs={'placeholder': 'Digite o título','class': 'form-control'})
    )
    data_publicacao_inicio = forms.DateField(
        required=False,
        label='Data de Publicação (Início)',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    data_publicacao_fim = forms.DateField(
        required=False,
        label='Data de Publicação (Fim)',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        label='Categoria',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
  
