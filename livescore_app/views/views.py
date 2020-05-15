from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home_view(httprequest):
    my_dict = {
        'name': 'frank',
        'tournaments': [
            {
                'name': 'WAG Championship I',
                'date': '13.02.2020',
                'status': 'complete'
            },
            {
                'name': 'WAG Championship II',
                'date': '20.02.2020',
                'status': 'complete'
            }, 
            {
                'name': 'WAG Championship III',
                'date': '27.02.2020',
                'status': 'running'
            },
            {
                'name': 'WAG Championship IV',
                'date': '05.03.2020',
                'status': 'upcoming'
            }
        ],
        'time': datetime.now()
    }

    return render(httprequest, 'home.html', my_dict)
