from abc import ABC, abstractmethod
from Event import Event
from typing import Optional, Type
import StateMachine as SM


class State(ABC):
    @abstractmethod
    def enter(self, machine: 'SM'):
        pass

    @abstractmethod
    def update(self, machine: 'SM'):
        pass

    @abstractmethod
    def exit(self, machine: 'SM'):
        pass


    def on_event(self, event: Event, machine: 'SM'):
            pass

    @abstractmethod
    def __str__(self):
        pass
