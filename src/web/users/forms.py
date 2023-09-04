from django.forms import ModelForm

from users.models import User


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'type_blood', 'curp', 'photo', 'is_rrhh')


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'type_blood', 'curp', 'photo', 'is_rrhh')

