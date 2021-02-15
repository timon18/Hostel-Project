from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
from .models import Reservation, Room

class ReservForms(forms.ModelForm):
    def filter(self, cat):
        self.fields["room_number"] = forms.ModelChoiceField(queryset=Room.objects.filter(works = True).filter(room_category = cat))
        self.id = cat
        print(self.fields)
    

    class Meta:
        model = Reservation
        fields = ['check_in_date', 'check_out_date', 'room_number']
        
    
    def clean_check_in_date(self):
        data = self.cleaned_data['check_in_date']
        
        #Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом). 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
    
        #Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
    
        # Помните, что всегда надо возвращать "очищенные" данные.
        return data