import { useEffect, useState } from "react";
import {
  fetchNotes,
  createNote,
  deleteNote,
} from "../services/api";
import NoteItem from "../components/NoteItem";

export default function NotesPage() {
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Load notes on page load
  useEffect(() => {
    loadNotes();
  }, []);

  async function loadNotes() {
    try {
      setLoading(true);
      const data = await fetchNotes();
      setNotes(data);
    } catch (err) {
      setError("Failed to load notes");
    } finally {
      setLoading(false);
    }
  }

  async function handleCreate(e) {
    e.preventDefault();

    if (!title.trim() || !content.trim()) {
      alert("Title and content are required");
      return;
    }

    try {
      await createNote({ title, content });
      setTitle("");
      setContent("");
      loadNotes();
    } catch (err) {
      alert("Failed to create note");
    }
  }

  async function handleDelete(id) {
    try {
      await deleteNote(id);
      loadNotes();
    } catch (err) {
      alert("Failed to delete note");
    }
  }

  return (
    <div style={{ maxWidth: "600px", margin: "40px auto" }}>
      <h1>Notes</h1>

      {/* Create Note */}
      <form onSubmit={handleCreate} style={{ marginBottom: "20px" }}>
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={{ width: "100%", marginBottom: "10px" }}
        />

        <textarea
          placeholder="Content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          rows="4"
          style={{ width: "100%", marginBottom: "10px" }}
        />

        <button type="submit">Add Note</button>
      </form>

      {/* Status */}
      {loading && <p>Loading notes...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {/* Notes List */}
      {notes.length === 0 && !loading && <p>No notes yet</p>}

      {notes.map((note) => (
        <NoteItem
          key={note.id}
          note={note}
          onDelete={handleDelete}
        />
      ))}
    </div>
  );
}
