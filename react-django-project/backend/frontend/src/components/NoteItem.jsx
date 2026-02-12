export default function NoteItem({ note, onDelete }) {
  return (
    <div
      style={{
        border: "1px solid #ddd",
        borderRadius: "6px",
        padding: "12px",
        marginBottom: "12px",
        backgroundColor: "#fafafa",
      }}
    >
      <h3 style={{ margin: "0 0 6px 0" }}>{note.title}</h3>

      <p style={{ margin: "0 0 10px 0" }}>{note.content}</p>

      <button
        onClick={() => onDelete(note.id)}
        style={{
          backgroundColor: "#e53935",
          color: "#fff",
          border: "none",
          padding: "6px 12px",
          borderRadius: "4px",
          cursor: "pointer",
        }}
      >
        Delete
      </button>
    </div>
  );
}
