from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(initial='Мне очень нравится ваш сайт!')
    email = forms.EmailField(required=False, label='Почта')
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'special'}), label='Сообщение')

    # вызывается на этапе проверки если начинается с clean_ + название поля
    def clean_message(self):
        message = self.cleaned_data['message']
        num_word = len(message.split())
        if num_word < 3:
            raise forms.ValidationError('Слишком мало слов )))')
        return message