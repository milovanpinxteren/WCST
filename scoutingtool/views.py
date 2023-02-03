from django.shortcuts import render
from django.http import HttpResponse

from scoutingtool.classes.PlayerSelector import PlayerSelector
from scoutingtool.forms import CritereaSelectorForm


def index(request):
    criterea_selection_form = CritereaSelectorForm()

    context = {'criterea_selection_form': criterea_selection_form}
    return render(request, 'critereaselection.html', context)

def submit_criterea(request):
    if request.method == 'POST':
        criterea_selection_form = CritereaSelectorForm(request.POST)
        if criterea_selection_form.is_valid():
            playerselector = PlayerSelector(criterea_selection_form)
            playerdata = playerselector.get_player_data()
            context = {'playerdata': playerdata}


    return render(request, 'resultspage.html', context)