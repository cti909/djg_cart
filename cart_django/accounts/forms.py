from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        # fields = ['field1','field2']
        fields = '__all__' 

