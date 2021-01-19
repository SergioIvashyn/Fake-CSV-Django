from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DataSchema(models.Model):
    COMMA = ","
    SEMICOLON = ";"
    PIPE = "|"
    DOUBLE_QUOTE = "\""
    ASTERISK = "*"

    COLUMN_SEPARATOR_CHOICES = (
        (COMMA, _(f"Comma ({COMMA})")),
        (SEMICOLON, _(f"Semicolon ({SEMICOLON})")),
        (PIPE, _(f"Pipe ({PIPE})")),
    )

    STRING_CHARACTER_CHOICES = (
        (DOUBLE_QUOTE, _(f'Double-quote ({DOUBLE_QUOTE})')),
        (ASTERISK, _(f"Asterisk ({ASTERISK})")),
    )

    name = models.CharField(max_length=60, unique=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    column_separator = models.CharField(max_length=1, choices=COLUMN_SEPARATOR_CHOICES, default=SEMICOLON)
    string_character = models.CharField(max_length=1, choices=STRING_CHARACTER_CHOICES, default=DOUBLE_QUOTE)
    date_modified = models.DateTimeField(auto_now=True)

    @property
    def date_modified_format(self):
        return self.date_modified.strftime("%Y-%m-%d")

    def __str__(self):
        return f"{self.pk}-{self.name}"
