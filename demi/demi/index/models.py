from django.db import models

# Create your models here.


class User(models):
    name = models.CharField(max_length=30, unique=True, null=False, verbose_name="姓名")
    password = models.CharField(max_length=11, null=False, verbose_name="密码")

    class Meta:
        db_table = "users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name