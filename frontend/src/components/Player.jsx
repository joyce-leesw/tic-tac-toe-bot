import { useState } from 'react';
import '../styles/Player.css';

export default function Player({ initialName, symbol, isActive, onChangeName }) {
	const [name, setName] = useState(initialName);
	const [isEditing, setIsEditing] = useState(false);

	function handleChange(event) {
		setName(event.target.value);
	}

	function handleEditClick() {
		setIsEditing((isEditing) => !isEditing);
		
		if (isEditing) {
			onChangeName(symbol, name);
		}
	}

	return (
		<li className={isActive ? 'active' : undefined}>
			<span className="player">
				{isEditing ? (
					<input type="text" required value={name} onChange={handleChange} />
				) : (
					<span className="player-name">{name}</span>
				)}
				<span className="player-symbol">{symbol}</span>
			</span>
			<button
				onClick={handleEditClick}
				className="save-button"
			>
				{isEditing ? 'Save' : 'Edit'}
			</button>
		</li>
	)
}