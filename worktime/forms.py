from django.forms import DateField, ModelForm

from config import settings
from worktime.models import DayData


class DayDataForm(ModelForm):
    date_of_birth = DateField(input_formats=settings.DATE_INPUT_FORMAT)

    class Meta:
        model = DayData
