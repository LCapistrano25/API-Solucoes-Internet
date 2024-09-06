from django.db import models
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name']  # Default ordering by name

    def __str__(self) -> str:
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=80, unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Prioridade"
        verbose_name_plural = "Prioridades"
        ordering = ['name']  # Default ordering by name

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=250)
    participants = models.ForeignKey(Group, on_delete=models.PROTECT, related_name="tasks")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="tasks")
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name="tasks")
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ['date_start']  # Default ordering by start date

    def __str__(self) -> str:
        return self.title

    def clean(self):
        # Ensure that date_end is not earlier than date_start
        if self.date_end < self.date_start:
            raise ValidationError(_('End date cannot be earlier than start date.'))

    def save(self, *args, **kwargs):
        # Trigger validation before saving
        self.clean()
        super().save(*args, **kwargs)
