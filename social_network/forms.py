from django import forms
from .models import Post

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "category"]



class Filter(forms.Form):
    author = forms.CharField(label='author', required=False)
    created = forms.DateField(label='data', required=False, widget=forms.DateInput(attrs={"type": "date"}))
    date1 = forms.DateField(label='min', required=False, widget=forms.DateInput(attrs={"type": "date"}))
    date2 = forms.DateField(label='max', required=False, widget=forms.DateInput(attrs={"type": "date"}))