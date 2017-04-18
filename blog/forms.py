from django.forms import ModelForm
# from django.db import  models
from models import Main


class FormBlog(ModelForm):
    class Meta:
        model = Main
