" Platzigram views "

#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json


""" Function for datetime """
def datetime_now():
    return datetime.now()\
        .strftime('%b %dth, %Y - %H:%M hrs')


""" Function a greetings """
def hello_world(request):
    return HttpResponse(f'Hello World, {datetime_now()}')


def sort_integer(request):
    #import pdb
    #pdb.set_trace()
    numbers = request.GET['numbers']
    numbers = [int(i) for i in numbers.split(',')]
    numbers_sorted = sorted(numbers)
    data = {
        'status':'ok',
        'numbers': numbers_sorted,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )


def say_hi(request, name, age):
    if age < 12:
        message = f"Sorry {name}, you are not allowed here"
    else:
        message = f"Hello {name}!, welcome to Platzigram"
    return HttpResponse(message)
