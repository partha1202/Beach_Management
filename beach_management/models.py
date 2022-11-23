from django.db import models

class EmpModel(models.Model):
    customer_id=models.IntegerField(primary_key = True)
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    pincode=models.IntegerField()
    age=models.IntegerField()
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    membership_card=models.BooleanField()
    class Meta:
        db_table="customers"
