from django import template
from ..models import Consert
register=template.Library()

@register.inclusion_tag("partials/favorite.html")
def favorites(user,consert):
    return {
        "consert":consert.favorites.user==user
    }
