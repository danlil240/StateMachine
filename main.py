

from StateMachine import StateMachine
from States import StateA, StateB, StateC

def main():
    sm = StateMachine()
    sm.logger.setLevel('INFO')

    sm.register_state(StateA)
    sm.register_state(StateB)
    sm.register_state(StateC)

    sm.change_state(StateA)
    
    while not sm.finish:
        sm.update()
        
        
if __name__ == "__main__":
    main()