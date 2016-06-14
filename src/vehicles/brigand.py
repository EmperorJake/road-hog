import global_constants
from road_vehicle import RVConsist, SuppliesHauler
# equiv. Scammell Highwayman or Explorer with dolly low loader trailer - not huge

consist = RVConsist(vehicle_type = SuppliesHauler,
                id = 'brigand',
                base_numeric_id = 540,
                title = 'Brigand [Supplies Truck]',
                replacement_id = '-none',
                power = 360,
                vehicle_life = 40,
                intro_date = 1953)

consist.add_unit(weight = 20,
                capacity = 0,
                vehicle_length = 6,
                visual_effect = 'VISUAL_EFFECT_DIESEL')

consist.add_unit(weight = 12,
                capacity = 45,
                vehicle_length = 7)

consist.add_unit(weight = 20,
                capacity = 0,
                vehicle_length = 6,
                visual_effect = 'VISUAL_EFFECT_DIESEL',
                spriterow_num_base = 0)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
