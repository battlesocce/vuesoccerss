from django_registration.forms import RegistrationForm
from users.models import CustomUser


class CustomUserForm(RegistrationForm):
    CustomUser._meta.get_field('email')._unique = True
    class Meta(RegistrationForm.Meta):
        model = CustomUser

