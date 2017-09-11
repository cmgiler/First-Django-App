from django import template

register = template.Library()

# Custom template filter
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    :param value: A string
    :param arg: Pattern to be cut from string
    :return: String with pattern cut
    """

    return value.replace(arg, '')

## Use method decorator instead
# register.filter(name='cut', filter_func=cut)
