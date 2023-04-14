import time

class Log:

    def __init__(self) -> None:
        self._START_TIME = 0
        self._END_TIME = 0
        self._TEMPO_MEDIO = 0

    def start_time(self) -> None:
        self._START_TIME = time.time()
    
    def end_time(self) -> None:
        self._END_TIME = time.time()


    def time_result(self) -> str:
        self._TEMPO_MEDIO = (self._END_TIME - self._START_TIME)
        return f"{self._TEMPO_MEDIO:.2f}s"