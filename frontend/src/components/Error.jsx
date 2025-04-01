import '../styles/Error.css';

export default function Error({ title, message, onConfirm }) {
	return (
		<div id="error">
			<h3>{title}</h3>
			<p>{message}</p>
			<p>
				<button onClick={onConfirm}>Okay</button>
			</p>
		</div>
	);
}