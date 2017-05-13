from django.forms import ModelForm
# from django.db import  models
from blog.models import Main


class FormBlog(ModelForm):
    class Meta:
        model = Main
        fields = '__all__'

blog = FormBlog()
