from django.contrib import admin
from django import forms
from app.models import AppUser, House, Housemates


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'

    def clean_apartment_amount(self):
        if not (self.cleaned_data['apartment_amount'].isdigit() and int(self.cleaned_data['apartment_amount']) > 0):
            raise forms.ValidationError("apartment is a digit field")
        return self.cleaned_data['apartment_amount']

    def clean_st_number(self):
        if not (self.cleaned_data['st_number'].isdigit() and int(self.cleaned_data['st_number']) > 0):
            raise forms.ValidationError("apartment is a digit field")
        return self.cleaned_data['st_number']


class HousemateForm(forms.ModelForm):
    class Meta:
        model = Housemates
        fields = '__all__'

    def clean_apartment(self):
        if not (self.cleaned_data['apartment'].isdigit() and int(self.cleaned_data['apartment']) > 0):
            raise forms.ValidationError("apartment is a digit field")
        apt_in_house = self.cleaned_data['house'].apartment_amount
        if int(apt_in_house) < int(self.cleaned_data['apartment']):
            raise forms.ValidationError("House: {} has {} apartments".format(self.cleaned_data['house'], apt_in_house))
        return self.cleaned_data['apartment']


class HouseInstanceInline(admin.TabularInline):
    model = Housemates


admin.site.register(AppUser)


@admin.register(Housemates)
class HousematesAdmin(admin.ModelAdmin):
    form = HousemateForm
    list_filter = ('house',)
    fields = ['last_name', 'middle_name', 'first_name', 'birth_date', 'house', 'apartment']


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseInstanceInline]
    form = HouseForm
