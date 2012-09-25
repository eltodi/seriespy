from django import forms
from series.models import *


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


class EpisodioForm(forms.ModelForm):
	class Meta:
		model = Episodio
		exclude = ["serie"]