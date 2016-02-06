import global_constants
import graphics_processor.utils as graphics_utils
from road_vehicle import RVConsist, DumpHauler

graphics_processors = graphics_utils.get_bulk_cargo_processors(template='powerstock_template.png',
                                              copy_block_top_offsets = [40],
                                              paste_top_offset = 40)

consist = RVConsist(id = 'powerstock',
              base_numeric_id = 340,
              title = 'Powerstock [Dump Truck]',
              replacement_id = '-none',
              power = 650,
              semi_truck = True,
              vehicle_life = 40,
              intro_date = 2001)

consist.add_unit(DumpHauler(consist = consist,
                        weight = 8,
                        capacity = 0,
                        vehicle_length = 2,
                        semi_truck_shift_offset_jank = 2,
                        effects = ['EFFECT_SPRITE_DIESEL, -2, 1, 10'],
                        always_use_same_spriterow = True,
                        spriterow_num = 0))

consist.add_unit(DumpHauler(consist = consist,
                        weight = 8,
                        capacity = 40,
                        vehicle_length = 6,
                        spriterow_adjust = {'multiplier': 0, 'offset': 1}))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0,
                       graphics_processor=graphics_processors[0])
