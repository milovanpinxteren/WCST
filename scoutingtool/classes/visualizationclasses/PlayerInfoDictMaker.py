
class PlayerInfoDictMaker:
    def make_dict(self, tag, resultset_counter, player_info_resultset, player_info_dict):
        if tag.text == 'Geboortedatum:':
            player_info_dict['Geboortedatum'] = player_info_resultset[resultset_counter + 1].text
        if tag.text == 'Geboorteplaats:':
            player_info_dict['Geboorteplaats'] = player_info_resultset[resultset_counter + 1].text.strip('\n')
        if tag.text == 'Leeftijd:':
            player_info_dict['Leeftijd'] = player_info_resultset[resultset_counter + 1].text
        if tag.text == 'Lengte:':
            player_info_dict['Lengte'] = player_info_resultset[resultset_counter + 1].text
        if tag.text == 'Nationaliteit:':
            player_info_dict['Nationaliteit'] = player_info_resultset[resultset_counter + 1].text.strip()
        if tag.text == 'Positie:':
            player_info_dict['Positie'] = player_info_resultset[resultset_counter + 1].text.strip()
        if tag.text == 'Voet:':
            player_info_dict['Voet'] = player_info_resultset[resultset_counter + 1].text.strip()
        if tag.text == 'Actuele club:':
            player_info_dict['Actuele club'] = player_info_resultset[resultset_counter + 1].text
        if tag.text == 'Contract tot en met:':
            player_info_dict['Contract tot en met'] = player_info_resultset[resultset_counter + 1].text.strip()
        if tag.text == 'Positie:':
            player_info_dict['Positie'] = player_info_resultset[resultset_counter + 1].text.strip()