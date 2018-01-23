from django import forms

from .models import Message


class NewMessageForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows':'1',
            'class':'form-control',
            'placeholder':'Type your message here.',
        }),
    )

    class Meta:
        model = Message
        fields = ("text",)