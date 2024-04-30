from simulation_model import SimulationModel
from heater import Heater, State

C_AIR = 1005.4

class Room(SimulationModel):
    def __init__(self, temperature, outside_temperature):
        self.thermal_resistance: float = 2e-3
        self.air_mass = 1000

        self.temperature: float = temperature
        self.outside_temperature: float = outside_temperature
        self.heater: Heater = Heater(self, State.off, fuel_amount = 5)
        super().__init__()

    def _tick(self):
        dQgain = 0
        if self.heater.state == State.on:
            dQgain = self.heater.air_flow_rate * C_AIR * (self.heater.temperature - self.temperature)
        dQloss = (self.temperature - self.outside_temperature) / self.thermal_resistance
        self.temperature += self.interval * (dQgain - dQloss) / (self.air_mass * C_AIR)

    def start(self):
        self.heater.turn_on()
        self.heater.start()
        super().start()

    def stop(self):
        self.heater.turn_off()
        self.heater.stop()
        super().stop()