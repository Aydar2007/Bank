from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from apps.users.models import User

class Transfers(models.Model):
    who_transfer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="Who_transfer",
        verbose_name="Кто отправил"
    )
    who_get = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="who_get",
        verbose_name="Получатель"
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Статус"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Произведен'
    )
    how_much = models.CharField(
        max_length=99999,
        verbose_name="Сумма"
    )
    def __str__(self):
        return self.who_transfer
    
    class Meta:
        verbose_name = "Истории"
        verbose_name_plural = "История"
