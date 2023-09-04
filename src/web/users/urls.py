from django.urls import path, include

from .views import (
    UserListView,
    UserDetailView,
    UserCreateView,
    UserUpdateView,
    UserCardDetailView,
)


urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<pk>/', include([
        path('', UserDetailView.as_view(), name='user-detail'),
        path('alta-empleado', UserCreateView.as_view(), name='user-create'),
        path('actualizar', UserUpdateView.as_view(), name='user-update'),
    ])),
    path('card/<pk>', UserCardDetailView.as_view(), name='user-card')
]
