'''
custom template tags for bag
'''
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ calculates subtotal on the checkout bag items"""
    return price * quantity
