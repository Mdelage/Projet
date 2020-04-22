# coding=utf-8
from django import forms


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre addresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé", required=False)

    # def clean_message(self):
    #     message = self.cleaned_data['message']
    #     if "pizza" in message:
    #         raise forms.ValidationError("Pas de pizza svp")
    #
    #     return message

    # def clean(self):
    #     cleaned_data = super(ContactForm, self).clean()
    #     sujet = cleaned_data.get('sujet')
    #     message = cleaned_data.get('message')
    #
    #     if sujet and message: #vérifie si sujet et message sont valides
    #         if "pizza" in sujet and "pizza" in message:
    #             raise forms.ValidationError("Pas de pizza dans le sujet et le message")
    #
    #     return cleaned_data

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message:  # vérifie si sujet et message sont valides
            if "pizza" in sujet and "pizza" in message:
                self.add_error("message", "Pas de pizza dans le sujet et le message")

        return cleaned_data
