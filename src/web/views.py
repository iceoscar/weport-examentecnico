from django.contrib.auth.views import LoginView, LogoutView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    next_page = '/login/'


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        return redirect('employee-list')
