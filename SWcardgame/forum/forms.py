from django.forms import *
from .models import *

class AddPost(ModelForm):
   class Meta:
        boost = {'class': 'form-control'}
        fields = ['title', 'text']
        model = Post
        widgets = {
            'title': TextInput(boost),
            'text': Textarea(boost),
            'created_at': DateInput({'class': 'form-control', 'type': 'date'})
        }

class AddComment(ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'text')
