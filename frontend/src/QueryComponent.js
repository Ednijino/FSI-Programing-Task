import React, { useState } from 'react';

const QueryComponent = () => {
    const [query, setQuery] = useState(''); // To hold the user's query
    const [answer, setAnswer] = useState(''); // To hold the API's response
    const [isLoading, setIsLoading] = useState(false); // Loading state

    const handleInputChange = (event) => {
        setQuery(event.target.value);
    };

    const handleFormSubmit = async (event) => {
        event.preventDefault(); // Prevent the form from refreshing the page
        setIsLoading(true); // Set loading state

        try {
            const response = await fetch('/api/get-answer', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question: query })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            setAnswer(data.answer); // Assuming the API returns an object with an 'answer' key
        } catch (error) {
            setAnswer('Failed to fetch answer');
            console.error('There was a problem with the fetch operation:', error);
        } finally {
            setIsLoading(false); // Reset loading state
        }
    };

    return (
        <div>
            <form onSubmit={handleFormSubmit}>
                <input
                    type="text"
                    value={query}
                    onChange={handleInputChange}
                    placeholder="Ask a question about the TSLA"
                />
                <button type="submit" disabled={isLoading}>
                    Get Answer
                </button>
            </form>
            <div>
                {isLoading ? <p>Loading...</p> : <p>Answer: {answer}</p>}
            </div>
        </div>
    );
};

export default QueryComponent;