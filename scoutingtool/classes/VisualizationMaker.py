
class VisualizationMaker():

    def make_visualizations(self, selected_players, criterea_list):
        print(criterea_list)
        playersdata = []
        for player in selected_players:
            # playerdata = []
            # playerdata.append(player.player_name)
            # playerdata.append(player.player_age)
            # playersdata.append(playerdata)
            playersdata.append(player.player_name)
        return playersdata