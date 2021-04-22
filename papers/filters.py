import django_filters as filters
from django.forms import SelectMultiple

from .models import Paper, Image


class PaperFilterSet(filters.FilterSet):

    class Meta:
        model = Paper
        fields = {
            'title': ['contains'],
            'year': ['gte', 'lte'],
            'abstract': ['contains']
        }

    document_type = filters.MultipleChoiceFilter(widget=SelectMultiple, field_name="document_type",
                                                 choices=Paper.DOCUMENT_TYPE_OPTIONS)


class ResultsFilterSet(filters.FilterSet):

    class Meta:
        model = Image
        fields = ('category',)
