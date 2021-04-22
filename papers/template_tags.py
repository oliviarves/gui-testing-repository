from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, None)

@register.filter
def remove_extension(value):
    return value.split('.')[0].replace('/', '_')
