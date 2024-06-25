import logging

from typing import Optional, Type
from time import sleep
from Event import Event
from State import State

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class StateMachine:
    def __init__(self):
        self.states = {}
        self.state: Optional[State] = None
        self.next_state: Optional[State] = None
        self.finish = False
        self.logger = logger

    def register_state(self, state_class: Type[State]):
        state_instance = state_class()
        self.states[state_class] = state_instance
        self.logger.info(f"Registered state: {state_instance}")

    def change_state(self, new_state_class: Type[State]):
        new_state_instance = self.states.get(new_state_class)
        if not new_state_instance:
            self.logger.error(f"Cannot find instance for state class: {new_state_class}")
            return
        
        try:
            if self.state is not None:
                self.logger.info(f"Exiting state: {self.state}")
                self.state.exit(self)
            
            self.state = new_state_instance
            self.logger.info(f"Entering state: {self.state}")
            self.state.enter(self)
        except Exception as e:
            self.logger.error(f"Error while changing state: {e}")
            # Handle or log the exception as necessary
                
    def set_next_state(self, new_state_class: Optional[Type[State]]):
        if new_state_class:
            next_state_instance = self.states.get(new_state_class)
            self.logger.debug(f"Next state set: {next_state_instance}")
            self.next_state = next_state_instance
        else:
            self.logger.debug("Next state set to None")
            self.next_state = None

    def update(self):
        if self.state is not None:
            self.state.update(self)
            if self.next_state is not None:
                self.change_state(type(self.next_state))
                self.next_state = None
            sleep(0.3)

    def on_event(self, event: Event):
        if self.state is not None:
            self.state.on_event(event, self)
            self.logger.debug(f"Event '{event.name}' processed in state: {type(self.state)}")

