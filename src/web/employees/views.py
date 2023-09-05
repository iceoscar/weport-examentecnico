import qrcode
import qrcode.image.svg

from io import BytesIO
from django.core.files import File

from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from employees.models import Employee

from .forms import EmployeeCreateForm, EmployeeUpdateForm, EmployeeDeleteForm


templates_base = 'employees/'


class EmployeeBaseView(LoginRequiredMixin):
    model = Employee
    pk_url_kwarg = 'employee_pk'

    def get_success_url(self):
        pk = self.object.pk
        return reverse('employee-detail', kwargs={'employee_pk': pk})


class EmployeeListView(EmployeeBaseView, ListView):
    template_name = templates_base + 'list.html'
    ordering = '-is_active'


class EmployeeDetailView(EmployeeBaseView, DetailView):
    template_name = templates_base + 'detail.html'


class EmployeeCreateView(EmployeeBaseView, CreateView):
    template_name = templates_base + 'create.html'
    form_class = EmployeeCreateForm

    def form_valid(self, form):
        self.object = form.save()
        employee = self.object
        factory = qrcode.image.svg.SvgImage
        url_qr_code = f"{self.request.META['HTTP_ORIGIN']}/empleados/card/{employee.pk}"
        qr_code = qrcode.make(url_qr_code, image_factory=factory)
        file_name = 'qr_code.svg'
        stream = BytesIO()
        qr_code.save(stream, 'SVG')
        employee.qr_code.save(file_name, File(stream), save=False)
        return super().form_valid(form)


class EmployeeUpdateView(EmployeeBaseView, UpdateView):
    template_name = templates_base + 'update.html'
    form_class = EmployeeUpdateForm


class EmployeeDeleteView(EmployeeBaseView, UpdateView):
    template_name = templates_base + 'delete.html'
    form_class = EmployeeDeleteForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.is_active = False
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('employee-list')


class EmployeeCardDetailView(DetailView):
    model = Employee
    pk_url_kwarg = 'employee_pk'
    template_name = templates_base + 'card.html'
