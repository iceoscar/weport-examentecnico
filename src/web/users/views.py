from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import User

from .forms import UserCreateForm, UserUpdateForm


templates_base = 'users/'


class UserBaseView(LoginRequiredMixin):
    model = User


class UserListView(UserBaseView, ListView):
    template_name = templates_base + 'list.html'


class UserDetailView(UserBaseView, DetailView):
    template_name = templates_base + 'detail.html'


class UserCreateView(UserBaseView, CreateView):
    template_name = templates_base + 'create.html'
    form_class = UserCreateForm


class UserUpdateView(UserBaseView, UpdateView):
    template_name = templates_base + 'update.html'
    form_class = UserUpdateForm


class UserCardDetailView(DetailView):
    model = User
    template_name = templates_base + 'card.html'
