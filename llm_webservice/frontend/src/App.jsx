
import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  async function askQuestion() {
    console.log("clicked");

    const res = await fetch("http://127.0.0.1:5000/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: question }),
    });

    if (!res.ok) {
      const text = await res.text();
      console.error("Server error:", text);
      return;
    }

    const data = await res.json();
    console.log(data);

    setAnswer(data.answer);
  }

  return (
    <div style={{ maxWidth: "600px", margin: "40px auto" }}>
      <h1>Legal QA Demo</h1>

      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && question.trim() !== "") {
            askQuestion();
          }
        }}
        placeholder="개인정보법률에 관한 질문을 입력하세요"
        style={{
          width: "100%",
          padding: "12px",
          fontSize: "16px",
          marginBottom: "10px"
        }}
      />

      <button 
        onClick={askQuestion}
        style={{ padding: "10px 20px" }}
      >
        Ask
      </button>

      {answer && (
        <div style={{ marginTop: "20px" }}>
          <h3>Answer</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;

