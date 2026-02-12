import { useEffect, useState } from "react";
import { fetchNotes, createNote, updateNote, deleteNote } from "../api/noteApi";
import NoteForm from "../components/NoteForm";
import NoteItem from "../components/NoteItem";

const NotesPage = () => {
  const [notes, setNotes] = useState([]);
  const [editingNote, setEditingNote] = useState(null);

  // READ
  const loadNotes = async () => {
    const res = await fetchNotes();
    setNotes(res.data);
  };

  // CREATE
  const handleCreate = async (data) => {
    const res = await createNote(data);
    setNotes([...notes, res.data]);
  };

  // UPDATE
  const handleUpdate = async (id, data) => {
    const res = await updateNote(id, data);
    setNotes(notes.map(n => n.id === id ? res.data : n));
    setEditingNote(null);
  };

  // DELETE
  const handleDelete = async (id) => {
    await deleteNote(id);
    setNotes(notes.filter(n => n.id !== id));
  };

  useEffect(() => {
    loadNotes();
  }, []);

  return (
    <div className="max-w-xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Notes App</h1>

      <NoteForm
        onSubmit={editingNote ? handleUpdate : handleCreate}
        editingNote={editingNote}
      />

      <div className="mt-4 space-y-2">
        {notes.map(note => (
          <NoteItem
            key={note.id}
            note={note}
            onEdit={setEditingNote}
            onDelete={handleDelete}
          />
        ))}
      </div>
    </div>
  );
};

export default NotesPage;
