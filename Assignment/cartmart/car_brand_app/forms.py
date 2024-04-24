from django import forms
from car_brand_app.models import Brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'