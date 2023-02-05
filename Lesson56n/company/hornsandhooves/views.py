from django.shortcuts import render
from django.http import Http404

def main(request):
    try:
        pass
        return render(request, 'main.html')
    except Http404:
        raise Http404('Page does not exist')


def about(request):
    try:
        pass
        return render(request, 'about.html')
    except Http404:
        raise Http404('Page does not exist')

def contacts(request):
    try:
        pass
        return render(request, 'contacts.html')
    except Http404:
        raise Http404('Page does not exist')

def management(request):
    try:
        pass
        return render(request, 'management.html')
    except Http404:
        raise Http404('Page does not exist')

def news(request):
    try:
        pass
        return render(request, 'news.html')
    except Http404:
        raise Http404('Page does not exist')
