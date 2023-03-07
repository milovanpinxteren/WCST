from scoutingtool.classes.visualizationclasses.InfoGetter import InfoGetter


class VisualizationMaker():
    def make_visualizations(self, selected_players, criterea_list):
        print(criterea_list)
        full_players_data_dict = {}
        infogetter = InfoGetter()
        player_counter = 1
        for player in selected_players:
            player_data_dict = {}
            player_data_dict['id'] = str(player_counter)
            try:
                general_player_info = infogetter.get_transfermarkt_data(player)[0]
                transfer_value_info = infogetter.get_transfermarkt_data(player)[1]
            except KeyError: #no information found
                general_player_info = infogetter.get_transfermarkt_data(player)
            player_data_dict['general_player_info'] = general_player_info
            player_data_dict['transfer_value_info'] = transfer_value_info
            full_players_data_dict[str(player_counter)] = player_data_dict
            player_counter += 1
            print('FULL PLAYER DATA DICT')
            print(full_players_data_dict)
        return full_players_data_dict
        # self.prepare_dict(full_players_data_dict)


    def prepare_dict(self, full_players_data_dict):
        return full_players_data_dict

