import numpy as np

import random
class Q:
    def __init__(self, alpha=0.001, discount=0.9):
        self.alpha = alpha
        self.discount = discount
        # initialise q table with 0
        # board state and its reward were stored as a key and value pair in a dictionary
        # a dict subclass that calls a factory function to supply missing values
        self.values = {}

    # initialise q table, choose action, perform action, measure reward, update q
    def update(self, state, action, next_state, reward):
        value =  self.values.get(state, [[0,0,0] for _ in range(3)])
        next_q_values = self.values.get(next_state, [[0,0,0] for _ in range(3)])
        max_next_q_value = np.max(next_q_values)
        value[action[0]][action[1]] += self.alpha * (reward + self.discount * max_next_q_value - value[action[0]][action[1]])
        self.values[state] = value

    def get_best_move(self, state, board):
        q_values = self.values.get(state, [[0,0,0] for _ in range(3)])
        empty_cells = np.array([[i, j] for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 0])
        empty_q_values = [q_values[cell[0]][cell[1]] for cell in empty_cells]
        max_q_value = max(empty_q_values)
        max_q_indices = [i for i in range(len(empty_cells)) if empty_q_values[i] == max_q_value]
        max_q_index = random.choice(max_q_indices)
        action = empty_cells[max_q_index]

        return action