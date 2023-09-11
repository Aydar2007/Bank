from django.db import models

from django.contrib.auth.models import AbstractUser
import secrets

# Create your models here.
class Authentication(AbstractUser):
    email = models.EmailField(
        verbose_name="Электронная почта",
        unique=True
    )
    Number = models.CharField(
        max_length=15,
        verbose_name="Телефоный номер"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    money = models.CharField(
        max_length=999999,
        verbose_name="Баланс",
        default=0,
        blank = True, 
        null = True,
    )
    id_card = models.CharField(
        max_length=12,
        verbose_name="Номер счета",
        unique=True,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователь"

    def save(self, *args, **kwargs):
        if not self.wallet_address:
            self.wallet_address = secrets.token_hex(6)
        super().save(*args, **kwargs)
