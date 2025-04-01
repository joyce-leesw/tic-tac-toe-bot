import '../styles/Gameboard.css';

export default function GameBoard({ onSelectSquare, board }) {
	return <ol id="game-board">
		{board.map((row, rowIndex) => (
			<li key={rowIndex}>
				<ol>
					{row.map((playerSymbol, colIndex) => (
						<li key={colIndex}>
							<button 
								onClick={() => onSelectSquare(rowIndex, colIndex)} 
								disabled={playerSymbol !== null}
								className="player-symbol-board"
							>
								{playerSymbol}
							</button>
						</li>
					))}
				</ol>
			</li>
		))}
	</ol>
}