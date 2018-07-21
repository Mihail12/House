from django.contrib import admin
from django import forms
from app.models import AppUser, House, Housemate


class HousemateForm(forms.ModelForm):
    class Meta:
        model = Housemate
        fields = '__all__'

    def clean_apartment(self):
        if self.instance.house_id:
            house = House.objects.get(pk=self.instance.house_id)
            if int(house.apartment_amount) < int(self.cleaned_data['apartment']):
                raise forms.ValidationError(
                    "House: {} has {} apartments".format(house, house.apartment_amount))
        if self.cleaned_data.get('house'):
            apt_in_house = self.cleaned_data['house'].apartment_amount
            if int(apt_in_house) < int(self.cleaned_data['apartment']):
                raise forms.ValidationError("House: {} has {} apartments".format(self.cleaned_data['house'], apt_in_house))
        return self.cleaned_data['apartment']


class HouseInstanceInline(admin.TabularInline):
    form = HousemateForm
    model = Housemate


admin.site.register(AppUser)


@admin.register(Housemate)
class HousematesAdmin(admin.ModelAdmin):
    form = HousemateForm
    list_filter = ('house',)
    fields = ['last_name', 'middle_name', 'first_name', 'birth_date', 'house', 'apartment']


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseInstanceInline]
