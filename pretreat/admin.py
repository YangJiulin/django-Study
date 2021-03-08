import hashlib
from pathlib import Path
from django.conf import settings
import os
import re
import subprocess
from django.contrib import admin
from .models import AppBaseInfo, AppMoreInfo

admin.site.register(AppMoreInfo)
# Register your models here.
@admin.register(AppBaseInfo)
class AppinfoAdmin(admin.ModelAdmin):
    fields = ['apk_file']
    list_display = ('md5','apk_file')


    aapt_path = str(Path(os.environ.get('ANDROID_HOME', None)) / 'build-tools/30.0.3/aapt')

    def get_apk_base_info(self,apk_path):  # 获取apk包的基本信息
        p = subprocess.Popen(self.aapt_path + " dump badging %s" % apk_path,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        package_match = re.compile(
            "package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not package_match:
            raise Exception("can't get package,versioncode,version")
        package_name = package_match.group(1)
        version_code = package_match.group(2)
        version_name = package_match.group(3)
        launch_activity_match = re.compile(
            "launchable-activity: name='(\S+)'").search(output.decode())
        if not launch_activity_match:
            raise Exception("can't get launch_activity")
        launch_activity = launch_activity_match.group(1)
        sdk_version_match = re.compile(
            "sdkVersion:'(\S+)'").search(output.decode())
        if not sdk_version_match:
            raise Exception("can't get min_sdk_version")
        min_sdk_version = sdk_version_match.group(1)
        target_sdk_version_match = re.compile(
            "targetSdkVersion:'(\S+)'").search(output.decode())
        if not target_sdk_version_match:
            raise Exception("can't get target_sdk_version")
        target_sdk_version = target_sdk_version_match.group(1)
        application_label_match = re.compile(
            "application-label:'([\u4e00-\u9fa5_a-zA-Z0-9-\S]+)'").search(output.decode())
        if not application_label_match:
            raise Exception("can't get application_label")
        application_label = application_label_match.group(1)
        p.kill()
        return package_name, version_name, version_code, launch_activity, min_sdk_version, target_sdk_version, application_label

    def save_model(self, request, obj, form, change):
        d5 = hashlib.md5()
        for chunk in request.FILES['apk_file'].chunks():
            d5.update(chunk)
        file_md5 = d5.hexdigest()
        obj.md5 = file_md5
        print(file_md5)
        super().save_model(request, obj, form, change)
        package_name, version_name, version_code, launch_activity, \
        min_sdk_version, target_sdk_version, application_label = self.get_apk_base_info(str(settings.BASE_DIR / obj.apk_file.path))
        m = AppMoreInfo(app = obj,name=application_label,package_name = package_name,version_code = version_code,version_name= version_name)
        m.save()
        
