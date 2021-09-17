from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Contract (models.Model):
    Start_Date=models.DateTimeField(auto_now_add=True)
    End_Date=models.DateTimeField(auto_now_add=True)

class Dealers (models.Model):
    Name = models.CharField(max_length=15, blank=True)
    SSN = models.PositiveIntegerField( primary_key=True, verbose_name='SSN')
    phone = models.PositiveIntegerField( blank=True)
    Is_owner=models. BooleanField(default=False,blank=True)
    Can_buy_car=models. BooleanField(default=False)
    Can_sign_contract=models. BooleanField(default=False)
    Can_sell_car=models. BooleanField(default=False)
    Can_change_price=models. BooleanField(default=False)
    Contract = models.ManyToManyField(
        Contract, related_name='Dealers', blank=True)
    IS_available=models. BooleanField(default=True)

class Customers (models.Model):
    Name = models.CharField(max_length=15, blank=True)
    SSN = models.PositiveIntegerField( primary_key=True, verbose_name='SSN')
    phone = models.PositiveIntegerField( blank=True)


    

class Industries (models.Model):
    Name = models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Name')
    phone = models.PositiveIntegerField( blank=True)


class Cars (models.Model):
    Model = models.CharField(max_length=15, blank=True)
    Price = models.PositiveIntegerField( blank=True)
    Plate_No =models.CharField(max_length=15, blank=True)
    Customer = models.ForeignKey(Customers, related_name='Cars', on_delete=models.CASCADE, null=True)
    Contract =  models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        
    )
    Industries=models.ForeignKey(Industries, related_name='Cars', on_delete=models.CASCADE)






