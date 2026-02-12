const BASE_URL = "http://localhost:8000/api";

export async function fetchNotes() {
  const response = await fetch(`${BASE_URL}/notes/`);
  return response.json();
}

export async function createNote(note) {
  const response = await fetch(`${BASE_URL}/notes/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(note),
  });
  return response.json();
}

export async function deleteNote(id) {
  await fetch(`${BASE_URL}/notes/${id}/`, {
    method: "DELETE",
  });
}
