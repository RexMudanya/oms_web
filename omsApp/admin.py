from django.contrib import admin
from omsApp.models import *
from django.contrib.auth.models import User,Group

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['firstname' , 'lastname' ,'phone' ,'email']
    list_filter = ('firstname',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','productType','price','image']


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['type','description']
    # fields = [('firstname','lastname'),('phone','email'),]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['customerId','productId','dateOfTransaction']
    list_filter = ('dateOfTransaction',)


@admin.register(DeliveryType)
class DeliveryTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'description']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['nameOfLocation' ,'longtitude','latitude']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['transactionId','deliverytype','placeOfDelivery','timeOfPick']



@admin.register(Offer)
class Offer(admin.ModelAdmin):
    list_display = ['typeOfOffer','offerDescription', 'productId' ,'priceOffer']


admin.site.site_header='HOTEL ORDERING MANAGEMENT SYSTEM'
admin.site.site_title='HOMS Portal'
admin.site.index_title='PRODUCTS AND SERVICES ADMINISTRATION'

# removing User and Group default models
admin.site.unregister(User)
admin.site.unregister(Group)


