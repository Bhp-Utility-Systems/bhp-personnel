from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import KeyPerformanceArea


class KeyPerformanceAreaForm(SiteModelFormMixin, forms.ModelForm):

    def clean(self):
        super().clean()

        weighting = self.cleaned_data.get('weighting')

        kpa_rating = self.cleaned_data.get('kpa_rating')

        if weighting and kpa_rating:
            self.cleaned_data['kpa_score'] = (weighting / 100) * int(kpa_rating)

    class Meta:
        model = KeyPerformanceArea
        fields = '__all__'
