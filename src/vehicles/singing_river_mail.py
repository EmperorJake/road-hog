from road_vehicle import MailTramConsist, ElectricRoadVehicle

consist = MailTramConsist(id='singing_river_mail',
                   base_numeric_id=850,
                   name='Singing River',
                   power=600,
                   vehicle_life=40,
                   gen=5)

consist.add_unit(type=ElectricRoadVehicle,
                 capacity=36,
                 vehicle_length=8,
                 effects=['EFFECT_SPRITE_ELECTRIC, 0, 0, 10'])
