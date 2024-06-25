from abc import ABC, abstractmethod
from Event import Event
from typing import Optional, Type


class State(ABC):
    @abstractmethod
    def enter(self, machine: 'StateMachine'):
        pass

    @abstractmethod
    def update(self, machine: 'StateMachine'):
        pass

    @abstractmethod
    def exit(self, machine: 'StateMachine'):
        pass


    def on_event(self, event: Event, machine: 'StateMachine'):
            pass

    @abstractmethod
    def __str__(self):
        pass


class StateMachine(ABC):
    @abstractmethod
    def change_state(self, state_class: Type[State]):
        pass
