from collections import defaultdict

class Q:
    def __init__(self, alpha=0.75, discount=0.9):
        self.alpha = alpha
        self.discount = discount
        # initialise q table with 0
        # board state and its reward were stored as a key and value pair in a dictionary
        # a dict subclass that calls a factory function to supply missing values
        self.values = defaultdict(lambda: defaultdict(lambda: 0.0))
        # self.values = [[0,0,0] for _ in range(3)]

    # initialise q table, choose action, perform action, measure reward, update q
    def update(self, state, action, next_state, reward):
        value = self.values[state][action]
        v = list(self.values[next_state].values())
        next_q = max(v) if v else 0
        value = value + self.alpha * (reward + self.discount * next_q - value)
        self.values[state][action] = value

    def get_best_move(self, state):
        keys = list(self.values[state].keys())
        if not keys:
            return None
        return max(keys, key=lambda x: self.values[state][x])