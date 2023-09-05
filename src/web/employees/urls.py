from django.urls import path, include

from .views import (
    EmployeeListView,
    EmployeeDetailView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    EmployeeCardDetailView
)


urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee-list'),
    path('alta-empleado', EmployeeCreateView.as_view(), name='employee-create'),
    path('<employee_pk>/', include([
        path('', EmployeeDetailView.as_view(), name='employee-detail'),
        path('actualizar', EmployeeUpdateView.as_view(), name='employee-update'),
        path('baja-empleado', EmployeeDeleteView.as_view(), name='employee-delete'),
        path('contactos-emergencia/', include('web.employees.emergency_contacts.urls'))
    ])),
    path('card/<employee_pk>', EmployeeCardDetailView.as_view(), name='employee-card')
]
