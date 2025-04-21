import { useState } from 'react'
import './App.css'

function App() {
  const [query, setQuery] = useState('')
  const [transcript, setTranscript] = useState('')
  const [audioUrl, setAudioUrl] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [showTranscript, setShowTranscript] = useState(false)
  const [showAudio, setShowAudio] = useState(false)

  const backendUrl = import.meta.env.VITE_BACKEND_URL

  const handleSubmit = async (e) => {
    e.preventDefault()
    setIsLoading(true)
    setShowTranscript(false)
    setShowAudio(false)

    try {
      const response = await fetch(`${backendUrl}/rag-pipeline`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
      })

      const data = await response.json()
      setTranscript(data.answer)
      setAudioUrl(data.audio_file_url)

      setTimeout(() => {
        setShowTranscript(true)
        setTimeout(() => setShowAudio(true), 500)
      }, 500)

    } catch (err) {
      console.error('Error:', err)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#1a1a2e] v-ia-[#16213e] to-[#0f3460] text-white flex flex-col items-center justify-center px-6 py-12">
      
      <h1 className="text-5xl font-bold mb-10 pb-10 text-center  bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-blue-500">
        Justice Whisper - An Audio RAG on Legal Court Recordings
      </h1>

      <div className="w-full max-w-6xl grid grid-cols-1 md:grid-cols-2 gap-10">
        {/* Input Panel */}
        <div className="bg-slate-800 p-6 rounded-xl shadow-lg">
          <h2 className="text-2xl font-bold mb-4">Ask a Question</h2>
          <form onSubmit={handleSubmit}>
            <textarea
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              className="w-full p-4 bg-slate-700 border border-slate-600 rounded-lg text-white"
              rows="6"
              placeholder="Type your query here..."
              required
            />
            <button
              type="submit"
              disabled={isLoading}
              className="mt-4 bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg w-full font-semibold"
            >
              {isLoading ? 'Processing...' : 'Submit'}
            </button>
          </form>
        </div>

        {/* Output Panel */}
        <div className="bg-slate-800 p-6 rounded-xl shadow-lg">
          <h2 className="text-2xl font-bold mb-4">Response</h2>

          {showTranscript && (
            <div className="mb-4">
              <h3 className="font-semibold mb-2">Transcript:</h3>
              <div className="bg-slate-700 p-4 rounded-lg max-h-48 overflow-y-auto">
                <p className="whitespace-pre-wrap">{transcript}</p>
              </div>
            </div>
          )}

          {showAudio && (
            <div>
              <h3 className="font-semibold mb-2">Audio:</h3>
              <audio controls className="w-full">
                <source src={audioUrl} type="audio/mpeg" />
                Your browser does not support the audio element.
              </audio>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default App
