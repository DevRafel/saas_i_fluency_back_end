from django import forms
from .models import Links

class FormLinks(forms.ModelForm):
       
       class Meta:
              model = Links
              fields = ['link_redirecionado', 'link_encurtado'] 