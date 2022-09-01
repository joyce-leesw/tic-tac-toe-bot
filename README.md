# Tic-Tac-Toe-Bot-using-Q-Learning

A project to design a Tic Tac Toe Bot to play with using Q Learning.  

Q Learning works by encouraging the machine to explore its environment to choose the best action through trial-and-error. It uses the **Bellman equation** whereby the machine estimates the Q value of an action given its state. Each state-action pair is stored as a key-value pair in a dictionary and assigned a reward, with higher Q value indicating a high desirability for the action. Its ability to consider action and reward of its state depicts a finite **Markov Decision Process**. In the beginning, the machine will select a random action and play horribly. However, through iterations, it updates itself and learns to optimise the rewards of its action, ultimately reaching a high winning probability using **epsilon greedy algorithms**. 

