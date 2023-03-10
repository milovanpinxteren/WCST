from scoutingtool.classes.FilterPlayers import FilterPlayers
from scoutingtool.classes.PlayerSorter import PlayerSorter
from scoutingtool.classes.VisualizationMaker import VisualizationMaker
from scoutingtool.models import GeneralPlayerInfo


class PlayerSelector():
    def __init__(self, criterea_selection_form):
        self.handle_form(criterea_selection_form)
        self.query_players()
        self.sort_players()

    def handle_form(self, criterea_selection_form): #change input to sorted list of dicts with critirea and weights
        self.criterea_list = []
        for field in criterea_selection_form.fields:
            if not "_importance" in field:
                value = criterea_selection_form[field].value()
                try:
                    importance = int(criterea_selection_form[field + '_importance'].value())
                except KeyError: #for position and age, no importance passed by user, highest importance by default
                    importance = 6
                criterium_dict = {'field': field, 'value': value, 'importance': importance}
                self.criterea_list.append(criterium_dict)
        def sortingFunction(e):
            return e['importance']
        self.criterea_list.sort(key=sortingFunction, reverse=True)


    def query_players(self): #Filters the players based on the criterea passed by the user
        filterplayers = FilterPlayers()
        self.queryset = filterplayers.filter_players(self.criterea_list)


    def sort_players(self): #sorts the players based on importance passed by user, and selects top five
        playersorter = PlayerSorter(self.queryset, self.criterea_list)
        self.sorted_queryset = playersorter.sort_queryset()[:5]
        return self.sorted_queryset, self.criterea_list


