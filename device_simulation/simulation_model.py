from threading import Thread, Event, Lock
from time import sleep

class SimulationModel:
    def __init__(self, interval: float = 0.2):
        self.interval: float = interval

        self.__simulation_thread = Thread(target = self.__simulation)
        self.__stop_event = Event()

    def __simulation(self):
       while True:
            if self.__stop_event.is_set():
                break
            self._tick()
            sleep(self.interval)

    def _tick(self):
        pass

    def start(self):
        if self.__simulation_thread.is_alive():
            return
        self.__stop_event.clear()
        self.__simulation_thread.start()

    def stop(self):
        self.__stop_event.set()