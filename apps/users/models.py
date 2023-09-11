from django.contrib.auth.models import AbstractUser, Group, Permission
import secrets
from django.db import models

class User(AbstractUser):
    email = models.EmailField(
        verbose_name="Электронная почта",
        unique=True
    )
    number = models.CharField(
        max_length=15,
        verbose_name="Телефоный номер"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    balance = models.CharField(
        max_length=999999,
        verbose_name="Баланс",
        default=0,
        blank=True,
        null=True,
    )
    id_card = models.CharField(
        max_length=12,
        verbose_name="Номер счета",
        unique=True,
        blank=True,
        null=True,
    )
    username = models.CharField(
    max_length=150,
    unique=True,
    default="admin",  # Добавьте значение по умолчанию
)

    # Добавьте related_name для полей groups и user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name=('Группа'),
        blank=True,
        help_text=(''),
        related_name='admin',  # Задайте здесь свое имя
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=(''),
        related_name='admin',  # Задайте здесь свое имя
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def save(self, *args, **kwargs):
        if not self.id_card:
            self.id_card = secrets.token_hex(6)
        super().save(*args, **kwargs)





