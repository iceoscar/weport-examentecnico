from django.forms import ModelForm

from employees.models import Employee


class EmployeeBaseForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'type_blood', 'photo')


class EmployeeCreateForm(EmployeeBaseForm):
    pass


class EmployeeUpdateForm(EmployeeBaseForm):
    pass


class EmployeeDeleteForm(EmployeeBaseForm):
    class Meta:
        model = Employee
        fields = ()
