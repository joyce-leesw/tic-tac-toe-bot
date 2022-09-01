from agent import Agent
from tictactoe import Tictactoe

# return winner at the terminal
def play(agent):
    game = Tictactoe()
    key = game.get_player()
    while True:
        action = agent.qlearner.get_best_move(game.cur_state())
        winner = game.play(*action)
        if winner:
            print("You lost :(")
            break
        if game.get_end():
            print("It's a tie!")
            break

        # ensure player does not try to overwrite a taken position
        flag = 1
        while flag == 1:
            row, column = map(int, input("input x and y: ").split())
            if game.board[row][column] != 0:
                print("You can't go there. Go again.")
            else:
                flag = 0

        winner = game.play(row, column)
        if winner:
            print("You won!")
            break
        if game.get_end():
            print("It's a tie!")
            break
    return None

agentTTT = Agent()
print("Agent is learning")
agentTTT.learn()
print("Done learning")

while True:
    print("Let's play a game of Tic Tac Toe.\n")
    play(agentTTT)
