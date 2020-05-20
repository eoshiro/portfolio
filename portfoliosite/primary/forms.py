from django import forms
from primary.models import Contact
from django.core.files.images import get_image_dimensions
from django.core.mail import send_mail, BadHeaderError

class ContactForm(forms.ModelForm):

    class Meta():
        model = Contact
        fields = ('Name','Email','message',)

        widgets = {
            'Name':forms.TextInput(attrs={'class':'textinputclass'}),
            'message':forms.Textarea(attrs={'class':'message-container'}),
            'Email':forms.EmailInput()
        }
