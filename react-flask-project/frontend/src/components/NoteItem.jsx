const NoteItem = ({ note, onEdit, onDelete }) => {
  return (
    <div className="bg-white p-3 rounded shadow flex justify-between">
      <div>
        <h3 className="font-semibold">{note.title}</h3>
        <p className="text-sm">{note.content}</p>
      </div>
      <div className="space-x-2">
        <button
          onClick={() => onEdit(note)}
          className="text-blue-600"
        >
          Edit
        </button>
        <button
          onClick={() => onDelete(note.id)}
          className="text-red-600"
        >
          Delete
        </button>
      </div>
    </div>
  );
};

export default NoteItem;
