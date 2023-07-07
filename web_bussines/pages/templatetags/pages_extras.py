# from django import template
# from pages.models import Page

# register = template.Library()


# @register.tag
# def get_page_list():
#     pages = Page.objects.all()
#     return pages

from django import template
from pages.models import Page

register = template.Library()


@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages
