from django.db.models import fields
from django.forms import ModelForm
from .models import AppBaseInfo

class AppinfoForm(ModelForm):
    class Meta:
        model = AppBaseInfo
        fields = ['apk_file']