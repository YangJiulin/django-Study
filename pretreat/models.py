from django.db import models
from django.conf import settings
import os
from django.utils import timezone
from django.contrib.auth.models import User


class AppBaseInfo(models.Model):
    md5 = models.CharField(max_length=30,primary_key=True)
    apk_file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created',)
    
    def __str__(self) -> str:
        return self.md5



class AppMoreInfo(models.Model):
    app = models.OneToOneField(AppBaseInfo,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField("应用名",max_length=250)
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    avater = models.FilePathField(os.path.join(str(settings.BASE_DIR),'media/avater/default.png'))
    package_name = models.CharField('包名',max_length=250)
    version_code = models.CharField('版本号',max_length=250)
    version_name = models.CharField('版本名',max_length=250)

    class Meta:
        ordering = ('-name',)


    def __str__(self):
        return self.name