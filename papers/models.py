from django.db import models
from django_mysql.models import EnumField


class Paper(models.Model):

    author = models.TextField()
    title = models.TextField()
    year = models.IntegerField()
    source_title = models.CharField(max_length=255)

    DOCUMENT_TYPE_OPTIONS = [
        ('ar', 'Article'),
        ('co', 'Conference Paper'),
        ('bc', 'Book Chapter'),
        ('bo', 'Book'),
        ('mt', 'Master Thesis'),
        ('pt', 'PhD Thesis'),
        ('ot', 'Other'),
    ]
    # document_type = models.CharField(max_length=2, choices=DOCUMENT_TYPE_OPTIONS, default=)
    document_type = EnumField(choices=DOCUMENT_TYPE_OPTIONS, default='ot')
    abstract = models.TextField()
    doi = models.CharField(max_length=100)
    # bibtex = models.JSONField()
