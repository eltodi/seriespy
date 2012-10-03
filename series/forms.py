from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from crispy_forms.bootstrap import FormActions
from series.models import *


class BuscaSerieForm(forms.Form):
    titulo = forms.CharField(max_length = 50)

    def clen(self):
        return self.cleaned_data


class SerieForm(forms.Form):
    titulo = forms.CharField(max_length = 38)
    temporadas = forms.IntegerField()
    argumento = forms.CharField(required=False)

    def clean_temporadas(self):
        if self.cleaned_data["temporadas"] > 5:
            raise forms.ValidationError("Demasiadas Temporadas")
        return self.cleaned_data["temporadas"]


    def clean_titulo(self):
        if "CSI" in self.cleaned_data["titulo"]:
            raise forms.ValidationError("Meh..")
        return self.cleaned_data["titulo"]


    def clean(self):
        if self.cleaned_data.get("titulo","") == u"True Blood" and self.cleaned_data.get("temporadas","") == 3:
            raise forms.ValidationError(u"True Blood tiene 5 temporadas")
        return self.cleaned_data


class SerieForm2(forms.ModelForm):
    class Meta:
        model = Serie
        exclude = ["slug"]
        # exlude es para decir que campos queremos que no aparezcan en  formulario


class SerieForm3(forms.ModelForm):
    class Meta:
        model = Serie
        exclude = ['slug', 'genero', 'imdb_id', 'min_cover', 'mini_plot']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Obligatorio',
                "titulo",
                "rating"
            ),
            Fieldset(
                u'Produccion',
                "director",
                "productora",
                "estado",
                "year"
            ),
            Fieldset(
                'Cartel',
                "cover",
                "plot"
            ),
            FormActions(
                Submit('submit', 'Guardar', css_class='btn btn-success')
            )
        )
        super(SerieForm3, self).__init__(*args, **kwargs)


class SerieEditar(forms.ModelForm):
    class Meta:
        model = Serie
        exclude = ['slug', 'genero', 'imdb_id', 'min_cover', 'mini_plot']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Obligatorio',
                "titulo",
                "rating"
            ),
            Fieldset(
                u'Produccion',
                "director",
                "productora",
                "estado",
                "year"
            ),
            Fieldset(
                'Cartel',
                "cover",
                "plot"
            ),
            FormActions(
                Submit('submit', 'Guardar', css_class='btn btn-success')
            )
        )
        super(SerieEditar, self).__init__(*args, **kwargs)


class EpisodioForm(forms.ModelForm):
    class Meta:
        model = Episodio
        exclude = ["serie"]








