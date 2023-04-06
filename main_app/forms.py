from django.forms import ModelForm
from .models import Updates

class UpdatesForm(ModelForm):
    class Meta:
        model = Updates
        fields = ['date', 'service']