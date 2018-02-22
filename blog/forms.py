from django.forms import ModelForm, TextInput, Textarea

from blog.models import Comments



class CommentForm(ModelForm):
    class Meta:
        model = Comments
        widgets = {
            'comments_author': TextInput(attrs={'placeholder': 'Ваше имя'}),
            'comments_text': Textarea(attrs={'placeholder': 'Текст комментария'}),
        }
        fields = ['comments_author', 'comments_text']
