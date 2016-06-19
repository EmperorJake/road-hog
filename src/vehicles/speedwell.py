import global_constants
from road_vehicle import RVConsist, BoxHauler

consist = RVConsist(vehicle_type = BoxHauler,
                id = 'speedwell',
                base_numeric_id = 400,
                title = 'Speedwell [Box Truck]',
                replacement_id = '-none',
                semi_truck_so_redistribute_capacity = True,
                vehicle_life = 40,
                intro_date = 1997)

consist.add_unit(weight = 7,
                capacity = 0,
                vehicle_length = 2,
                semi_truck_shift_offset_jank = 2,
                effects = ['EFFECT_SPRITE_DIESEL, -2, 1, 10'])

consist.add_unit(weight = 8,
                capacity = 40,
                vehicle_length = 7)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
