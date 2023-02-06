from django.db.models import Avg

from scoutingtool.models import Shooting


class ShootingFilter():
    def filter_players(self, criterium):
        if criterium['field'] == 'goals_per_90_mins':
            avg = Shooting.objects.aggregate(Avg(criterium['field']))[criterium['field'] + '__avg']
            filter_dict = {criterium['field'] + '__gte': avg}
            filtered_id_list = Shooting.objects.filter(**filter_dict).values_list('player_id', flat=True)
            # filtered_id_list = Shooting.objects.filter(goals_per_90_mins__gte=avg).values_list('player_id', flat=True)
        elif criterium['field'] == 'shots':
            avg_shooting = Shooting.objects.aggregate(Avg('shots_per_90_mins'))['shots_per_90_mins__avg']
            filtered_id_list = Shooting.objects.filter(shots_per_90_mins__gte=avg_shooting).values_list('player_id', flat=True)
        elif criterium['field'] == 'shots_on_target':
            avg_shooting = Shooting.objects.aggregate(Avg('shots_on_target_per_90_mins'))['shots_on_target_per_90_mins__avg']
            filtered_id_list = Shooting.objects.filter(shots_on_target_per_90_mins__gte=avg_shooting).values_list('player_id', flat=True)
        elif criterium['field'] == 'goals_per_shot':
            avg_shooting = Shooting.objects.aggregate(Avg('goals_per_shot'))['goals_per_shot__avg']
            filtered_id_list = Shooting.objects.filter(goals_per_shot__gte=avg_shooting).values_list('player_id', flat=True)
        elif criterium['field'] == 'penalty_killer':
            avg_shooting = Shooting.objects.aggregate(Avg('penalty_success_rate'))['penalty_success_rate__avg']
            filtered_id_list = Shooting.objects.filter(penalty_success_rate__gte=avg_shooting).values_list('player_id', flat=True)
        return filtered_id_list


