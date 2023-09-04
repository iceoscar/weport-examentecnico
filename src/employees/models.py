import uuid

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models

from _project.models import TimeStampAbstract


def file_user_path(instance, filename):
    return f'employee_{instance.id}/{filename}'


class Employee(TimeStampAbstract):
    BLOOD_TYPES = (
        ('A +', 'A +'),
        ('A -', 'A -'),
        ('B +', 'B +'),
        ('B -', 'B -'),
        ('AB +', 'AB +'),
        ('AB -', 'AB -'),
        ('O +', 'O +'),
        ('O -', 'O -')
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    first_name = models.CharField(
        'Nombre(s)',
        max_length=128
    )
    last_name = models.CharField(
        'Apellidos',
        max_length=128
    )
    type_blood = models.CharField(
        'Tipo de Sangre',
        max_length=4,
        choices=BLOOD_TYPES,
        default='',
        blank=True
    )
    photo = models.ImageField(
        'Foto del empleado',
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to=file_user_path,
        default=f'{settings.MEDIA_ROOT}/employee-default.png',
        blank=True
    )
    qr_code_url = models.CharField(
        max_length=128,
        blank=False
    )
    qr_code = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to=file_user_path,
        editable=False
    )
    is_active = models.BooleanField(
        default=True
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
