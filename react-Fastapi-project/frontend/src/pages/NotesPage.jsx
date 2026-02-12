import { useEffect, useState } from "react";
import { fetchNotes, createNote, deleteNote } from "../services/api";
import NoteForm from "../components/NoteForm";
import NoteList from "../components/NoteList";

export default function NotesPage() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    loadNotes();
  }, []);

  async function loadNotes() {
    const data = await fetchNotes();
    setNotes(data);
  }

  async function handleCreate(note) {
    await createNote(note);
    loadNotes();
  }

  async function handleDelete(id) {
    await deleteNote(id);
    loadNotes();
  }

  return (
    <div style={{ maxWidth: "600px", margin: "auto" }}>
      <h2>Public Notes</h2>
      <NoteForm onCreate={handleCreate} />
      <NoteList notes={notes} onDelete={handleDelete} />
    </div>
  );
}
