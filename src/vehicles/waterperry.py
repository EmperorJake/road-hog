import global_constants
from road_vehicle import RVConsist, EdiblesTanker

consist = RVConsist(id = 'waterperry',
              base_numeric_id = 470,
              title = 'Waterperry [Edibles Tanker Truck]',
              replacement_id = '-none',
              power = 200,
              semi_truck = True,
              vehicle_life = 40,
              intro_date = 1972)

consist.add_unit(EdiblesTanker(consist = consist,
                        weight = 7,
                        capacity = 20,
                        vehicle_length = 2,
                        semi_truck_shift_offset_jank = 2,
                        effects = ['EFFECT_SPRITE_DIESEL, -3, 1, 10'],
                        spriterow_num = 0))

consist.add_unit(EdiblesTanker(consist = consist,
                        weight = 7,
                        capacity = 20,
                        vehicle_length = 5,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
