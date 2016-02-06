import global_constants
from road_vehicle import RVConsist, BulkPowderHauler

consist = RVConsist(id = 'limebreach',
              base_numeric_id = 260,
              title = 'Limebreach [Covered Hopper Truck]',
              replacement_id = '-none',
              power = 250,
              semi_truck = True,
              vehicle_life = 40,
              intro_date = 1949)

consist.add_unit(BulkPowderHauler(consist = consist,
                        weight = 6,
                        capacity = 0,
                        vehicle_length = 2,
                        semi_truck_shift_offset_jank = 2,
                        effects = ['EFFECT_SPRITE_DIESEL, -2, 1, 10'],
                        spriterow_num = 0))

consist.add_unit(BulkPowderHauler(consist = consist,
                        weight = 8,
                        capacity = 30,
                        vehicle_length = 5,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
