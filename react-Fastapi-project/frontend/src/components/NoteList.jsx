import NoteItem from "./NoteItem";

export default function NoteList({ notes, onDelete }) {
  return (
    <div>
      {notes.map((note) => (
        <NoteItem key={note.id} note={note} onDelete={onDelete} />
      ))}
    </div>
  );
}
