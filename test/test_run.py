import unittest
from unittest.mock import patch, MagicMock
from StateMachine import StateMachine  # Assuming your StateMachine class is in StateMachine.py
from State import State  # Assuming State and StateA are defined in State.py
from States import StateA, StateB, StateC  # Assuming State and StateA are defined in State.py
from Event import Event  # Assuming Event is defined in Event.py

class TestStateMachine(unittest.TestCase):

    def setUp(self):
        self.state_machine = StateMachine()
        self.state_machine.register_state(StateA)
        self.state_machine.register_state(StateB)
        self.state_machine.register_state(StateC)

    def test_run_method(self):
        state_A = StateA()
        state_B = StateB()
        state_C = StateC()

        state_A.enter = MagicMock()
        state_A.update = MagicMock()
        state_B.enter = MagicMock()
        state_B.update = MagicMock()
        state_C.enter = MagicMock()
        state_C.update = MagicMock()

        # Mocking an event triggering a state change
        state_A.on_event = MagicMock(side_effect=lambda event, machine: self.state_machine.change_state(StateB, "event"))

        with unittest.mock.patch.object(StateMachine, 'update', side_effect=self.state_machine.update) as mock_update:
            self.state_machine.run(StateA)

            state_A.enter.assert_called_once()
            self.assertTrue(mock_update.call_count > 0)

            # Simulate another event
            state_B.on_event = MagicMock(side_effect=lambda event, machine: self.state_machine.change_state(StateC, "another_event"))
            state_B.on_event(Event("SomeEvent"))

            self.assertEqual(self.state_machine.state, StateC)
            state_C.enter.assert_called_once()

    def tearDown(self):
        self.state_machine.stop()
        self.state_machine = None

if __name__ == '__main__':
    unittest.main()