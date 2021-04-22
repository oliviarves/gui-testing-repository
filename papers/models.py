from django.db import models
from django.db.models import CASCADE
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


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=CASCADE, null=True, blank=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return 'Category ' + self.name


class Image(models.Model):
    path = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Image {} {}'.format(self.category.  name, self.path)
