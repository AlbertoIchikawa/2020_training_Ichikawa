from django.db import models


# Create your models here.
class User(models.Model):
    id_user = models.AutoField('ID', primary_key=True)
    name = models.CharField('name', max_length=60)
    email = models.CharField('email', max_length=255, unique=True)
    password = models.CharField('password', max_length=20)

    class Meta:
        db_table = 'user'