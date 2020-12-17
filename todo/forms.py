from django import forms
from django.core import validators


class ToDoForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control bg-dark border-dark text-white", "placeholder": "Title"}),
        validators=[
            validators.MinLengthValidator(10, "minimum title length is 10 characters!"),
            validators.MaxLengthValidator(40, "maximum title length is 40 characters!")
        ]
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"cols": "30", "rows": "10", "class": "form-control bg-dark border-dark text-white",
                   "placeholder": "Description", "style": "resize: none;"}),
        validators=[
            validators.MinLengthValidator(20, "minimum description length is 20 characters!"),
            validators.MaxLengthValidator(400, "maximum description length is 400 characters!")
        ]
    )
