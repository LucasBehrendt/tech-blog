from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Form for posting comments"""

    class Meta:
        """Definition of fields used in form"""
        model = Comment
        fields = ['body', ]
