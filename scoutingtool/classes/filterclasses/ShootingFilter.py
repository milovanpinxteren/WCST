from django.db.models import Avg

from scoutingtool.models import Shooting


class ShootingFilter():
    def filter_players(self, criterium):
        avg = Shooting.objects.aggregate(Avg(criterium['field']))[criterium['field'] + '__avg']
        if criterium['value'] == '0': #no preference
            filtered_id_list = Shooting.objects.all()
        if criterium['value'] == '1': #low amount
            filter_dict = {criterium['field'] + '__lte': avg}
            filtered_id_list = Shooting.objects.filter(**filter_dict).values_list('player_id', flat=True)
        elif criterium['value'] == '2': #medium amount
            filter_dict = {criterium['field'] + '__lt': avg}
            ordering = '-' + criterium['field']
            filtered_id_list = Shooting.objects.filter(**filter_dict).order_by(ordering).values_list('player_id', flat=True)[:25]
            #Gets the 25 players closest to the average amount (arbitrary chosen number)
        elif criterium['value'] == '3': #high amount
            filter_dict = {criterium['field'] + '__gte': avg}
            filtered_id_list = Shooting.objects.filter(**filter_dict).values_list('player_id', flat=True)
        return filtered_id_list


