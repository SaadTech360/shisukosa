from django   import forms
from .models  import Events,Gallery

class EventsCreationForm(forms.ModelForm):
    
    class Meta:
        model = Events
        fields = ['title','image','description','status','location','date','time']
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'}),
            'time':forms.TimeInput(attrs={'type':'time'}),
        }

class GalleryUploadForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title','description','image']