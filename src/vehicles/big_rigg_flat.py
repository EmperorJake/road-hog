from road_vehicle import FlatbedTruckConsist, DieselVehicleUnit

consist = FlatbedTruckConsist(id='big_rigg_flat',
                       base_numeric_id=660,
                       name='Big Rigg',
                       vehicle_life=40,
                       gen=5)

consist.add_unit(type=DieselVehicleUnit,
                 vehicle_length=5,
                 cargo_length=3)

consist.add_unit(vehicle_length=4,
                 cargo_length=4)
