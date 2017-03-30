from django import forms

class categoryAddForm(forms.Form):
    name = forms.CharField(label='назв категор', max_length=200, widget=forms.Textarea)
    sort = forms.IntegerField(label=u'Сортировка',initial=100)
    active = forms.BooleanField(initial=True, label='active')
    # img = forms.FileField(upload_to=u'category/', label=u'Картинка',  blank=True, null=True)
