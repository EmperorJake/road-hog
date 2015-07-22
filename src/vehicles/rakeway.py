import global_constants
from road_vehicle import EngineConsist, BoxHauler

consist = EngineConsist(id = 'rakeway',
              base_numeric_id = 870,
              title = 'Rakeway [Box Tram]',
              roadveh_flag_tram = True,
              replacement_id = '-none',
              power = 200,
              vehicle_life = 40,
              intro_date = 1900)

consist.add_unit(BoxHauler(consist = consist,
                        weight = 12,
                        capacity = 0,
                        vehicle_length = 3,
                        effect_spawn_model = 'EFFECT_SPAWN_MODEL_STEAM',
                        effects = ['EFFECT_SPRITE_STEAM, -2, 0, 14'],
                        spriterow_num = 0))

consist.add_unit(BoxHauler(consist = consist,
                        weight = 4,
                        capacity = 16,
                        vehicle_length = 4,
                        spriterow_num = 1), repeat=5)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
