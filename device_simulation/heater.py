from enum import Enum
from simulation_model import SimulationModel

class Room:
    temperature: float = 0

class State(Enum):
    on = 0
    off = 1

class Heater(SimulationModel):
    def __init__(self,
                 environment: Room,
                 state: State = State.off,
                 fuel_amount: float = 5,
                 preset_temperature: float = 50):
        self.max_fuel_amount: float = 5 #liters
        self.fuel_consumption: float = 2.78e-4 #liters per second
        self.air_flow_rate: float = 1 #kg per second
        self.battery_charge = 100

        self.environment: Room = environment
        self.state: State = state
        self.temperature: float = environment.temperature
        self.preset_temperature: float = preset_temperature

        self.fuel_amount = fuel_amount
        super().__init__()

    @property
    def fuel_amount(self) -> float:
        return self._fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, value: float):
        if value >= 0 and value <= self.max_fuel_amount:
            self._fuel_amount = value

    def _tick(self):
        self.battery_charge -= 1e-5 * self.interval
        if self.fuel_amount <= 0:
            self.turn_off
        if self.is_on():
            self.fuel_amount -= self.interval * self.fuel_consumption
            self.temperature = self.preset_temperature
        else:
            self.temperature = self.environment.temperature

    def turn_on(self):
        self.state = State.on

    def turn_off(self):
        self.state = State.off

    def is_on(self) -> bool:
        if self.state == State.on:
            return True
        else:
            return False