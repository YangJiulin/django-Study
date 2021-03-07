from django.contrib import admin
from .models import AppBaseInfo

# Register your models here.
class AppinfoAdmin(admin.ModelAdmin):
    fields = ['apk_file']

admin.site.register(AppBaseInfo,AppinfoAdmin)