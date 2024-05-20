import uuid
from django.db.models import Sum
from django.conf import settings
from django.db import models, transaction
from django.db import models
from django.contrib.auth.models import User


class Container(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    total_dinar = models.FloatField()
    total_dollar = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'القاصات'
