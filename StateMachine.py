import logging
from typing import Optional, Type, Dict, List
from time import sleep
from Event import Event
from State import State

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class StateMachine:
    def __init__(self):
        self.states: Dict[Type[State], State] = {}
        self.state: Optional[State] = None
        self.next_state: Optional[State] = None
        self.finish = False
        self.logger = logger
        self.transition_history: List[str] = []
        

    def register_state(self, state_class: Type[State]):
        if state_class in self.states:
            self.logger.warning(f"State {state_class} is already registered.")
            return
        state_instance = state_class()
        self.states[state_class] = state_instance
        self.logger.info(f"Registered state: {state_instance}")
        
        
    def setFirstState(self, first_state: Type[State]):
        if first_state in self.states:
            self._perform_state_change(self.states.get(first_state))
            self.transition_history.append(f"Setting first state: {self.states.get(first_state)}")
        else:
            self.logger.error(f"Cannot find state {first_state} in states")



    def change_state(self, new_state_class: Type[State], reason: str = ''):
        new_state_instance = self.states.get(new_state_class)
        if not new_state_instance:
            self.logger.error(f"Cannot find instance for state class: {new_state_class}")
            return

        self.logger.info(f"Changing state to {new_state_instance} due to {reason}")
        self.transition_history.append(f"From {self.state} to {new_state_instance} due to {reason}")
        self.next_state = new_state_instance

    def _perform_state_change(self, new_state_instance: State):
        try:
            if self.state is not None:
                self.logger.info(f"Exiting state: {self.state}")
                self.state.exit(self)

            self.state = new_state_instance
            self.logger.info(f"Entering state: {self.state}")
            self.state.enter(self)
        except Exception as e:
            self.logger.error(f"Error while changing state: {e}")

    def update(self):
        if self.state is not None:
            try:
                self.state.update(self)
            except Exception as e:
                self.logger.error(f"Error during update in state {self.state}: {e}")

        if self.next_state is not None:
            self._perform_state_change(self.next_state)
            self.next_state = None

        sleep(0.3)

    def on_event(self, event: Event):
        if self.state is not None:
            try:
                self.state.on_event(event, self)
                self.logger.debug(f"Event '{event.name}' processed in state: {self.state}")
            except Exception as e:
                self.logger.error(f"Error processing event '{event.name}' in state {self.state}: {e}")

    def stop(self):
        self.finish = True
        self.logger.info("State machine stopping gracefully.")

    def run(self,first_state: State):
        self.setFirstState(first_state)
        while not self.finish:
            self.update()

