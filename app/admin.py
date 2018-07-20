from django.contrib import admin

from app.models import AppUser, House, Housemates

admin.site.register(AppUser)
admin.site.register(House)
admin.site.register(Housemates)