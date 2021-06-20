from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    """Форма для редактирования сообщения."""
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'title', 'text': 'text'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
