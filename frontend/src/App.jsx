import Player from "./components/Player";
import GameBoard from "./components/GameBoard";
import { useState, useEffect } from "react";
import Log from "./components/Log";
import GameOver from "./components/GameOver";
import axios from "axios";
import Error from "./components/Error";

const PLAYERS = {
  X: 'Player 1',
  O: 'AI'
};

const INITIAL_GAMEBOARD = Array(3).fill(Array(3).fill(null));

function App() {
  const [players, setPlayers] = useState(PLAYERS);
  const [gameTurns, setGameTurns] = useState([]);
  const [gameBoard, setGameBoard] = useState(() => JSON.parse(JSON.stringify(INITIAL_GAMEBOARD)));
  const [activePlayer, setActivePlayer] = useState('X');
  const [winner, setWinner] = useState(null);
  const [hasDraw, setHasDraw] = useState(false);
  const [errors, setErrors] = useState();

  const resetGame =  async () => {
    try {
      await axios.post("http://127.0.0.1:8000/reset");
      setGameBoard(JSON.parse(JSON.stringify(INITIAL_GAMEBOARD)));
      setGameTurns([]);
      setWinner(null);
      setHasDraw(false);
      setActivePlayer('X');
    } catch (error) {
      console.error("Error resetting game:", error);
      setErrors({ message: error.message || 'Failed to reset tic tac toe board.'})
    }
  };

  const handlePlayerMove = (row, col, player) => {
    setGameBoard((prevBoard) =>
      prevBoard.map((r, rIdx) => rIdx === row ? r.map((cell, cIdx) => (cIdx === col ? player : cell)) : r)
    );
    setGameTurns((prevTurns) => [
      { square: { row, col }, player },
      ...prevTurns,
    ]);
  };

  // Handle player move and communicate with backend
  const handleSelectSquare = async (rowIndex, colIndex) => {
    if (gameBoard[rowIndex][colIndex] || winner || hasDraw) return;

    handlePlayerMove(rowIndex, colIndex, 'X');
    setActivePlayer('O');

    try {
      const { data } = await axios.post("http://127.0.0.1:8000/play", {
        row: rowIndex,
        column: colIndex
      });
      const { ai_move, winner, game_over } = data;
      if (winner && winner != 'AI') setWinner(players['X']);
      if (game_over) setHasDraw(!winner && game_over);

      setActivePlayer('O');
    
      if (ai_move) {
        setTimeout(() => {
          handlePlayerMove(ai_move[0], ai_move[1], 'O');
          if (winner) setWinner(players['O']);
          if (!winner && !game_over) setActivePlayer('X');
        }, 500);
      }

    } catch (error) {
      console.error("Error sending player move to server:", error);
      setErrors({ message: error.message || 'Failed to play tic tac toe.'})
    }
  };

  function handlePlayerNameChange(symbol, newName) {
    setPlayers((prevPlayers) => ({
      ...prevPlayers,
      [symbol]: newName
    }));
  }

  function handleError() {
    setErrors(null);
  }

  useEffect(() => {
    resetGame();
  }, []);

  return (
    <main>
      <div id="game-container">
        {errors && 
          <Error title="An error has occurred!" message={errors.message} onConfirm={handleError}></Error>
        }
        <ol id="players" className="highlight-player">
          {Object.keys(PLAYERS).map((symbol) => (
            <Player
              key={symbol}
              initialName={PLAYERS[symbol]}
              symbol={symbol}
              isActive={activePlayer === symbol}
              onChangeName={handlePlayerNameChange}
            />
          ))}
        </ol>
        {(winner || hasDraw) &&
          <GameOver winner={winner} onRestart={resetGame} />
        }
        <GameBoard
          onSelectSquare={handleSelectSquare}
          board={gameBoard}
        />
      </div>
      <Log turns={gameTurns} />
    </main>
  );
}

export default App;

