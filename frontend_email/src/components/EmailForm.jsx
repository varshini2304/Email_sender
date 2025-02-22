import { useState } from "react";
import axios from "axios";

const EmailForm = () => {
  const [email, setEmail] = useState({ to: "", subject: "", body: "" });
  const [message, setMessage] = useState("");

const sendEmail = async (e) => {
  e.preventDefault();
  try {
    const res = await axios.post(
      "http://127.0.0.1:5000/send-email", // Ensure this matches your backend URL
      email,
      { headers: { "Content-Type": "application/json" } }
    );
    setMessage(res.data.message || "Email sent successfully!");
  } catch (error) {
    setMessage(error.response?.data?.error || "Error sending email. Check the backend logs.");
  }
};

  return (
    <div>
      <h2>Send Email</h2>
      <form onSubmit={sendEmail}>
        <input
          type="email"
          placeholder="Recipient Email"
          required
          value={email.to}
          onChange={(e) => setEmail({ ...email, to: e.target.value })}
        />
        <input
          type="text"
          placeholder="Subject"
          required
          value={email.subject}
          onChange={(e) => setEmail({ ...email, subject: e.target.value })}
        />
        <textarea
          placeholder="Message"
          required
          value={email.body}
          onChange={(e) => setEmail({ ...email, body: e.target.value })}
        />
        <button type="submit">Send</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default EmailForm;
