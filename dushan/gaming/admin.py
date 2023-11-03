from django.contrib import admin
from .models import StoreItemDes  # import storeitemdes class or table
# import StoreNewGamesSlide class or table
from .models import StoreNewGamesSlide
# Register your models here.

admin.site.register(StoreItemDes)  # register table on admin site
admin.site.register(StoreNewGamesSlide)  # register table on admin site
