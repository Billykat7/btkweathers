
from django.forms                                   import forms

from crispy_forms.layout                            import Layout
from crispy_forms.bootstrap                         import StrictButton
from crispy_forms.helper                            import FormHelper
from crispy_forms.layout                            import Layout, Fieldset, ButtonHolder, Submit


class ClimateForm(forms.Form):

    class Meta:
        fields = ['city', 'period_start', 'period_end']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            Fieldset(
                'city',
                'period_start',
                'period_end',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
