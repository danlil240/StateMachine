# States.py
from State import State

class StateA(State):
    def enter(self, machine: 'StateMachine'):
        pass

    def on_event(self, event: 'Event', machine: 'StateMachine'):
        if event.name == "TO_STATE_B":
            machine.change_state(StateB, "Event TO_STATE_B triggered")

    def update(self, machine: 'StateMachine'):
        pass

    def exit(self, machine: 'StateMachine'):
        pass

    def __str__(self) -> str:
        return 'StateA'


class StateB(State):
    def enter(self, machine: 'StateMachine'):
        pass

    def on_event(self, event: 'Event', machine: 'StateMachine'):
        if event.name == "TO_STATE_C":
            machine.change_state(StateC, "Event TO_STATE_C triggered")

    def update(self, machine: 'StateMachine'):
        pass

    def exit(self, machine: 'StateMachine'):
        pass

    def __str__(self) -> str:
        return 'StateB'


class StateC(State):
    def enter(self, machine: 'StateMachine'):
        pass

    def on_event(self, event: 'Event', machine: 'StateMachine'):
        if event.name == "TO_STATE_A":
            machine.change_state(StateA, "Event TO_STATE_A triggered")

    def update(self, machine: 'StateMachine'):
        pass

    def exit(self, machine: 'StateMachine'):
        pass

    def __str__(self) -> str:
        return 'StateC'

# Event.py
class Event:
    def __init__(self, name: str):
        self.name = name
