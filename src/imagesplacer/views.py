from django import forms
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render


class ImageForm(forms.Form):
    """Form to validate requested placeholder image."""
    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)


def placeholder(request, width, height):
    form = ImageForm({'height': height, 'width': width})
    if form.is_valid():
        height = form.cleaned_data['height']
        width = form.cleaned_data['width']
        return HttpResponse('Ok')
    else:
        return HttpResponseBadRequest('Invalid Image Request')

def index(request):
    return HttpResponse('Hello World')
