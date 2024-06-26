

from StateMachine import StateMachine
from States import StateA, StateB, StateC

def main():
    sm = StateMachine()
    sm.logger.setLevel('INFO')

    sm.register_state(StateA)
    sm.register_state(StateB)
    sm.register_state(StateC)    
    sm.run(StateA)
        
        
if __name__ == "__main__":
    main()