from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from livescore_app.models import Tournament, User
import logging

# Create your views here.
def home_view(httprequest):
    allTournaments = Tournament.objects.all

    context = {
        "allTournaments": allTournaments
    }
    # my_dict = {
    #     'name': 'frank',
    #     'tournaments': [
    #         {
    #             'name': 'WAG Championship I',
    #             'date': '13.02.2020',
    #             'status': 'complete'
    #         },
    #         {
    #             'name': 'WAG Championship II',
    #             'date': '20.02.2020',
    #             'status': 'complete'
    #         }, 
    #         {
    #             'name': 'WAG Championship III',
    #             'date': '27.02.2020',
    #             'status': 'running'
    #         },
    #         {
    #             'name': 'WAG Championship IV',
    #             'date': '05.03.2020',
    #             'status': 'upcoming'
    #         }
    #     ],
    #     'time': datetime.now()
    # }

    return render(httprequest, 'home.html', context)


def tournamentDetail(httprequest,my_id, *args, **kwargs):
    tournament = get_object_or_404(Tournament, id=my_id)
    context = {
        "tournament": tournament
    }

    return render(httprequest,"tournament_detail.html",context)

def playerDetail(httprequest,my_id,*args, **kwargs):
    player = get_object_or_404(User, id=my_id)
    context = {
        "player": player
    }

    return render(httprequest,"player_detail.html",context)
