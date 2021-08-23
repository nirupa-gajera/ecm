from django.contrib import admin
from .models import register

# Register your models here.
from .models import *

admin.site.register(register)
admin.site.register(product)
admin.site.register(person)
admin.site.register(category)
admin.site.register(subcategory)
admin.site.register(productss)
admin.site.register(vendor)
admin.site.register(cart)
admin.site.register(address)
admin.site.register(buy123)
admin.site.register(admin1)
admin.site.register(country)
admin.site.register(state)
admin.site.register(city)
admin.site.register(wallet)
admin.site.register(voucher)