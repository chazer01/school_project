from django.db import models


class Groups(models.Model):
    group_name = models.CharField(max_length=100)
    group_type = models.CharField(max_length=100)



