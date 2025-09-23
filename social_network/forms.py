from django import forms
from .models import Post

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "image", "text", "category"]



class Filter(forms.Form):
    author = forms.CharField(label='author', required=False, widget=forms.TextInput(attrs={'placeholder': 'name'}))
    created = forms.DateField(label='data', required=False, widget=forms.DateInput(attrs={"type": "date"}))
    date1 = forms.DateField(label='min', required=False, widget=forms.DateInput(attrs={"type": "date"}))
    date2 = forms.DateField(label='max', required=False, widget=forms.DateInput(attrs={"type": "date"}))


from django import forms
from authenticator.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
