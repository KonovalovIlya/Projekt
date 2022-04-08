from django.contrib import admin
from advertisements_app.models import Advertisement, User, Category
# Register your models here.
@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class AdvertisementAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class AdvertisementAdmin(admin.ModelAdmin):
    pass