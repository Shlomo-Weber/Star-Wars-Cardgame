from django.forms import *
from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
   class Meta:
        boost = {'class': 'form-control'}
        fields = ['title', 'text']
        model = Post
        widgets = {
            'title': TextInput(boost),
            'text': Textarea(boost),
            'created_at': DateInput({'class': 'form-control', 'type': 'date'})
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
