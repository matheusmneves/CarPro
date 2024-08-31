from django import forms
from cars.models import Brand, Car

# class CarForm(forms.Form):
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all())
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     licence_plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     photo = forms.ImageField()
    
#     def save(self):
#         car = Car(
#             model = self.cleaned_data['model'],
#             brand = self.cleaned_data['brand'],
#             factory_year = self.cleaned_data['factory_year'],
#             model_year = self.cleaned_data['model_year'],
#             licence_plate = self.cleaned_data['licence_plate'],
#             value = self.cleaned_data['value'],
#             photo = self.cleaned_data['photo'],
#         )
#         car.save()
#         return car
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 1000:
            self.add_error('value', 'Minimum value is $1,000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2000:
            self.add_error('factory_year', 'Minimum factory year is 2000')
        return factory_year