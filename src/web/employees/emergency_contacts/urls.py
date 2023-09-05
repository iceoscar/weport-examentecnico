from django.urls import path, include

from .views import (
    EmergencyContactListView,
    EmergencyContactDetailView,
    EmergencyContactCreateView,
    EmergencyContactUpdateView,
    EmergencyContactDeleteView
)


urlpatterns = [
    path('', EmergencyContactListView.as_view(), name='emergency-contact-list'),
    path('alta-contacto-emergencia', EmergencyContactCreateView.as_view(), name='emergency-contact-create'),
    path('<emergency_contact_pk>/', include([
        path('', EmergencyContactDetailView.as_view(), name='emergency-contact-detail'),
        path('actualizar', EmergencyContactUpdateView.as_view(), name='emergency-contact-update'),
        path('baja-contacto-emergencia', EmergencyContactDeleteView.as_view(), name='emergency-contact-delete'),
    ])),
]
