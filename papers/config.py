from django.apps import AppConfig


class PapersAppConfig(AppConfig):
    name = 'papers'

    def ready(self):
        from papers import template_tags  # noqa