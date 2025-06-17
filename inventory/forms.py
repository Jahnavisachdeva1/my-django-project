from django import forms
from .models import InventoryManagement

class InventoryManagementForm(forms.ModelForm):
    rc_upload = forms.FileField(required=False)
    insurance_copy = forms.FileField(required=False)
    number_plate_photo = forms.FileField(required=False)
    branding_photo_1 = forms.FileField(required=False)
    branding_photo_2 = forms.FileField(required=False)
    branding_photo_3 = forms.FileField(required=False)
    branding_photo_4 = forms.FileField(required=False)

    class Meta:
        model = InventoryManagement
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get('rc_upload'):
            instance.rc_upload = self.cleaned_data['rc_upload'].read()
        if self.cleaned_data.get('insurance_copy'):
            instance.insurance_copy = self.cleaned_data['insurance_copy'].read()
        if self.cleaned_data.get('number_plate_photo'):
            instance.number_plate_photo = self.cleaned_data['number_plate_photo'].read()
        if self.cleaned_data.get('branding_photo_1'):
            instance.branding_photo_1 = self.cleaned_data['branding_photo_1'].read()
        if self.cleaned_data.get('branding_photo_2'):
            instance.branding_photo_2 = self.cleaned_data['branding_photo_2'].read()
        if self.cleaned_data.get('branding_photo_3'):
            instance.branding_photo_3 = self.cleaned_data['branding_photo_3'].read()
        if self.cleaned_data.get('branding_photo_4'):
            instance.branding_photo_4 = self.cleaned_data['branding_photo_4'].read()
        if commit:
            instance.save()
        return instance