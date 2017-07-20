from django import forms
from .validators import validate_url, validate_dot_com

class SubmitUrlForm(forms.Form):
    url = forms.CharField(
                label='',
                validators=[validate_url],
                widget=forms.TextInput(
                        attrs={
                            "placeholder": "Long URL",
                            "class":"form-control"
                            },
                    ),
                )

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     print(cleaned_data)
    #
    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     print("cleaned_data")
    #     return url
