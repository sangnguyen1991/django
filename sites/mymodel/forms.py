from django.forms import ModelForm
from mymodel.models import Comment
 
class MyCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'text', 'notes']