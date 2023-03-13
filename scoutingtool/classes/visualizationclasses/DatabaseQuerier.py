from scoutingtool.models import GeneralPlayerInfo, Shooting, Passing, Defense, Possession, DuelsandOffside

class DatabaseQuerier:
    def get_values_from_criterea(self, player, important_criterea):
        model_fields_dict = self.get_models_fields()
        for criterium in important_criterea:
            criterium_name = criterium['field']
            target_model = [k for k, v in model_fields_dict.items() if criterium_name in v] #str of the model where the data needs to come from
            #target_model, player and criterium_name and return the value of that criterium
            # {'criterium1_name': value from database, 'criterium2_name': value from database,}
            # return dict
        print(model_fields_dict)


    def get_models_fields(self):
        model_array = ['Shooting', 'Passing', 'Defense', 'Possession', 'DuelsandOffside', 'GeneralPlayerInfo']
        fields_dict = {}
        for model_name in model_array:
            fields_list = self.get_fields(model_name)
            fields_dict[model_name] = fields_list
        return fields_dict

    def get_fields(self, model_name):
        return [f.name for f in eval(model_name)._meta.fields]
