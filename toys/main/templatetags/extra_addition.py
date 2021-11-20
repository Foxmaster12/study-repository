from django import template

register = template.Library()


class Env:
    def __init__(self):
        self.one = 'one'
        self.two = 'two'
        self.three = 'three'


@register.inclusion_tag('main/modify.html')
def get_some_arguments():
    return {'arguments': ['first', 'second', 'third'],
            'facts': Env()}
