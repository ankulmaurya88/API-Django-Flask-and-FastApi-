const BASE_URL = "http://127.0.0.1:8000";

export async function fetchNotes() {
  const res = await fetch(`${BASE_URL}/notes`);
  return res.json();
}

export async function createNote(note) {
  const res = await fetch(`${BASE_URL}/notes`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(note),
  });
  return res.json();
}

export async function deleteNote(id) {
  await fetch(`${BASE_URL}/notes/${id}`, {
    method: "DELETE",
  });
}
