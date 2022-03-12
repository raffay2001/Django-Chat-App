from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Creating a new form for the user to sing up for a new account 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



