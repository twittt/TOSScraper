import './App.css';
import React , {useState , useEffect} from 'react' 
import {io} from "socket.io-client"


function App() {
  const [url, setUrl] = useState(''); 
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [mentions , setMentions] = useState('');
  const [link , setLink] = useState('');
  const [socket , setSocket] = useState(null); 

  useEffect(()=> {
    const newSocket = io("http://127.0.0.1:5000" , { 
      
    }); 

    newSocket.on("connect" , () => {
      console.log('Connected to Flask Web Socket server') 
    })

    newSocket.on("result" , (result) => {
      console.log('Received number from flask:', result)
      setLoading(false);
      setResult(result.prohibited)
      setLink(result.found_page)
      setMentions(result.mentions);  
    })
 
    setSocket(newSocket);

    return () => {
      console.log("Clean up function called");
      newSocket.disconnect();
    }
  } , [])   

  const submitUrl = () => {
    setLoading(true);
    if (url && socket){
      socket.emit("check" , url) ; 
    }
  }

  const handleReset = () => {
    setUrl('');
    setResult(null);
    setLink(null)
    setMentions([]);
  };

  return (

    <div className="container">
      <h1>Tela's TOS Checker</h1>

      <form id="scrapingForm" onSubmit={submitUrl}>
          <input
              type="text"
              id="url"
              name="url"
              placeholder="Enter ecommerce website URL"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              required
          />
          <div className="buttons">
            <button onClick={submitUrl} disabled={loading}>Find Terms of Service</button>
            <button type="button" onClick={handleReset} disabled={loading}>Reset</button>
          </div>
      </form>

      {loading && <div className="loader"></div>}

      <br></br>
      <br></br>

      <div className="result" id="result">
          {result !== null && (
              <p style={{ color: result ? '#ff4d4d' : '#4dff88' }}>
                  {result
                      ? 'Web scraping is mentioned in the terms of service of the website.'
                      : 'No mentions of web scraping found in the terms of service of the website.'}
              </p>
          )}
          {result !== null && (
              <p>
                {result
                  ? 'Type CTRL + F and search for words like \"spider\" or \"scrape\" to find specific verbiage.'
                  : ''}
              </p>
          )}
          {link!== null&&(
            <p><a href={link} target="_blank">{link}</a></p>
          )}

          {mentions.length > 0 && (
              <div className="mentions">
                  {mentions.map((mention, index) => (
                      <p key={index}>{mention}</p>
                  ))}
              </div>
          )}
      </div>

    </div>
  );
}

export default App;
