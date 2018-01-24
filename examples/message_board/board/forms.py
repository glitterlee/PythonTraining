from django import forms
from django.contrib.auth.models import User
from .models import Message


class NewMessageForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows':'1',
            'class':'form-control',
            'placeholder':'Type your message here.',
        }),
    )
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    class Meta:
        model = Message
        fields = ("user", "text",)
