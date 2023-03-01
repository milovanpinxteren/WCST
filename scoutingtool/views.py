from django.shortcuts import render
from django.http import HttpResponse

from scoutingtool.classes.PlayerSelector import PlayerSelector
from scoutingtool.classes.VisualizationMaker import VisualizationMaker
from scoutingtool.forms import CritereaSelectorForm


def index(request): #show the form where users can specify what kind of player they want
    criterea_selection_form = CritereaSelectorForm()

    context = {'criterea_selection_form': criterea_selection_form}
    return render(request, 'critereaselection.html', context)

def submit_criterea(request): #when user submits the form
    if request.method == 'POST':
        criterea_selection_form = CritereaSelectorForm(request.POST)
        if criterea_selection_form.is_valid():
            playerselector = PlayerSelector(criterea_selection_form)
            selected_players, criterea_list = playerselector.sort_players()
            visualizationmaker = VisualizationMaker()
            visualizations = visualizationmaker.make_visualizations(selected_players, criterea_list)


            context = {'playerdata': visualizations}


    return render(request, 'resultspage.html', context)