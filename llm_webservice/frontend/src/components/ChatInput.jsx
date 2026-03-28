import { useRef } from "react";
import "../App.css"

export default function ChatInput({ question, setQuestion, onSubmit, loading  }) {
  const textareaRef = useRef(null);

  // 🔥 자동 높이 조절
  const handleChange = (e) => {
    setQuestion(e.target.value);

    const el = textareaRef.current;
    el.style.height = "auto";
    el.style.height = el.scrollHeight + "px";
  };

  return (
    <div
      style={{
        width: "100%",
        marginTop: "20px",
        position: "relative",
        display: "flex"   
      }}
    >
      
      <textarea
        className="chat-textarea"
        ref={textareaRef}
        value={question}
        onChange={handleChange}
        placeholder="개인정보에 관한거라면 뭐든지 물어보라구!"
        rows={1}
        style={{
          width: "100%",
          flex: 1,
          padding: "16px",
          paddingRight: "70px",
          borderRadius: "24px",
          resize: "none",          
          overflow: "hidden",      
          boxSizing: "border-box",
        }}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            if (question.trim()) onSubmit();
          }
        }}
      />

      <button
        onClick={onSubmit}
        disabled={loading}
        className="send-button"
        onChange={handleChange}
        style={{
          marginTop: "10px",
          padding: "8px 12px",
          borderRadius: "24px",
          cursor: "pointer",
          position: "absolute",
          right: "8px",
        }}
      >
        ➤
      </button>

    </div>
  );
}