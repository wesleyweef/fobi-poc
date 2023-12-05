from django import forms
from django.utils.translation import gettext_lazy as _
from fobi.base import BasePluginForm, get_theme

theme = get_theme(request=None, as_instance=True)


class HTTPRepostForm(forms.Form, BasePluginForm):
    """Form for ``HTTPRepostPlugin``."""

    plugin_data_fields = [
        ("endpoint_url", ""),
    ]

    endpoint_url = forms.URLField(
        label=_("Endpoint URL"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"class": theme.form_element_html_class}
        ),
    )


class HTTPRepostFormWizard(forms.Form, BasePluginForm):
    """Form for ``HTTPRepostPlugin``."""

    plugin_data_fields = [
        ("endpoint_url", ""),
        ("key_auth", ""),
    ]

    endpoint_url = forms.URLField(
        label=_("Endpoint URL"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"class": theme.form_element_html_class}
        ),
    )

    key_auth = forms.CharField(
        label=_("Key Auth"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"class": theme.form_element_html_class}
        ),
    )
