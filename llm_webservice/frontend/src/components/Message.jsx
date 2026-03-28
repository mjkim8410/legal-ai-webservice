export default function Message({ answer }) {
  if (!answer) return null;

  return (
    <div>
      <h3>Answer</h3>
      <p>{answer}</p>
    </div>
  );
}