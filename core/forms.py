from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', required=True)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)