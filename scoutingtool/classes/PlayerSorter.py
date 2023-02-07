from scoutingtool.models import GeneralPlayerInfo, Shooting, Passing


class PlayerSorter():
    def __init__(self, queryset, criterea_list):
        self.prepare_sorter(queryset, criterea_list)


    def get_sorting_fields(self, criterea_list, importance_value):
        self.sorting_fields = []
        for criterium in criterea_list:
            if criterium['importance'] == importance_value:
                self.sorting_fields.append(criterium['field'])
        return self.sorting_fields

    def prepare_sorter(self, queryset, criterea_list): #makes sure the most important criterea are used for sorting
        importance_value = 5
        self.queryset = queryset
        self.get_sorting_fields(criterea_list, importance_value)

        while not self.sorting_fields:
            importance_value -= 1
            self.get_sorting_fields(criterea_list, importance_value)
        if self.sorting_fields:
            self.sort_queryset()


    def sort_queryset(self): #sorts the queryset on the most important criterea
        sorting_string = 'self.queryset.order_by('
        for sortingfield in self.sorting_fields:
            if Shooting._meta.get_field(sortingfield):
                orderby = "'shooting__" + sortingfield + "'"
                sorting_string += orderby + ','
            elif Passing._meta.get_field(sortingfield):
                print('ASDF')
            else: print('asdfasd')
            #TODO the same for passing etc
        sorting_string += ')'
        self.sorted_queryset = eval(sorting_string)
        return self.sorted_queryset
