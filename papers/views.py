import itertools
from os import listdir
from os.path import isfile, join

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django_filters.views import FilterView

from papers.forms import PaperSearchForm
from papers.models import Paper, Image
from papers.filters import PaperFilterSet, ResultsFilterSet
from repository.settings import BASE_DIR


class PapersList(FilterView):
    paginate_by = 50
    template_name = 'papers_list.html'
    # context_object_name = 'page_obj'
    # queryset = Paper.objects.all().order_by("year")
    # form_class = PaperFilterSet().get_form_class()
    filterset_class = PaperFilterSet
    model = Paper

    # def get_form(self, form_class=None):
    #     return super().get_form(form_class)
    #
    # def get_initial(self):
    #     initials = self.request.GET.copy()
    #     if "document_type" in initials:
    #         pass
    #     return initials

    def get_context_data(self, **kwargs):
        context_data = super(PapersList, self).get_context_data(**kwargs)
        number = context_data['page_obj'].number
        paginator = context_data['paginator']
        left = right = 1
        if number == paginator.num_pages:
            left = 2
        if number == 1:
            right = 2
        page_range = range(max(number - left, 1), min(number + right, paginator.num_pages)+1)
        context_data['range'] = page_range
        context_data['document_type'] = {doc_type[0]:doc_type[1] for doc_type in Paper.DOCUMENT_TYPE_OPTIONS}
        context_data['values'] = self.request.GET
        return context_data

    def get_queryset(self):
        qs = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=qs)
        return self.filterset.qs
        # if self.request.GET:
        #     filtered_model_list = PaperFilterSet(self.request.GET, queryset=self.queryset)
        #     return filtered_model_list.qs
        # else:
        #     return super(PapersList, self).get_queryset()


class Results(FilterView):
    template_name = "results.html"
    filterset_class = ResultsFilterSet

    # GRAPHS = list(itertools.chain.from_iterable([[f for f in listdir(p) if isfile(join(p, f))] for p in paths]))

    # def get_context_data(self, **kwargs):
    #     context_data = super(Results, self).get_context_data(**kwargs)
    #     return context_data


class Home(TemplateView):
    template_name = "home.html"


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def keywords(request):
    return redirect("{}data/Keywords.xlsx".format(settings.STATIC_URL))


def bibliography(request):
    return redirect("{}data/Bib.pdf".format(settings.STATIC_URL))

