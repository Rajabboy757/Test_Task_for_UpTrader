from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=30)
    is_main = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu', kwargs={'menu_id': self.pk})
