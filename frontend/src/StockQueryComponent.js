import React, { useState } from 'react';
import axios from 'axios';

function StockQueryComponent() {
    const [ticker, setTicker] = useState('TSLA'); // Default ticker
    const [question, setQuestion] = useState('What is the risk of the company?'); // Default question
    const [answer, setAnswer] = useState(''); // Stores the fetched answer
    const [loading, setLoading] = useState(false); // Tracks whether the request is loading

    const handleTickerChange = (event) => {
        setTicker(event.target.value);
    };

    const handleQuestionChange = (event) => {
        setQuestion(event.target.value);
    };

    const handleSubmit = async () => {
        setLoading(true); // Set loading to true when the request starts
        try {
            const response = await axios.post("/api/get-answer", {
                ticker,
                question
            });
            setAnswer(response.data.answer); // Set the fetched answer
        } catch (error) {
            console.error('Error fetching data: ', error);
            setAnswer('Failed to fetch answer');
        } finally {
            setLoading(false); // Set loading to false when the request completes
        }
    };

    return (
        <div className="container">
            <div className="ticker-input">
                <input
                    type="text"
                    value={ticker}
                    onChange={handleTickerChange}
                    placeholder="Enter Ticker Symbol"
                />
            </div>
            <div className="question-section">
                <input
                    type="text"
                    value={question}
                    onChange={handleQuestionChange}
                    placeholder="Ask your question"
                    className="question-input"
                />
                <button onClick={handleSubmit} disabled={loading}>
                    {loading ? 'Loading...' : 'Submit'}
                </button>
                <div>
                    Answer: {loading ? 'Fetching answer...' : answer}
                </div>
            </div>
        </div>
    );
}

export default StockQueryComponent;