import { useState } from 'react'


// /frontend/src/App.jsx


export default function App() {
  const [videoUrl, setVideoUrl] = useState('');
  const [sections, setSections] = useState([]);
  const [query, setQuery] = useState('');
  const [chatResponse, setChatResponse] = useState('');

  const handleSubmit = async () => {
    const res = await fetch('http://localhost:8000/process', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url: videoUrl })
    });
    const data = await res.json();
    setSections(data.sections);
  };

  const handleChat = async () => {
    const res = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    });
    const data = await res.json();
    setChatResponse(data.answer);
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h1 className="text-xl font-bold mb-4">Chat with YouTube Video</h1>

      <input
        className="w-full p-2 border rounded mb-2"
        placeholder="Paste YouTube video URL..."
        value={videoUrl}
        onChange={(e) => setVideoUrl(e.target.value)}
      />
      <button className="bg-blue-500 text-white px-4 py-2 rounded" onClick={handleSubmit}>
        Process Video
      </button>

      <div className="my-4">
        <h2 className="font-semibold">Sections:</h2>
        <ul>
          {sections.map((section, i) => (
            <li key={i}>
              <a
                href={`https://www.youtube.com/watch?v=${videoUrl.split('v=')[1]}&t=${section.timestamp}s`}
                target="_blank"
                className="text-blue-600 underline"
              >
                [{section.timestamp}s] {section.title}
              </a>
            </li>
          ))}
        </ul>
      </div>

      <div className="my-4">
        <input
          className="w-full p-2 border rounded mb-2"
          placeholder="Ask something about the video..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button className="bg-green-500 text-white px-4 py-2 rounded" onClick={handleChat}>
          Ask
        </button>
        <p className="mt-2 whitespace-pre-wrap">{chatResponse}</p>
      </div>
    </div>
  );
}
