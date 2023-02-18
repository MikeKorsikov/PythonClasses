from django.shortcuts import render
import datetime


def main(request):
    currentDateAndTime = datetime.datetime.now()
    hour = currentDateAndTime.hour + 1
    print(hour)
    if 5 <= hour < 12:
        response = ' Доброго ранку, everybody!'
    elif 12 <= hour < 18:
        response = 'Доброго дня, everybody!'
    elif 18 <= hour < 23:
        response = 'Доброго вечора, everybody!'
    else:
        response = 'Надобраніч, everybody!'

    context = {
        'greeting': response
    }
    return render(request, 'main.html', context=context)


def error_404_view(request, exception):
    pass
    return render(request, '404.html')
