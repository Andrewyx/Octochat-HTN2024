import { useState, useRef, useEffect } from "react";
import { MdClose, MdOutlineMessage } from "react-icons/md";
import "./App.css";
import axios from "axios";


const App = () => {
  const [msgs, setMsgs] = useState<any>([]);
  const [curInput, setCurInput] = useState("");
  const [showInitialMessage, setShowInitialMessage] = useState(true);
  const [showDownloadButton, setShowDownloadButton] = useState(false);
  const [showPanel, setShowPanel] = useState();

  const inputRef = useRef<HTMLInputElement>(null);
  
  // Simulating a bot response after the user sends a message
  // const getBotResponse = (userMsg: string) => {
  //   return new Promise((resolve) => {
  //     setTimeout(() => {
  //       resolve(`Bot: I received your message: "${userMsg}"`);
  //     }, 1000); // Simulate a delay for bot response
  //   });
  // };

  const sendMessage = async () => {
    console.log(window.location.href);
    if (curInput.trim() === "") return;

    setShowInitialMessage(false);

    setShowDownloadButton(/https?:\/\/[^\s]+/.test(curInput)); // check if the message contains a URL
    const userMsg = `You: ${curInput}`;
    setMsgs((prev: any) => [...prev, userMsg]);
    console.log(curInput);

    const vfResponseCur = await interact({
      type: "text",
      payload: curInput,
    });

    setCurInput("");

    // const botResponse = await getBotResponse(curInput);
    setMsgs((prev: any) => [...prev, vfResponseCur]);

    setShowDownloadButton(false);

    inputRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  // const checkGithubURL = () => {
  //   const regex = /^https:\/\/github\.com\/[a-zA-Z0-9-]+\/[a-zA-Z0-9-]+$/;
  //   if (regex.test(curInput)) {
  //     setValidationMessage("Valid GitHub repository URL.");
  //   } else {
  //     setValidationMessage("Invalid GitHub repository URL.");
  //   }
  // }

  const interact = async (request: any) => {
    try {
      const response = await axios.post(
        `https://general-runtime.voiceflow.com/state/user/66e57d0592f43d1a82365bbe/interact`,
        { request: request },
        {
          headers: {
            Authorization: process.env.VOICEFLOW_API_KEY,
            versionID: "66e57d0592f43d1a82365bbf",
            accept: "application/json",
            "content-type": "application/json",
          },
        }
      );

      let data = response.data;
      data = data.filter((x: any) => x.type === "text")[0];
      console.log(data.payload.message);
      return data.payload.message;
    } catch (error) {
      console.error("Error interacting with Voiceflow:", error);
    }
  };
  return (
    <div className="chat-container">
      <div className="chat-header">
        <span className="title">Octochat</span>
        <MdClose 
          onClick={() => {}}
          size={24} 
          className="close-icon" 
        />
      </div>
      <div className="chat-window">
        {showInitialMessage &&
          <div className="header-text">
            <span className="cloud-icon">
              <img src="/icon/16.png" />
            </span>
            <p>Ask me anything about this repository!</p>
          </div>
        }
        {msgs.map((msg: any, index: number) => (
          <div key={index} className="message">
            {msg}
          </div>
        ))}
        <div ref={inputRef}></div>
      </div>

      <div className="input-container">
        <input
          value={curInput}
          onChange={(e) => setCurInput(e.target.value)}
          placeholder="Type your message..."
          className="input-box"
        />
        {showDownloadButton ? (
          <button className="download-button" onClick={() => alert('Repo uploaded!')}>
            Validate
          </button>
        ) : (
        <button className="send-button" onClick={sendMessage}>
          Enter
        </button>)}
      </div>
    </div>
  );
};

export default App;
