from scoutingtool.models import GeneralPlayerInfo


class PlayerSelector():
    def __init__(self, criterea_selection_form):
        self.handle_form(criterea_selection_form)
        self.query_players()
        self.get_player_data()


    def handle_form(self, criterea_selection_form):
        self.criterea_list = []
        for field in criterea_selection_form.fields:
            if not "_importance" in field:
                value = criterea_selection_form[field].value()
                try:
                    importance = int(criterea_selection_form[field + '_importance'].value())
                except KeyError: #for position, no importance passed by user, high importance by default
                    importance = 5
                criterium_dict = {'field': field, 'value': value, 'importance': importance}
                self.criterea_list.append(criterium_dict)
        def sortingFunction(e):
            return e['importance']
        self.criterea_list.sort(key=sortingFunction, reverse=True)


    def query_players(self):
        queryset = GeneralPlayerInfo.objects.all()
        # queryset = queryset.filter(player_age__lte=self.player_age_max)


        self.queryset = queryset

    def get_player_data(self):
        playersdata = []
        for player in self.queryset:
            playerdata = []
            playerdata.append(player.player_name)
            playerdata.append(player.player_age)
            playersdata.append(playerdata)

        return playersdata
