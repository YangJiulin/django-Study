from django.db.models import fields
from django.forms import ModelForm
from .models import AppInfo

class AppinfoForm(ModelForm):
    class Meta:
        model = AppInfo
        fields = ['apk_file']