from django import forms
from .models import Blog,Post


class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']
        labels = {'name':''}

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':50})}