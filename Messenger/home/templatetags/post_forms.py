from django import template
from ..models import User_Post

register = template.Library()

@register.inclusion_tag('inclusion_tags/post_form_tag.html', takes_context=True)
def form_for_post(context: dict):
    # form = context["form"]
    # print("context =", context)
    return {
        'form': context.get("form"),
        'form_name': context.get("form_name")
    }
# {% form_for_post context %}