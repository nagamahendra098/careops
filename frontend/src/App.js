import { useEffect, useState } from "react";
import "./styles.css";

function App() {
  const [dashboard, setDashboard] = useState(null);
  const [conversations, setConversations] = useState([]);
  const [messages, setMessages] = useState([]);
  const [calendar, setCalendar] = useState([]);

  const [selected, setSelected] = useState(null);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [reply, setReply] = useState("");

  // ---------------- LOAD ALL DATA ----------------
  const loadData = () => {
    fetch("https://careops-mf4t.onrender.com/dashboard")
      .then(res => res.json())
      .then(setDashboard);

    fetch("https://careops-mf4t.onrender.com/conversations")
      .then(res => res.json())
      .then(setConversations);

    fetch("https://careops-mf4t.onrender.com/calendar")
      .then(res => res.json())
      .then(setCalendar);
  };

  useEffect(() => {
    loadData();
  }, []);

  // ---------------- CREATE CONTACT ----------------
  const createContact = async () => {
    if (!name) return;

    await fetch(
      `https://careops-mf4t.onrender.com/contact?name=${name}&email=${email}`,
      { method: "POST" }
    );

    setName("");
    setEmail("");
    loadData();
  };

  // ---------------- LOAD MESSAGES ----------------
  const loadMessages = (id) => {
    setSelected(id);

    fetch(`https://careops-mf4t.onrender.com/messages/${id}`)
      .then(res => res.json())
      .then(setMessages);
  };

  // ---------------- SEND STAFF REPLY ----------------
  const sendReply = async () => {
    if (!reply) return;

    await fetch(
      `https://careops-mf4t.onrender.com/reply?conversation_id=${selected}&content=${reply}`,
      { method: "POST" }
    );

    setReply("");
    loadMessages(selected);
  };

  // ---------------- CREATE BOOKING ----------------
  const createBooking = async (contactId) => {
    await fetch(
      `https://careops-mf4t.onrender.com/booking?contact_id=${contactId}&date=2026-02-20&time=5pm`,
      { method: "POST" }
    );

    loadData();
  };

  return (
    <div className="layout">
      {/* SIDEBAR */}
      <div className="sidebar">
        <h2>CareOps</h2>
        <p>Dashboard</p>
        <p>Inbox</p>
        <p>Calendar</p>
        <p>Settings</p>
      </div>

      {/* MAIN CONTENT */}
      <div className="main">
        <h1>Business Dashboard</h1>

        {/* DASHBOARD CARDS */}
        {dashboard && (
          <div className="cards">
            <Card title="Contacts" value={dashboard.total_contacts} />
            <Card title="Bookings" value={dashboard.total_bookings} />
            <Card title="Today" value={dashboard.today_bookings} />
            <Card title="Messages" value={dashboard.total_messages} />
          </div>
        )}

        {/* CALENDAR PANEL */}
        <div className="panel">
          <h3>📅 Calendar</h3>

          <div className="calendar">
            {calendar.map(b => (
              <div key={b.id} className="calendarItem">
                <b>{b.date}</b> — {b.time}
                <div>Contact {b.contact_id}</div>
              </div>
            ))}
          </div>
        </div>

        {/* GRID LAYOUT */}
        <div className="grid">
          {/* LEFT PANEL - INBOX */}
          <div className="panel">
            <h3>Inbox</h3>

            {conversations.map(c => (
              <div className="conv" key={c.id}>
                <div>
                  <b>Contact {c.contact_id}</b>
                </div>

                <div>
                  <button onClick={() => loadMessages(c.id)}>
                    Open
                  </button>

                  <button
                    onClick={() => createBooking(c.contact_id)}
                    className="secondary"
                  >
                    Book
                  </button>
                </div>
              </div>
            ))}

            <hr />

            <h3>Add Contact</h3>
            <input
              placeholder="Name"
              value={name}
              onChange={e => setName(e.target.value)}
            />
            <input
              placeholder="Email"
              value={email}
              onChange={e => setEmail(e.target.value)}
            />
            <button onClick={createContact}>Add</button>
          </div>

          {/* RIGHT PANEL - CHAT */}
          <div className="panel chat">
            {!selected && <p>Select a conversation</p>}

            {selected && (
              <>
                <div className="chatbox">
                  {messages.map(m => (
                    <div
                      key={m.id}
                      className={
                        m.sender === "staff"
                          ? "msg staff"
                          : m.sender === "customer"
                          ? "msg customer"
                          : "msg system"
                      }
                    >
                      {m.content}
                    </div>
                  ))}
                </div>

                <div className="reply">
                  <input
                    value={reply}
                    onChange={e => setReply(e.target.value)}
                    placeholder="Type reply..."
                  />
                  <button onClick={sendReply}>Send</button>
                </div>
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

// ---------- CARD COMPONENT ----------
const Card = ({ title, value }) => (
  <div className="card">
    <p>{title}</p>
    <h2>{value}</h2>
  </div>
);

export default App;
