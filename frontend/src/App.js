// import logo from './logo.svg';
// import './App.css';
// import React, { useState, useEffect } from 'react';
// import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

// const data = [
//   {
//     name: 'Page A',
//     uv: 4000,
//     pv: 2400,
//     amt: 2400,
//   },
//   {
//     name: 'Page B',
//     uv: 3000,
//     pv: 1398,
//     amt: 2210,
//   },
//   {
//     name: 'Page C',
//     uv: 2000,
//     pv: 9800,
//     amt: 2290,
//   },
//   {
//     name: 'Page D',
//     uv: 2780,
//     pv: 3908,
//     amt: 2000,
//   },
//   {
//     name: 'Page E',
//     uv: 1890,
//     pv: 4800,
//     amt: 2181,
//   },
//   {
//     name: 'Page F',
//     uv: 2390,
//     pv: 3800,
//     amt: 2500,
//   },
//   {
//     name: 'Page G',
//     uv: 3490,
//     pv: 4300,
//     amt: 2100,
//   },
// ];



// function App() {
//   const [return_value, setReturn_value] = useState(0);
//   useEffect(() => {
//     fetch('/api/content').then(res => res.json()).then(data => {
//       setReturn_value(data.content);
//     });
//   }, []);

  

//   fetch(`/api/data?param1=MSFT&param2=Risk`)
//   .then(response => response.json())
//   .then(data => console.log(data));


  
// }
import React, { useState } from 'react';
import axios from 'axios';
import ReactWordcloud from 'react-wordcloud';
import QueryComponent from './QueryComponent'
function App() {
  const [words, setWords] = useState([]);
  const [ticker, setTicker] = useState(''); // State to store the ticker input

  const handleTickerChange = (event) => {
      setTicker(event.target.value); // Update ticker on input change
  };

  const handleTickerSubmit = async () => {
      try {
          const response = await axios.post('/api/get_chart_data', { ticker });
          setWords(response.data.words);
      } catch (error) {
          console.error('Error fetching word cloud data:', error);
      }
  };

  return (
      <div>
          <input type="text" value={ticker} onChange={handleTickerChange} />
          <button onClick={handleTickerSubmit}>Generate Word Cloud</button>
          <ReactWordcloud words={words} />
      </div>,
      <div className="App">
      <header className="App-header">
        <QueryComponent />
      </header>
    </div>
  );
}

export default App;



