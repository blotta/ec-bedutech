from django.shortcuts import render
from django.http import HttpResponse

import calendar
from calendar import HTMLCalendar

from datetime import datetime

def say_hello(request):
    month = list(calendar.month_name)[5]
    now = datetime.now()

    cal = HTMLCalendar().formatmonth(now.year, now.month, True)

    time = now.strftime('%H:%M')
    vm = {
        'name': 'Lucas',
        'month': month,
        'cal': cal,
        'time': time
    }
    return render(request, 'playground/hello.html', vm)