from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Column(models.Model):
    TYPE_NAME_CHOICES = (
        ("name", "Full name"),
        ("job", "Job"),
        ("phone_number", "Phone number"),
        ("company", "Company name"),
        ("sentence", "Text"),
        ("pyint", "Integer"),
        ("address", "Address"),
        ("date", "Date"),
    )
    type_name = models.CharField(max_length=40, unique=True, choices=TYPE_NAME_CHOICES)
    is_ranged = models.BooleanField(default=False)
    is_number = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk}-{self.type_name}"

    def clean(self):
        if all([self.is_number, not self.is_ranged]):
            raise ValidationError(_("\"Number\" column might not be not ranged."))
