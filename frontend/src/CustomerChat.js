import { useState } from "react";

function CustomerChat() {
  const [convId, setConvId] = useState("");
  const [msg, setMsg] = useState("");

  const send = async () => {
    await fetch(
      `http://127.0.0.1:8000/public_reply?conversation_id=${convId}&content=${msg}`,
      { method: "POST" }
    );
    setMsg("");
    alert("Message sent!");
  };

  return (
    <div style={{ padding: 40 }}>
      <h2>Customer Chat</h2>

      <input
        placeholder="Conversation ID"
        value={convId}
        onChange={e => setConvId(e.target.value)}
      />

      <input
        placeholder="Your message"
        value={msg}
        onChange={e => setMsg(e.target.value)}
      />

      <button onClick={send}>Send</button>
    </div>
  );
}

export default CustomerChat;
