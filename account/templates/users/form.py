from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class meta(UserCreationForm):
        felids=UserCreationForm.Meta.fields+("email",)