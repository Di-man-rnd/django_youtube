from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(initial='Мне очень нравится ваш сайт!')
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)
