from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from emergency_contacts.models import EmergencyContact

from .forms import EmergencyContactCreateForm, EmergencyContactUpdateForm, EmergencyContactDeleteForm


template_base = 'emergency_contacts/'


class EmergencyContactBaseView(LoginRequiredMixin):
    model = EmergencyContact
    pk_url_kwarg = 'emergency_contact_pk'
    employee_pk = None

    def get_success_url(self):
        self.employee_pk = self.request.resolver_match.kwargs['employee_pk']
        return reverse('employee-detail', kwargs={'employee_pk': self.employee_pk})


class EmergencyContactListView(EmergencyContactBaseView, ListView):
    template_name = template_base + 'list.html'


class EmergencyContactDetailView(EmergencyContactBaseView, DetailView):
    template_name = template_base + 'detail.html'


class EmergencyContactCreateView(EmergencyContactBaseView, CreateView):
    template_name = template_base + 'create.html'
    form_class = EmergencyContactCreateForm

    def form_valid(self, form, *args, **kwargs):
        self.employee_pk = self.request.resolver_match.kwargs['employee_pk']
        emergency_contact = form.save(commit=False)
        emergency_contact.employee_id = self.employee_pk
        return super().form_valid(form)


class EmergencyContactUpdateView(EmergencyContactBaseView, UpdateView):
    template_name = template_base + 'update.html'
    form_class = EmergencyContactUpdateForm


class EmergencyContactDeleteView(EmergencyContactBaseView, DeleteView):
    pass
