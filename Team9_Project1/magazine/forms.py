from django import forms

class ContactUsForm(forms.Form):
    fullname = forms.CharField(label='Full-Name', max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
