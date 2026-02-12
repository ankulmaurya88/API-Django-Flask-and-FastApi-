import { useEffect, useState } from "react";

const NoteForm = ({ onSubmit, editingNote }) => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  useEffect(() => {
    if (editingNote) {
      setTitle(editingNote.title);
      setContent(editingNote.content);
    }
  }, [editingNote]);

  const handleSubmit = () => {
    if (!title || !content) return;
    onSubmit(editingNote?.id, { title, content });
    setTitle("");
    setContent("");
  };

  return (
    <div className="bg-white p-3 rounded shadow">
      <input
        className="border p-2 w-full mb-2"
        placeholder="Title"
        value={title}
        onChange={e => setTitle(e.target.value)}
      />
      <textarea
        className="border p-2 w-full mb-2"
        placeholder="Content"
        value={content}
        onChange={e => setContent(e.target.value)}
      />
      <button
        onClick={handleSubmit}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        {editingNote ? "Update" : "Add"}
      </button>
    </div>
  );
};

export default NoteForm;
