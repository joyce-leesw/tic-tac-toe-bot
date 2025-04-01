import random
import numpy as np

from q import Q
from tictactoe import Tictactoe

class Agent:
    def __init__(self):
        # probability of choosing a random function, decreases over time
        # epsilon greddy algorithm
        self.exploration_rate = 0.5
        self.qlearner = Q()

    def get_moves(self, state, board):
        # choose a random move to begin
        # If this number is smaller than a predetermined epsilon value the algorithm will play a random move 
        # however if the generated number was larger than epsilon the algorithm will take the q-learning approach
        if random.uniform(0, 1) < self.exploration_rate or state not in self.qlearner.values:
            empty_cells = np.array([[i, j] for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 0])
            best = random.choice(empty_cells)
        else:
            best = self.qlearner.get_best_move(state, board)
        return best 

    def learn(self, num_episodes=50000):
        counter_win = 0
        counter_draw = 0
        counter_loss = 0
        for _ in range(num_episodes):
            game = Tictactoe(render=False)
            while not game.get_end():
                state = game.cur_state()

                action = self.get_moves(state, game.board)
                winner = game.play(action[0], action[1])

                if game.get_end():
                    if winner == 1:
                        self.qlearner.update(state, action, game.cur_state(), -1)
                        counter_loss += 1
                    elif winner == -1:
                        self.qlearner.update(state, action, game.cur_state(), 1)
                        counter_win += 1
                    else:
                        self.qlearner.update(state, action, game.cur_state(), 0)
                        counter_draw += 1

            self.exploration_rate *= 0.99

        agent_win_percentage = (counter_win / num_episodes) * 100
        print("Win rate: {:.2f}%".format(agent_win_percentage), counter_win)
        print(counter_draw)
        print(counter_loss)
        print(num_episodes)
    
        