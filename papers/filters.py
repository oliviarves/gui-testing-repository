import django_filters as filters
from .models import Paper


class PaperFilterSet(filters.FilterSet):

    class Meta:
        model = Paper
        fields = {
            'title': ['contains'],
            'year': ['gte', 'lte'],
            'abstract': ['contains']
        }
