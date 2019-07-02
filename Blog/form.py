from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    author = forms.CharField(label='author',
        widget= forms.TextInput(
            attrs={
            "class":"w3-input w3-border w3-margin-bottom", "style":"height: 60px;"
            }
            )
    )
    text = forms.CharField(
        widget= forms.Textarea(
            attrs={
            "class":"w3-input w3-border w3-margin-bottom", "style":"height: 300px;"
            }
            )
    )
    email = forms.EmailField(
       widget= forms.TextInput(
            attrs={
            "class":"w3-input w3-border w3-margin-bottom", "style":"height: 60px;"
            }
            )
    )

    class Meta:
        model = Comment
        fields = [
            'author', 
            'text',
            'email'
        ]
       