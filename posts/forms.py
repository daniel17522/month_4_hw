from django import forms
from django.core.exceptions import ValidationError
from django.template.defaulttags import comment

from posts.models import Post, Tag


class PostForm(forms.Form):
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')


        if title and content and title.lower == content.lower():
            raise forms.ValidationError('Заголовок и контент не должны совпадать')
        else:
            return cleaned_data

    def clean_title(self):
        cleaned_data = super().clean()
        title = self.cleaned_data.get('title')
        if title and title.lower == "Python":
            raise forms.ValidationError("Заголовок не может быть словом Python")





class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'rate', 'image', 'tags']

class SearchForm(forms.Form):
    search = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={
        'placeholder': "Введите текст для поиска",
        'class': 'form-control'}))

    tag = forms.ModelMultipleChoiceField(required=False,
                                    queryset=Tag.objects.all(),
                                    widget=forms.CheckboxSelectMultiple,)
    orderings = (
        ("title", "По названию"),
        ("-title", "По названию в обратном порядке"),
        ("rate", "По рейтингу"),
        ("-rate", "По рейтингу в обратном порядке"),
        ("created_at", "По дате создания"),
        ("-created_at", "По дате создания в обратном порядке")
    )
    ordering = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(attrs={'class': 'form-control'})
    )