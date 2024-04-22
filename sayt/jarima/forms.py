from django import forms
from .models import UploadedFile

class BazaForm(forms.Form):
    okpo = forms.CharField(max_length=8)
    inn = forms.CharField(max_length=9)
    nomi = forms.CharField(max_length=400)
    soato = forms.CharField(max_length=20)
    soato4 = forms.CharField(max_length=4)
    soato7 = forms.CharField(max_length=7)
    hisobot_nomi = forms.CharField()
    topshirish_muddati = forms.CharField()
    aniqlangan_sanasi = forms.DateField()
    sababi = forms.CharField(max_length=400)
    # xat_turi = forms.ForeignKey(Xat_turi, on_delete=forms.CASCADE)
    xat_sanasi = forms.DateField()
    chiqib_ketgan = forms.BooleanField()
    izoh = forms.CharField()
    notijorat = forms.BooleanField()
    sudga_chiqarilgan = forms.BooleanField()
    tugatilgan = forms.BooleanField()
    dalolatnoma = forms.BooleanField()
    faoliyatsiz = forms.BooleanField()
    huquqbuzarlik_soni = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['okpo'].widget.attrs.update({'class': 'form-control'})
        self.fields['inn'].widget.attrs.update({'class': 'form-control'})
        self.fields['nomi'].widget.attrs.update({'class': 'form-control'})
        self.fields['soato'].widget.attrs.update({'class': 'form-control'})
        self.fields['soato4'].widget.attrs.update({'class': 'form-control'})
        self.fields['soato7'].widget.attrs.update({'class': 'form-control'})
        self.fields['aniqlangan_sanasi'].widget.attrs.update({'class': 'form-control'})




class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'innx']



