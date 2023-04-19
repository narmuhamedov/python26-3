from django import forms
from . import models


class PhoneForm(forms.ModelForm):
    class Meta:
        model = models.PhoneShop
        fields = "__all__"
        # fields = "title description"
