import numpy as np

class Agent:
    def __init__(self, strategy, model):
        self.strategy = strategy
        self.model = model

    def get_current_epsilon(self):
        return self.strategy.get_exploration_rate(self.current_step)
    
    def get_action(self, state, valid_actions):
        qs = self.model.get_current_qs(state)[0]
        qs = list(enumerate(qs))  # Assuming 0 based action space
        # Pass only valid actions, with their q values (a, q)
        valid_qs = np.array([a_q for a_q in qs if a_q[0] in valid_actions])
        action = self.strategy.select_action(valid_qs)
        return action