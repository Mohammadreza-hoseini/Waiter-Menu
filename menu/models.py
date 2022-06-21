from django.db import models
from django.conf import settings


class Desk(models.Model):
    code = models.CharField(max_length=16, null=False, blank=False)
    title = models.CharField(max_length=64, null=False, blank=False)
    waiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.title}"


class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.title


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)


class Requests(models.Model):
    desk = models.ForeignKey(Desk, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)

