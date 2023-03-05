from scoutingtool.classes.visualizationclasses.InfoGetter import InfoGetter


class VisualizationMaker():

    def make_visualizations(self, selected_players, criterea_list):
        print(criterea_list)
        playersdata = {}
        infogetter = InfoGetter()
        for player in selected_players:
            infogetter.get_transfermarkt_data(player)


            # playersdata.append(player.player_name) #TODO nog aanpassen, is dict
        return playersdata
