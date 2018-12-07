from django import template

register = template.Library()

@register.filter
def dictkey(data, value):
	return data[value]