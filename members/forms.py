from django   import forms
from .models  import Events

class EventsCreationForm(forms.ModelForm):
    
    class Meta:
        model = Events
        fields = ['title','image','description','status','location','date','time']
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'}),
            'time':forms.TimeInput(attrs={'type':'time'}),
        }