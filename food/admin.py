from django.contrib import admin
from food.models import OrderItem, Product,Category,Cart,Order,Profile
from atexit import register

# Register your models here.
# admin.site.register(Register)
# admin.site.register(Gujproduct)
# admin.site.register(Southjproduct)
# admin.site.register(Punjabijproduct)
# admin.site.register(Rajsthaniproduct)
# admin.site.register(Indianstreetproduct)
# admin.site.register(Chinesseproduct)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)



