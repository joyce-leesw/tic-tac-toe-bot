import random

from q import Q
from tictactoe import Tictactoe

class Agent:
    def __init__(self):
        # probability of choosing a random function, decreases over time
        # epsilon greddy algorithm
        self.epsilon = 1.0
        self.qlearner = Q()

    def get_moves(self, state, valid_moves):
        best = self.qlearner.get_best_move(state)
        # choose a random move to begin
        # If this number is smaller than a predetermined epsilon value the algorithm will play a random move 
        # however if the generated number was larger than epsilon the algorithm will take the q-learning approach
        if best is None or random.random() < self.epsilon:
            best = random.choice(valid_moves)
        return best 

    def learn(self, n=50000):
        counter_win = 0
        counter_lose = 0
        for _ in range(n):
            game = Tictactoe(render=False)
            while True:
                state = game.cur_state()
                action = self.get_moves(state, game.get_valid_moves())
                winner = game.play(*action)
                # perform chosen action, transition to next state
                # receive rewards for action and update q table
                if winner or game.get_end():
                    self.qlearner.update(state, action, game.cur_state(), 100)
                    counter_win += 1
                    break

                winner = game.play(*random.choice(game.get_valid_moves()))
                if winner or game.get_end():
                    self.qlearner.update(state, action, game.cur_state(), -100)
                    counter_lose += 1
                    break
                self.qlearner.update(state, action, game.cur_state(), 0)
            self.epsilon -= 0.0001
        print("Win rate:", counter_win)
        print("Lose rate:", counter_lose)
    