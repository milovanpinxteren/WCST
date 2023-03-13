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
    # uncomment this after testing ↓
    if request.method == 'POST':
        criterea_selection_form = CritereaSelectorForm(request.POST)
        if criterea_selection_form.is_valid():

            playerselector = PlayerSelector(criterea_selection_form)
            selected_players, criterea_list = playerselector.sort_players()
            visualizationmaker = VisualizationMaker()
            playerdata = visualizationmaker.make_visualizations(selected_players, criterea_list)
            jsondata = str(playerdata).replace("'", '"')
            # uncomment this after testing ↑

    # playerdata = {'1': {'id': '1', 'general_player_info': {'Naam': 'Jerome Ngom Mbekeli', 'Geboortedatum': '30 sep. 1998 ', 'Geboorteplaats': 'Yaoundé\xa0\xa0 ', 'Leeftijd': '24', 'Lengte': '1,75\xa0m', 'Nationaliteit': 'Kameroen', 'Positie': 'Aanval - Linksbuiten', 'Voet': 'tweevoetig', 'Contract tot en met': '30 jun. 2024'}, 'transfer_value_info': {'2019-10-03': '125000', '2022-11-14': '300000'}}, '2': {'id': '2', 'general_player_info': {'Naam': 'AgustÃ\xadn Canobbio', 'Geboortedatum': 'Geen info bekend'}, 'transfer_value_info': {'2019-10-03': '125000', '2022-11-14': '300000'}}, '3': {'id': '3', 'general_player_info': {'Naam': 'Alan Franco', 'Geboortedatum': '11 okt. 1996 ', 'Geboorteplaats': 'Avellaneda\xa0\xa0 ', 'Leeftijd': '26', 'Lengte': '1,83\xa0m', 'Nationaliteit': 'Argentinië', 'Positie': 'Verdediging - Centrale verdediger', 'Voet': 'rechts', 'Contract tot en met': '31 dec. 2025'}, 'transfer_value_info': {'2017-10-09': '1500000', '2018-05-08': '6000000', '2018-12-18': '7500000', '2019-08-06': '5000000', '2019-12-05': '5000000', '2020-04-08': '4000000', '2021-02-08': '4000000', '2021-04-16': '3000000', '2021-07-09': '3000000', '2021-11-09': '3000000', '2022-08-18': '3000000', '2022-11-08': '2500000'}}, '4': {'id': '4', 'general_player_info': {'Naam': 'Declan Rice', 'Geboortedatum': '14 jan. 1999 ', 'Geboorteplaats': 'London\xa0\xa0 ', 'Leeftijd': '24', 'Lengte': '1,88\xa0m', 'Nationaliteit': 'Engeland\xa0\xa0Ierland', 'Positie': 'Middenveld - Defensief middenveld', 'Voet': 'rechts', 'Contract tot en met': '30 jun. 2024'}, 'transfer_value_info': {'2017-10-23': '500000', '2018-01-02': '2000000', '2018-05-28': '10000000', '2018-10-17': '15000000', '2018-12-19': '20000000', '2019-03-05': '35000000', '2019-06-13': '45000000', '2019-09-12': '50000000', '2019-12-10': '55000000', '2020-04-08': '49500000', '2020-10-13': '55000000', '2021-03-18': '60000000', '2021-05-28': '65000000', '2021-07-15': '70000000', '2021-12-23': '75000000', '2022-06-15': '80000000', '2022-11-03': '80000000'}}, '5': {'id': '5', 'general_player_info': {'Naam': 'Mohamed Ali Ben Romdhane', 'Geboortedatum': '6 sep. 1999 ', 'Geboorteplaats': 'Tunis\xa0\xa0 ', 'Leeftijd': '23', 'Lengte': '1,85\xa0m', 'Nationaliteit': 'Tunesië', 'Positie': 'Middenveld - Centraal middenveld', 'Voet': 'rechts', 'Contract tot en met': '30 jun. 2023'}, 'transfer_value_info': {'2019-01-17': '150000', '2019-06-28': '175000', '2020-01-05': '450000', '2020-04-08': '400000', '2021-02-24': '700000', '2021-06-19': '2500000', '2021-12-18': '2500000', '2022-06-25': '2700000', '2022-11-14': '2700000', '2022-12-29': '2700000'}}}
    # jsondata = '{"1": {"id": "1", "general_player_info": {"Naam": "Jerome Ngom Mbekeli", "Geboortedatum": "30 sep. 1998 ", "Geboorteplaats": "Yaoundé\xa0\xa0 ", "Leeftijd": "24", "Lengte": "1,75\xa0m", "Nationaliteit": "Kameroen", "Positie": "Aanval - Linksbuiten", "Voet": "tweevoetig", "Contract tot en met": "30 jun. 2024"}, "transfer_value_info": {"2019-10-03": "125000", "2022-11-14": "300000"}}, "2": {"id": "2", "general_player_info": {"Naam": "AgustÃ\xadn Canobbio", "Geboortedatum": "Geen info bekend"}, "transfer_value_info": {"2019-10-03": "125000", "2022-11-14": "300000"}}, "3": {"id": "3", "general_player_info": {"Naam": "Alan Franco", "Geboortedatum": "11 okt. 1996 ", "Geboorteplaats": "Avellaneda\xa0\xa0 ", "Leeftijd": "26", "Lengte": "1,83\xa0m", "Nationaliteit": "Argentinië", "Positie": "Verdediging - Centrale verdediger", "Voet": "rechts", "Contract tot en met": "31 dec. 2025"}, "transfer_value_info": {"2017-10-09": "1500000", "2018-05-08": "6000000", "2018-12-18": "7500000", "2019-08-06": "5000000", "2019-12-05": "5000000", "2020-04-08": "4000000", "2021-02-08": "4000000", "2021-04-16": "3000000", "2021-07-09": "3000000", "2021-11-09": "3000000", "2022-08-18": "3000000", "2022-11-08": "2500000"}}, "4": {"id": "4", "general_player_info": {"Naam": "Declan Rice", "Geboortedatum": "14 jan. 1999 ", "Geboorteplaats": "London\xa0\xa0 ", "Leeftijd": "24", "Lengte": "1,88\xa0m", "Nationaliteit": "Engeland\xa0\xa0Ierland", "Positie": "Middenveld - Defensief middenveld", "Voet": "rechts", "Contract tot en met": "30 jun. 2024"}, "transfer_value_info": {"2017-10-23": "500000", "2018-01-02": "2000000", "2018-05-28": "10000000", "2018-10-17": "15000000", "2018-12-19": "20000000", "2019-03-05": "35000000", "2019-06-13": "45000000", "2019-09-12": "50000000", "2019-12-10": "55000000", "2020-04-08": "49500000", "2020-10-13": "55000000", "2021-03-18": "60000000", "2021-05-28": "65000000", "2021-07-15": "70000000", "2021-12-23": "75000000", "2022-06-15": "80000000", "2022-11-03": "80000000"}}, "5": {"id": "5", "general_player_info": {"Naam": "Mohamed Ali Ben Romdhane", "Geboortedatum": "6 sep. 1999 ", "Geboorteplaats": "Tunis\xa0\xa0 ", "Leeftijd": "23", "Lengte": "1,85\xa0m", "Nationaliteit": "Tunesië", "Positie": "Middenveld - Centraal middenveld", "Voet": "rechts", "Contract tot en met": "30 jun. 2023"}, "transfer_value_info": {"2019-01-17": "150000", "2019-06-28": "175000", "2020-01-05": "450000", "2020-04-08": "400000", "2021-02-24": "700000", "2021-06-19": "2500000", "2021-12-18": "2500000", "2022-06-25": "2700000", "2022-11-14": "2700000", "2022-12-29": "2700000"}}}'
    # #playerdata and jsondata contain the same info.
    # However, the django template language needs a dict, whereas JS needs JSON as a string. Decided to just pass both
    context = {'playerdata': playerdata, 'jsondata': jsondata}


    return render(request, 'resultspage.html', context)