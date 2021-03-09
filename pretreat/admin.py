from pathlib import Path
from django.conf import settings
from django.contrib import admin
from .models import AppInfo
from .preprocess import Process

# admin.site.register(AppMoreInfo)
# Register your models here.
@admin.register(AppInfo)
class AppinfoAdmin(admin.ModelAdmin):
    fields = ['apk_file']
    list_display = ('name','package_name','version_name','version_code','avater','md5','apk_file')

    def save_model(self, request, obj, form, change):
        p = Process()
        obj.md5 = p.get_md5(request.FILES['apk_file'])
        super().save_model(request, obj, form, change)
        package_name, version_name, version_code, launch_activity, \
        min_sdk_version, target_sdk_version, application_label = p.get_apk_base_info(str(obj.apk_file.path))
        obj.name = application_label
        obj.package_name = package_name
        obj.version_code = version_code
        obj.version_name= version_name
        obj.save()
