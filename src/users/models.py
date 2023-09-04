import uuid
import qrcode
import qrcode.image.svg

from io import BytesIO
from django.core.files import File
from PIL import Image

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models

from django.contrib.auth.models import AbstractUser


def photo_user_path(instance, filename):
    return f'user_{instance.id}/{filename}'


class User(AbstractUser):
    REQUIRED_FIELDS = []
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
    type_blood = models.CharField(
        'Tipo de Sangre',
        max_length=4,
        choices=BLOOD_TYPES,
        default='',
        blank=True
    )
    curp = models.CharField(
        'CURP',
        max_length=18,
        blank=True
    )
    is_rrhh = models.BooleanField(
        '¿El usuario es del departamento de RRHH?',
        default=False
    )
    photo = models.ImageField(
        'Foto del empleado',
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to=photo_user_path,
        default=f'{settings.MEDIA_ROOT}/user-default.png',
        blank=True
    )
    qr_code = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to=photo_user_path,
        editable=False
    )

    def save(self, *args, **kwargs):
        # request.META.HTTP_HOST
        print(kwargs.get('request', None))
        factory = qrcode.image.svg.SvgImage
        qr_code = qrcode.make(self.id, image_factory=factory)
        file_name = 'qr_code.svg'
        stream = BytesIO()
        qr_code.save(stream, 'SVG')
        self.qr_code.save(file_name, File(stream), save=False)

        super().save(*args, **kwargs)
