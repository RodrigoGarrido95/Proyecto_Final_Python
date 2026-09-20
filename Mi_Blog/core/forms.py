from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido']

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo) < 5:
            raise forms.ValidationError("El título debe tener al menos 5 caracteres.")
        return titulo

    def clean_contenido(self):
        contenido = self.cleaned_data['contenido']
        if len(contenido) < 20:
            raise forms.ValidationError("El contenido debe tener al menos 20 caracteres.")
        return contenido
