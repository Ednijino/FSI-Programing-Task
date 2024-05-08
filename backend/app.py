from flask import Flask, jsonify, request
# from openai import OpenAI
from data_preprocess import read_and_combine_files
from analysis import *

app = Flask(__name__)
ticker, question = "MSFT", "What is the net revenue change over year?"
# @app.route('/api/data')
# def set_data():
#     param1 = request.args.get('param1')
#     param2 = request.args.get('param2')


# @app.route("/api/content")
# def return_content():
    

#     main_directory = 'sec-edgar-filings/MSFT/10-K'
#     content = read_and_combine_files(main_directory)
#     return {'content': content}
income_data = {
    "TSLA": [
        {"date": "2020-Q1", "income": 950},
        {"date": "2020-Q2", "income": 1200},
        {"date": "2020-Q3", "income": 1500},
        {"date": "2020-Q4", "income": 1800},
        {"date": "2021-Q1", "income": 2100},
        {"date": "2021-Q2", "income": 2400},
        {"date": "2021-Q3", "income": 2700},
        {"date": "2021-Q4", "income": 3000},
    ],
    "AAPL": [
        {"date": "2020-Q1", "income": 5300},
        {"date": "2020-Q2", "income": 5600},
        {"date": "2020-Q3", "income": 5900},
        {"date": "2020-Q4", "income": 6200},
        {"date": "2021-Q1", "income": 6500},
        {"date": "2021-Q2", "income": 6800},
        {"date": "2021-Q3", "income": 7100},
        {"date": "2021-Q4", "income": 7400},
    ],
    "AMZN": [
        {"date": "2020-Q1", "income": 4200},
        {"date": "2020-Q2", "income": 4400},
        {"date": "2020-Q3", "income": 4600},
        {"date": "2020-Q4", "income": 4800},
        {"date": "2021-Q1", "income": 5000},
        {"date": "2021-Q2", "income": 5200},
        {"date": "2021-Q3", "income": 5400},
        {"date": "2021-Q4", "income": 5600},
    ]
}

@app.route('/api/income-data', methods=['GET'])
def get_income_data():
    try:
        ticker = request.args.get('ticker', default='TSLA', type=str)
        data = income_data.get(ticker)
        if data:
            return jsonify(data)
        else:
            return jsonify({"error": "Ticker not found"}), 404
    except Exception as e:
        # Logging the exception can be helpful for debugging
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500



def generate_word_frequencies(ticker):
    question = "Give me the top 25 word frequency in the files"
    return get_answer_from_openai(ticker, question)

    # return [{"text": "Example", "value": 100}, {"text": "Word", "value": 50}]

@app.route('/api/get-answer', methods=['POST'])
def get_answer():
    if request.is_json:
        data = request.json
        ticker = data['ticker']
        question = data['question']
        answer = get_answer_from_openai("TSLA", question)
        return {'question': question, 'answer': answer}
    else:
        return {{"error": "Request must be JSON"}, 400}