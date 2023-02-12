from django.shortcuts import render


def main(request):
    pass
    return render(request, 'main.html')



def football(request):
    pass
    return render(request, 'football.html')


def hockey(request):
    pass
    return render(request, 'hockey.html')



def basketball(request):
    pass
    return render(request, 'basketball.html')


def error_404_view(request, exception):
    pass
    return render(request, '404.html')
