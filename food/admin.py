from django.contrib import admin
from food.models import Product,Category,Cart
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
