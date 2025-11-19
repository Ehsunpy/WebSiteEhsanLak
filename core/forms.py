from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="نام",
        max_length=120,
        widget=forms.TextInput(
            attrs={"placeholder": "نام شما", "class": "input-field"}
        ),
    )
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(
            attrs={"placeholder": "example@email.com", "class": "input-field"}
        ),
    )
    topic = forms.CharField(
        label="موضوع",
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "موضوع همکاری", "class": "input-field"}
        ),
    )
    message = forms.CharField(
        label="پیام",
        widget=forms.Textarea(
            attrs={"rows": 5, "placeholder": "متن پیام", "class": "input-field"}
        ),
    )

