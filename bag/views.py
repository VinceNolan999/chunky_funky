"""
views for the bag app
"""

from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ a view to return the bag page """

    return render(request, 'bag/bag.html')
