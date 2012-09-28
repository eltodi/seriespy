# coding: utf-8
from django import forms
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit, Button

from mensajes.models import Mensaje


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        exclude = ['fecha', 'visto', 'remitente']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                '',
                "destinatario",
                "texto"
            ),
            FormActions(
                Submit('submit', 'Enviar', css_class='btn btn-success')
            )
        )
        super(MensajeForm, self).__init__(*args, **kwargs)