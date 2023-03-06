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
            general_player_info = infogetter.get_transfermarkt_data(player)
            player_data_dict['general_player_info'] = general_player_info
            full_players_data_dict[str(player_counter)] = player_data_dict
            player_counter += 1
            print('FULL PLAYER DATA DICT')
            print(full_players_data_dict)
        return full_players_data_dict
        # self.prepare_dict(full_players_data_dict)


    def prepare_dict(self, full_players_data_dict):
        # '{"1": {"id": 1, "general_player_info": {"Naam": "Milo¡ Degenek", "Geboortedatum": "Geen info bekend"}}, "2": {"id": 2, "general_player_info": {"Naam": "ASDFA", "Geboortedatum": "GEEN IDEE"}}}'
        return full_players_data_dict

