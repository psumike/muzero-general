
import random
from games.othello import Othello
from games.tictactoe import TicTacToe
from games.connect4 import Connect4

game = Othello()
# game = TicTacToe()
# game = Connect4()

# random.seed(123)
max_steps = 64


for i in range(max_steps):
    game.render()
    print(f"Step {i}: Player {game.to_play()} turn")
    obs = game.get_observation()
    actions = game.legal_actions()
    # print(obs)
    print(f"Actions: {actions}")
    action = random.choice(actions)
    print(f"Playing: {action}")
    obs, reward, done = game.step(action)
    print(f"Reward: {reward}")
    print(f"Done: {done}")
    if done:
        break
    print("----------")
game.render()
