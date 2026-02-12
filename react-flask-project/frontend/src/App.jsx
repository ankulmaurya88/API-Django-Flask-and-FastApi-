import { useState } from 'react'

import NotesPage from "./pages/NotesPage";

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className="min-h-screen bg-gray-100">
      <NotesPage />
    </div>
    </>
  )
}

export default App
