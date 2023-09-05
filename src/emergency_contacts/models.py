from django.db import models

from _project.models import TimeStampAbstract
from employees.models import Employee


class EmergencyContact(TimeStampAbstract):
    class Meta:
        ordering = ('priority', )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        'Nombre completo',
        max_length=128
    )
    mobile = models.PositiveBigIntegerField(
        'Celular',
    )
    relationship = models.CharField(
        'Parentesco',
        max_length=32
    )
    priority = models.PositiveSmallIntegerField(
        'Prioridad',
        default=1,
        help_text='1 es mayor prioridad'
    )
