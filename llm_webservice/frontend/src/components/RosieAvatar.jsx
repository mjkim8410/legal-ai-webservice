import { useState } from "react";
import rosieSearchingSvg from "../assets/rosie/rosie searching through books fixed.svg";
import rosieSearchingHoverSvg from "../assets/rosie/rosie searching annoyed.svg";
import rosieDefaultSvg from "../assets/rosie/rosie striking down.svg";
import rosieHoverSvg from "../assets/rosie/rosie shocked.svg";

export default function RosieAvatar({ isThinking }) {
  const [clicked, setClicked] = useState(false);

  const handleClick = () => {
    setClicked(true);
    setTimeout(() => setClicked(false), 1000); // revert after 1 second
  };

  // Determine which image to show
  let imageSrc;
  if (clicked) {
    imageSrc = isThinking ? rosieSearchingHoverSvg : rosieHoverSvg;
  } else {
    imageSrc = isThinking ? rosieSearchingSvg : rosieDefaultSvg;
  }

  return (
    <div style={{ marginBottom: "20px" }}>
      <div
        style={{
          width: "500px",
          height: "500px",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          overflow: "hidden",
          transition: "0.3s",
          margin: "0 auto",
          animation: isThinking && !clicked ? "pulse 1s infinite" : "none",
          cursor: "pointer",
        }}
        onClick={handleClick}
      >
        <img
          src={imageSrc}
          alt="Rosie"
          style={{
            width: "90%",
            height: "90%",
            objectFit: "contain",
            display: "block",
            margin: "0 auto",
          }}
        />
      </div>

      <style>
        {`
          @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.03); }
            100% { transform: scale(1); }
          }
        `}
      </style>
    </div>
  );
}