from fastapi import FastAPI, HTTPException, status
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from agent import Agent
from tictactoe import Tictactoe

# Initialize FastAPI app
app = FastAPI()

# Initialize agent and game
agentTTT = Agent()
game = Tictactoe()

# Train the agent
print("Agent is learning")
agentTTT.learn()
print("Done learning")

# Define request and response models for the API
class MoveRequest(BaseModel):
    row: int
    column: int
class MoveResponse(BaseModel):
    ai_move: Optional[List[int]]
    game_over: bool
    winner: Optional[str]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_game_state(ai_move: Optional[List[int]] = None) -> MoveResponse:
    winner = game.is_winner()
    game_over = game.get_end() or winner is not None
    return MoveResponse(
        ai_move=ai_move,
        winner="AI" if winner == -1 else "Player" if winner == 1 else None,
        game_over=game_over
    )

@app.post("/reset", response_model=MoveResponse)
async def reset_game():
    global game
    game = Tictactoe()  # Reset the game
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.post("/play", response_model=MoveResponse)
async def play_game(move: MoveRequest):
    print(move.row, move.column)
    player_winner = game.play(move.row, move.column, 1)
    if player_winner:
        return MoveResponse(
            ai_move=None,
            game_over=True,
            winner="Player"
        )
    
    if game.get_end():
        return MoveResponse(
            ai_move=None,
            game_over=True,
            winner=None
        )
    
    ai_action = list(agentTTT.qlearner.get_best_move(game.cur_state(), game.board))
    print(ai_action[0], ai_action[1])
    if ai_action is None:
        raise HTTPException(status_code=500, detail="AI could not determine a valid move.")
    
    ai_winner = game.play(ai_action[0], ai_action[1], -1)
    if ai_winner:
        return MoveResponse(
            ai_move=ai_action,
            game_over=True,
            winner="AI"
        )
    
    return MoveResponse(
        ai_move=ai_action,
        game_over=game.get_end(),
        winner=None
    )