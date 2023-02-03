from scoutingtool.models import GeneralPlayerInfo


class PlayerSelector():
    def __init__(self, criterea_selection_form):
        print('player selector')
        self.get_values(criterea_selection_form)
        self.query_players()
        self.get_player_data()


    def get_values(self, criterea_selection_form):
        self.player_age_max = criterea_selection_form['player_age_max'].value()

    def query_players(self):
        queryset = GeneralPlayerInfo.objects.all()
        queryset = queryset.filter(player_age__lte=self.player_age_max)

        self.queryset = queryset

    def get_player_data(self):
        playersdata = []
        for player in self.queryset:
            playerdata = []
            playerdata.append(player.player_name)
            playerdata.append(player.player_age)
            playersdata.append(playerdata)

        return playersdata
