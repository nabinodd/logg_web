from django.db import models

class Visitor(models.Model):
    name=models.CharField(max_length=100)
    addr=models.CharField(max_length=100)
    instu=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    remarks=models.CharField(max_length=200)
    date=models.CharField(max_length=15)
    chk_in_time=models.CharField(max_length=20)
    chk_out_time=models.CharField(max_length=20)
    img_name=models.CharField(max_length=50)

