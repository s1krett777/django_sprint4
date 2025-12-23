from django import forms
from django.contrib.auth.models import User

from blog.models import Post, Comment


class BasePostForm(forms.ModelForm):
    pub_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Post
        exclude = ('author',)  # исключаем автора

    def clean_pub_date(self):
        return self.cleaned_data.get('pub_date')


class PostForm(BasePostForm):
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
