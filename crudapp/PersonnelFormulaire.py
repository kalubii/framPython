from django import forms
from .models import Personnel


class PersonnelFormulaire(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super (PersonnelFormulaire,self).__init__(*args,**kwargs)
        self.fields['poste'].empty_label=" "
