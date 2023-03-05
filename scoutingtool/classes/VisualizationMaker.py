from scoutingtool.classes.visualizationclasses.InfoGetter import InfoGetter


class VisualizationMaker():

    def make_visualizations(self, selected_players, criterea_list):
        print(criterea_list)
        full_players_data_dict = {}
        infogetter = InfoGetter()
        player_counter = 1
        for player in selected_players:
            player_data_dict = {}
            player_data_dict['id'] = player_counter
            general_player_info = infogetter.get_transfermarkt_data(player)
            player_data_dict['general_player_info'] = general_player_info
            full_players_data_dict[player_counter] = player_data_dict
            player_counter += 1
            print('FULL PLAYER DATA DICT')
            print(full_players_data_dict)
        return full_players_data_dict
