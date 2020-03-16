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
    title = forms.CharField(label=_("Title"), max_length=60, required=True)
    text = forms.CharField(label=_("First message"), widget=TinyMCE(
    attrs={'cols': 80, 'rows': 30, 'placeholder': _("Write your comment here!")}, mce_attrs=TINYMCE_DEFAULT_CONFIG))

    class Meta():
        model = Topic
        fields = ('title', 'text')
