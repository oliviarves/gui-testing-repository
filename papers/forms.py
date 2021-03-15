from .models import Paper
from django import forms


class PaperSearchForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(PaperSearchForm, self).__init__(*args, **kwargs)
        self.query = Paper.objects.all()

    search_title = forms.CharField(
        required=False,
        label='Search name or surname!',
        widget=forms.TextInput(attrs={'placeholder': 'search title here!'})
    )

    search_year_exact = forms.IntegerField(
        required=False,
        label='Search year (exact match)!'
    )

    # search_age_min = forms.IntegerField(
    #     required = False,
    #     label='Min age'
    # )
    #
    # search_age_max = forms.IntegerField(
    #   required = False,
    #   label='Max age'
    # )