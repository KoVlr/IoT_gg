from simulation_model import SimulationModel
from heater import Heater, State

C_AIR = 1005.4

saturated_steam_density_table = [
 (-30, 0.33),
 (-28, 0.41),
 (-26, 0.51),
 (-24, 0.60),
 (-22, 0.73),
 (-20, 0.88),
 (-18, 1.05),
 (-16, 1.27),
 (-14, 1.51),
 (-12, 1.80),
 (-10, 2.14),
 (-8, 2.54),
 (-6, 2.99),
 (-4, 3.51),
 (-2, 4.13),
 (0, 4.84),
 (2, 5.60),
 (4, 6.40),
 (6, 7.3),
 (8, 8.3),
 (10, 9.4),
 (12, 10.7),
 (14, 12.1),
 (16, 13.6),
 (18, 15.4),
 (20, 17.3),
 (22, 19.4),
 (24, 21.8),
 (26, 24.4),
 (28, 27.2),
 (30, 30.3),
 (32, 33.9),
 (34, 37.6),
 (36, 41.8),
 (38, 46.3),
 (40, 51.2),
 (50, 83.0),
 (60, 130),
 (70, 198),
 (80, 293),
 (90, 424),
 (100, 598)
]

def get_saturated_steam_density(temperature):
    for item in reversed(saturated_steam_density_table):
        if temperature >= item[0]:
            return item[1]
        
class Room(SimulationModel):
    def __init__(self, temperature, outside_temperature):
        self.thermal_resistance: float = 2e-3
        self.air_mass = 1000
        self.absolute_humidity = 8
        self.voltage = 230

        self.temperature: float = temperature
        self.compute_humidity
        self.outside_temperature: float = outside_temperature
        self.heater: Heater = Heater(self, State.off, fuel_amount = 5)
        super().__init__()

    def _tick(self):
        dQgain = 0
        if self.heater.state == State.on:
            dQgain = self.heater.air_flow_rate * C_AIR * (self.heater.temperature - self.temperature)
        dQloss = (self.temperature - self.outside_temperature) / self.thermal_resistance
        self.temperature += self.interval * (dQgain - dQloss) / (self.air_mass * C_AIR)
        self.compute_humidity()

    def compute_humidity(self):
        humidity = 100 * self.absolute_humidity / get_saturated_steam_density(self.temperature)
        self.humidity = humidity if humidity < 100 else 100

    def start(self):
        self.heater.turn_on()
        self.heater.start()
        super().start()

    def stop(self):
        self.heater.turn_off()
        self.heater.stop()
        super().stop()