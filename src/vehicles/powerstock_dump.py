from road_vehicle import DumpTruckConsist, DieselVehicleUnit

consist = DumpTruckConsist(id='powerstock_dump',
                    base_numeric_id=340,
                    name='Powerstock',
                    semi_truck_so_redistribute_capacity=True,
                    vehicle_life=40,
                    gen=5,
                    intro_date_offset=4)  # introduce later than gen epoch by design

consist.add_unit(type=DieselVehicleUnit,
                 vehicle_length=2,
                 semi_truck_shift_offset_jank=2,
                 effects=['EFFECT_SPRITE_DIESEL, -2, 1, 10',
                          'EFFECT_SPRITE_DIESEL, -2, -1, 10'],
                 always_use_same_spriterow=True)

consist.add_unit(vehicle_length=7)
