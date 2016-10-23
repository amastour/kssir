from django import forms 

from shoortner.models import *
from shoortner.validator import *


class URLForm(forms.Form):
    url = forms.URLField(
            label="",
            validators=[validate_url],
            widget= forms.TextInput(
                attrs={
                    "placeholder": "Long Url",
                    "class" :"form-control"
                    }
            )
        )
    