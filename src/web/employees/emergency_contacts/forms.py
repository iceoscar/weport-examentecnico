from django.forms import ModelForm

from emergency_contacts.models import EmergencyContact


class EmergencyContactBaseForm(ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ('name', 'mobile', 'relationship', 'priority')


class EmergencyContactCreateForm(EmergencyContactBaseForm):
    pass


class EmergencyContactUpdateForm(EmergencyContactBaseForm):
    pass


class EmergencyContactDeleteForm(EmergencyContactBaseForm):
    class Meta:
        model = EmergencyContact
        fields = ()
