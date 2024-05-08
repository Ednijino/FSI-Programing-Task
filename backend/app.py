from flask import Flask, request
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


@app.route("/api/get_chart_data", methods=['POST'])
def return_chart_data():
    print("Getting chart data")
    ticker = request.json.get('ticker')
    # Process the ticker to generate word frequencies
    word_frequencies = generate_word_frequencies(ticker)
    return {"words": word_frequencies}

def generate_word_frequencies(ticker):
    question = "Give me the top 25 word frequency in the files"
    return get_answer_from_openai(ticker, question)

    # return [{"text": "Example", "value": 100}, {"text": "Word", "value": 50}]

@app.route('/api/get-answer', methods=['POST'])
def get_answer():
    if request.is_json:
        # Parse the incoming JSON data
        data = request.get_json()
        question = data.get('question', '')
        answer = get_answer_from_openai("TSLA", question)
        return {'question': question, 'answer': answer}
    else:
        return {{"error": "Request must be JSON"}, 400}