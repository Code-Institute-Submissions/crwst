from django.shortcuts import render
from django.contrib import messages

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return an about page """
    return render(request, 'home/about.html')


def page_not_found_view(request, exception=None):
    """ A view to render custom 404 not found page """
    if exception:
        messages.error(request, f"error encountered: {exception}")

    return render(request, 'errors/404.html')


def permission_denied_view(request, exception=None):
    """ A view to render custom 403 permission denied view """
    if exception:
        messages.error(request, f"error encountered: {exception}")

    return render(request, 'errors/403.html')


def error_view(request, exception=None):
    """ A view to render custom 500 error view """
    if exception:
        messages.error(request, f"error encountered: {exception}")

    return render(request, 'errors/500.html')
