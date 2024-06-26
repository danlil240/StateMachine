# test_state_machine.py

import unittest
from StateMachine import StateMachine
from States import StateA, StateB, StateC
from Event import Event

class TestStateMachine(unittest.TestCase):
    def setUp(self):
        self.sm = StateMachine()
        self.sm.register_state(StateA)
        self.sm.register_state(StateB)
        self.sm.register_state(StateC)

    def test_initial_state(self):
        self.sm.setFirstState(StateA)
        # self.sm.update()
        self.assertIsInstance(self.sm.state, StateA)

    def test_immediate_transition(self):
        self.sm.setFirstState(StateA)
        self.sm.update()
        self.sm.change_state(StateB, "immediate transition")
        self.sm.update()
        self.assertIsInstance(self.sm.state, StateB)

    def test_deferred_transition(self):
        self.sm.setFirstState(StateA)
        self.sm.update()
        self.sm.change_state(StateB, "deferred transition")
        self.assertIsInstance(self.sm.state, StateA)
        self.sm.update()  # Deferred transition should now happen
        self.assertIsInstance(self.sm.state, StateB)

    def test_event_handling(self):
        self.sm.setFirstState(StateA)
        self.sm.update()
        self.sm.on_event(Event.TO_STATE_B)
        self.sm.update()
        self.assertIsInstance(self.sm.state, StateB)

    def test_transition_history(self):
        self.sm.setFirstState(StateA)
        self.sm.update()
        self.sm.change_state(StateB, "move to B")
        self.sm.update()
        self.sm.change_state(StateC, "move to C")
        self.sm.update()
        self.assertIn("Setting first state: StateA", self.sm.transition_history)
        self.assertIn("From StateA to StateB due to move to B", self.sm.transition_history)
        self.assertIn("From StateB to StateC due to move to C", self.sm.transition_history)

if __name__ == "__main__":
    unittest.main()
