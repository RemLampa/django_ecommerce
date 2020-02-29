from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (('S', 'Stripe'), ('P', 'Paypal'))


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "1234 Main St.",
            "class": "form-control"
        }))
    apartment_address = forms.CharField(required=False,
                                        widget=forms.TextInput(attrs={
                                            "placeholder":
                                            "Apartment or suite",
                                            "class":
                                            "form-control"
                                        }, ))
    country = CountryField(
        blank_label="Select Country", ).formfield(widget=CountrySelectWidget(
            attrs={"class": "custom-select d-block w-100"}), )
    zip = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"}))
    same_shipping_address = forms.BooleanField(
        widget=forms.CheckboxInput,
        required=False,
    )
    save_info = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=PAYMENT_CHOICES,
    )


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Promo Code",
            "aria-label": "Recipient's username",
            "aria-describedby": "basic-addon2"
        }))
