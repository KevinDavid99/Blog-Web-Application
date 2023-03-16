from .models import Post
from django import forms

class PostEdit(forms.ModelForm):
    
    
    class Meta:
        model = Post
        fields = '__all__' 
        exclude = ['author', 'updated', 'date_posted']
        widgets = {
            'image-file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }