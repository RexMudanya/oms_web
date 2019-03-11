from  __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from django.utils.encoding import python_2_unicode_compatible


#variables
phone_regex=RegexValidator(regex='^(?:254|\+254|0)?(7(?:(?:[129][0-9])|(?:0[0-8])|(4[0-1]))[0-9]{6})$',message='Phone number accept number starting with 254/07/+254')


product_types=(
    ('Be','Beverages'),
    ('De','Desserts'),
    ('Dr','Drinks'),
)


deliveryType=(

)


# models
@python_2_unicode_compatible #for python 3.5+ and 2.7
class Customer(models.Model):
    firstname=models.CharField(max_length=50,blank=False)
    lastname=models.CharField(max_length=50,blank=False)
    phone=models.CharField(max_length=15,blank=False,validators=[phone_regex])
    email=models.EmailField()

    def __str__(self):
        return '%s %s %s %s' %(self.firstname,self.lastname,self.phone ,self.email)

    class Meta:
        ordering=['firstname']

@python_2_unicode_compatible
class ProductType(models.Model):
    type=models.CharField(max_length=50,choices=product_types)
    description=models.CharField(max_length=250)

    def __str__(self):
        return self.type

@python_2_unicode_compatible
class Product(models.Model):
    name=models.CharField(max_length=50,unique=True,blank=False)
    productType=models.ForeignKey(ProductType,on_delete=models.PROTECT)
    price=models.FloatField()
    image=models.ImageField(upload_to='media/images/products', default='media/images/None/no-image.png',blank=True, null=True)

    def __str__(self):
        return '%s %s %s ' % (self.name,self.productType,self.price,self.image)

    class Meta:
        ordering=['name']

@python_2_unicode_compatible
class DeliveryType(models.Model):
    type=models.CharField(max_length=50,choices=deliveryType)
    description=models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' %(self.type,self.description)

@python_2_unicode_compatible
class Location(models.Model):
    nameOfLocation=models.CharField(max_length=50)
    longtitude=models.DecimalField(max_digits=22,decimal_places=16,blank=True)
    latitude=models.DecimalField(max_digits=22,decimal_places=16,blank=True)

    def __str__(self):
        return '%s %s %s'%(self.nameOfLocation,self.latitude,self.longtitude)

    class Meta:
        ordering=['nameOfLocation']

@python_2_unicode_compatible
class Offer(models.Model):
    typeOfOffer=models.CharField(max_length=50,blank=False)
    offerDescription=models.CharField(max_length=100,blank=True)
    productId=models.ForeignKey(Product,on_delete=models.PROTECT)
    priceOffer=models.FloatField()

    def __str__(self):
        return '%s %s %s  %s' %(self.typeOfOffer,self.offerDescription,self.productId,self.priceOffer)

    class Meta:
        ordering=['productId']

@python_2_unicode_compatible
class Transaction(models.Model):
    customerId=models.ForeignKey(Customer)
    productId=models.ForeignKey(Product,on_delete=models.PROTECT)
    dateOfTransaction=models.DateTimeField()

    def __str__(self):
        return '%s %s %s %s'%(self.customerId,self.productId,self.dateOfTransaction)

    class Meta:
        ordering=['-dateOfTransaction']


@python_2_unicode_compatible
class Order(models.Model):
    transactionId=models.ForeignKey(Transaction,on_delete=models.CASCADE)
    deliverytype=models.ForeignKey(DeliveryType,on_delete=models.PROTECT)
    placeOfDelivery=models.ForeignKey(Location,on_delete=models.PROTECT)
    timeOfPick=models.TimeField()

    def __str__(self):
        return '%s %s %s %s'%(self.transactionId,self.deliverytype,self.placeOfDelivery,self.timeOfPick)

    class Meta:
        ordering=['timeOfPick']