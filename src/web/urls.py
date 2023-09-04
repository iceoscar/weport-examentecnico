from django.urls import path, include

from .views import (
    CustomLoginView,
    CustomLogoutView,
    IndexView
)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('empleados/', include('web.employees.urls'))
]
