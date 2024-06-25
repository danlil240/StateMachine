import logging

from abc import ABC, abstractmethod
from State import State
from Event import Event
from typing import Optional, Type

class StateA(State):
    def __init__(self):
        self.i = 0

    def enter(self, machine: 'StateMachine'):
        pass

    def on_event(self, event: Event, machine: 'StateMachine'):
        if event == Event.TO_STATE_B:
            machine.change_state(StateB)
        elif event == Event.TO_STATE_C:
            machine.change_state(StateC)

    def update(self, machine: 'StateMachine'):
        self.i += 1
        machine.logger.info(f'State A  i: {self.i}')
        if self.i == 5:
            machine.set_next_state(StateB)
        elif self.i > 6:
            machine.finish = True
    
    def exit(self, machine: 'StateMachine'):
        pass
    
    def __str__(self) -> str:
        return 'StateA'
        


class StateB(State):
    def enter(self, machine: 'StateMachine'):
        pass

    def on_event(self, event: Event, machine: 'StateMachine'):
        if event == Event.TO_STATE_A:
            machine.set_next_state(StateA)
        elif event == Event.TO_STATE_D:
            machine.set_next_state(StateC)

    def update(self, machine: 'StateMachine'):
        machine.set_next_state(StateC)
        
    def exit(self, machine: 'StateMachine'):
        pass
    
    def __str__(self) -> str:
        return 'StateB'

class StateC(State):
    def enter(self, machine: 'StateMachine'):
        pass

    def update(self, machine: 'StateMachine'):
        machine.set_next_state(StateA)
        
    def exit(self, machine: 'StateMachine'):
        pass
    
    def __str__(self) -> str:
        return 'StateC'

    

    
class StateMachine(ABC):
    logger = logging.getLogger(__name__)
    @abstractmethod
    def change_state(self, state_class: Type[State]):
        pass

    @abstractmethod
    def set_next_state(self, state_class: Type[State]):
        pass

