import logging
from State import State
from Event import Event
from typing import Optional, Type
from StateMachine import StateMachine

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
            machine.change_state(StateB,'state a update')
        elif self.i > 6:
            machine.stop()
    
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
        machine.change_state(StateC,'state b update')
        return
        machine.logger.info('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        
    def exit(self, machine: 'StateMachine'):
        pass
    
    def __str__(self) -> str:
        return 'StateB'

class StateC(State):
    def enter(self, machine: 'StateMachine'):
        pass

    def update(self, machine: 'StateMachine'):
        machine.change_state(StateA,'state c update')
        machine.logger.info('update c')

        
    def exit(self, machine: 'StateMachine'):
        pass
    
    def __str__(self) -> str:
        return 'StateC'

    