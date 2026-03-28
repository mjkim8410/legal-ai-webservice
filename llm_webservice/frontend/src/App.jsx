import { useState } from "react";
import ChatInput from "./components/ChatInput";
import Message from "./components/Message";
import RosieAvatar from "./components/RosieAvatar";
import AnswerCard from "./components/AnswerCard";
import { askLegalQuestion } from "./services/api";
import rosieDefaultSvg from "./assets/rosie/rosie holding up a hammer.svg";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [done, setDone] = useState(false);

  async function handleAsk() {
    if (loading) return;
    try {
      setDone(false);
      setLoading(true);
      setAnswer("");
      const data = await askLegalQuestion(question);
      setAnswer(data.answer);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
      setDone(true);
    }
  }

  return (
    <div style={{ width: "100%", margin: "40px auto" }}>

      {/* Header (narrower) */}
      <div style={{ maxWidth: "800px", margin: "0 auto" }}>
        <h1
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            gap: "20px",
            margin: 0,
            fontSize: "68px"
          }}
        >
          <img src={rosieDefaultSvg} style={{ height: "120px" }} />
          법률 도우미 로지
        </h1>
      </div>

      {/* Search area (wider) */}
      <div style={{ width: "70%", margin: "40px auto", padding: "0 40px" }}>
        <div
          style={{
            display: "flex",
            alignItems: "stretch",
            gap: "20px"
          }}
        >
          <div style={{ display: "flex", width: "100%" }}>
            <ChatInput
              question={question}
              setQuestion={setQuestion}
              onSubmit={handleAsk}
              loading={loading}
            />
          </div>
        </div>
      </div>

      {/* Loading / Rosie Avatar + Text */}
      <div style={{ marginTop: "10px", textAlign: "center" }}>
        <RosieAvatar isThinking={loading} isDone={done} />
        <div style={{ marginTop: "10px", fontSize: "16px" }}>
          {loading && <p>🤔 로지가 열심히 찾는 중이에요… 🔍</p>}
          {!loading && done && <p>😊 로지가 답을 찾았어요!</p>}
        </div>

        {/* Pulse animation */}
        <style>
          {`
            @keyframes pulse {
              0% { transform: scale(1); }
              50% { transform: scale(1.05); }
              100% { transform: scale(1); }
            }
          `}
        </style>
      </div>

      {/* Answer */}
      <div style={{ display: "flex", width: "90%", margin: "auto" }}>
        <AnswerCard answer={answer} />
      </div>

    </div>
  );
}

export default App;