import data_preprocess
from analysis import *
from download_data import download_10_k
from xbrl_to_json import *
def test_get_chart_data():
    data = analysis.get_chart_data("MSFT")
    print(data)
    return

def test_get_answer_from_openai(ticker, question):
    return get_answer_from_openai(ticker, question)

if __name__ == '__main__':
    # download_10_k("AAPL")
    # # test_get_chart_data()
    # test_get_answer_from_openai("AAPL", "What is the net revenue change over year?")
    main_download_and_convert("AAPL", "0000320193", "10-K")


