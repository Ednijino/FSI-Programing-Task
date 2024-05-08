
import StockQueryComponent from './StockQueryComponent';
import IncomeChartComponent from './IncomeChartComponent';

import React, { useState } from 'react';
import './App.css';

function App() {
    const [ticker, setTicker] = useState('TSLA'); // Default ticker is TSLA
  
    return (
      <div className="App">
        <header className="App-header">
          <h1>Financial Dashboard</h1>
        </header>
        {/* <IncomeChartComponent ticker={ticker} /> */}
        <StockQueryComponent />
      </div>
    );
  }

export default App;




