from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from django import forms
from livescore_app.models import Tournament, User, Game
from livescore_app.forms import GameCreateForm

# Create your views here.


def home_view(httprequest):
    allTournaments = Tournament.objects.all()

    context = {
        "allTournaments": allTournaments
    }

    return render(httprequest, 'home.html', context)


def tournamentDetail(httprequest, tournament_id, *args, **kwargs):

    tournament = get_object_or_404(Tournament, id=tournament_id)
    activeGames = Game.objects.all().filter(tournament=tournament_id, status='2')
    upcomingGames = Game.objects.all().filter(tournament=tournament_id, status='1')
    completedGames = Game.objects.all().filter(
        tournament=tournament_id, status='3')

    context = {
        "tournament": tournament,
        "games": {
            "activeGames": activeGames,
            "upcomingGames": upcomingGames,
            "completedGames": completedGames
        }
    }

    # check if register is in get request- if so - check if player should be removed or not
    if 'register' in httprequest.GET:

        loggedInPlayer = httprequest.user
        if httprequest.GET['register'] == 'Register' and loggedInPlayer not in tournament.participants.all():

            tournament.participants.add(httprequest.user)
            context['registration'] = "Added"

            # return redirect('/tournament/'+str(tournament_id),context)
        elif httprequest.GET['register'] == 'Unregister' and loggedInPlayer in tournament.participants.all():

            tournament.participants.remove(httprequest.user)
            context['registration'] = "Removed"
            # return redirect('/tournament/'+str(tournament_id),context)

    return render(httprequest, "tournament_detail.html", context)


def playerDetail(httprequest, player_id, *args, **kwargs):
    player = get_object_or_404(User, id=player_id)
    context = {
        "player": player
    }

    return render(httprequest, "player_detail.html", context)


def gameDetail(httprequest, game_id, *args, **kwargs):
    game = get_object_or_404(Game, id=game_id)
    context = {
        "game": game,
        "game_id": game_id
    }

    return render(httprequest, "game_detail.html", context)


def createGame(httprequest, tournament_id, *args, **kwargs):

    gameForm = GameCreateForm(httprequest.POST or None)

    # get tournament
    tournament = get_object_or_404(Tournament, id=tournament_id)

    error = ""

    # set field values . only players which participate in tournament
    gameForm.fields["player1"].queryset = tournament.participants.all()
    gameForm.fields["player2"].queryset = tournament.participants.all()

    if gameForm.is_valid():
        # create, but do not save game yet
        newGame = gameForm.save(commit=False)
        # add tournament to the game
        newGame.tournament = tournament
    
        # save the game
        if gameForm.cleaned_data["player1"] != gameForm.cleaned_data["player2"]:
            newGame.save()
            gameForm = GameCreateForm()

            gameForm.fields["player1"].queryset = tournament.participants.all()
            gameForm.fields["player2"].queryset = tournament.participants.all()
        else:
            error = "Player 1 & Player 2 can not be the same!"


    context = {
        "form" : gameForm,
        "tournament": tournament,
        "error": error
    }
    return render(httprequest, "game_create.html", context)
