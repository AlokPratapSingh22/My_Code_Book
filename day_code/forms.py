from django import forms
from .models import CodePage, CodeBlock
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'placeholder': 'John Doe',
            'maxlength': '16',
            'minlength': '6',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': 'JohnDoe@mail.com',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'placeholder': 'Password',
            'maxlength': '22',
            'minlength': '8'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'placeholder': 'Confirm Password',
            'maxlength': '22',
            'minlength': '8'
        })

    username = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CodeBlockForm(forms.ModelForm):

    class Meta:
        model = CodeBlock
        fields = ("author", "title", "description")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control textbox'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control tabSupport textbox'})
        }


class CodePageForm(forms.ModelForm):

    class Meta:
        model = CodePage
        fields = ("title", "question", "code")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': "titleInput"}),
            'question': forms.Textarea(attrs={'rows': 2, 'class': 'form-control textbox tabSupport editable', 'id': "questionInput"}),
            'code': forms.Textarea(attrs={'rows': 3, 'class': 'form-control tabSupport code-area textbox editable', 'id': "codeInput"})
        }
