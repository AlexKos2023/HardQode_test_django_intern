from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def has_access(self, user):
        if user.groups.filter(product=self).exists() and self.start_date < timezone.now():
            return True
        else:
            return False


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_link = models.URLField()


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    min_users = models.PositiveSmallIntegerField()
    max_users = models.PositiveSmallIntegerField()
    users = models.ManyToManyField(User, related_name='groups_related')
