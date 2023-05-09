from django.db.models import Avg

from scoutingtool.models import DuelsandOffside


class DuelsandOffsideFilter():
    def filter_players(self, criterium):
        avg = DuelsandOffside.objects.aggregate(Avg(criterium['field']))[criterium['field'] + '__avg']
        if criterium['value'] == '0': #no preference
            filtered_id_list = DuelsandOffside.objects.all()
        if criterium['value'] == '1': #low amount
            filter_dict = {criterium['field'] + '__lte': avg}
            filtered_id_list = DuelsandOffside.objects.filter(**filter_dict).values_list('player_id', flat=True)
        elif criterium['value'] == '2': #medium amount (Gets the 25 players closest to the average amount (arbitrary chosen number))
            filter_dict = {criterium['field'] + '__lt': avg}
            ordering = '-' + criterium['field']
            filtered_id_list = DuelsandOffside.objects.filter(**filter_dict).order_by(ordering).values_list('player_id', flat=True)[:25]
        elif criterium['value'] == '3': #high amount
            filter_dict = {criterium['field'] + '__gte': avg}
            filtered_id_list = DuelsandOffside.objects.filter(**filter_dict).values_list('player_id', flat=True)
        return filtered_id_list


