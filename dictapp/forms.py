from django import forms

class Word(forms.Form):
    wordInput = forms.CharField(max_length=255)
    
    wordInput.widget.attrs.update({'class': 'form-control'})
        