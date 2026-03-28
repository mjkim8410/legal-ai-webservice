export default function AnswerCard({ answer }) {
  if (!answer) return null;

  // 🔥 임시 파싱 (나중에 백엔드 구조화 가능)
  const sections = answer.split("\n");

    /*
  return (
    <div className="answer-card">
      
      <div className="section">
        <div className="title">📌 요약</div>
        <p>{sections[0]}</p>
      </div>

      <div className="section">
        <div className="title">📖 관련 법 조항</div>
        <p>{sections[1] || "관련 법 조항 정보 없음"}</p>
      </div>

      <div className="section">
        <div className="title">🧠 로지의 해석</div>
        <p>{sections[2] || "해석 정보 없음"}</p>
      </div>

      <div className="section warning">
        <div className="title">⚠️ 주의사항</div>
        <p>{sections[3] || "법률 자문이 아닌 참고용입니다."}</p>
      </div>

    </div>
  ); */

  return (
    <div className="answer-card">
      
      <div className="section">
        <div className="title"></div>
        <p>{answer}</p>
      </div>

    </div>
  );
}