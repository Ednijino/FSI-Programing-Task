# from openai import OpenAI
import os
from data_preprocess import read_and_combine_files, extract_financial_data
from collections import Counter
from utils import *
# Get the answer from openai
# input: ticker - the stock ticker
#        question - the question to ask openai
# output: the answer from openai
def get_answer_from_openai(ticker, question):
    
    file_path = f'10Kfillings/{ticker}/income_statement_merge.txt'
    
    # Memorize the data, the same document will only be processed once and cached.
    text = get_text(file_path)
    memory_path = memorize(text)
    
    return answer(question, memory_path)


def get_chart_data(ticker):
    
    # remember to change to ticker
    main_directory = file_path = f'10Kfillings/{ticker}/income_statement_merge.txt'
    # Get the chart data
    data 
    with open(main_directory, 'r') as file:
        data = file.read()
    # Create the prompt sending to chatgpt
    prompt = f"Analyze the following financial data from {ticker} 10-k files give me the csv data I can use to draw a line chart of it's net revenue change over year. return only the csv data"
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": f"{prompt}"},
            {"role": "system", "content": f"{data}"},
        ]
    )
    return completion.choices[0].message

# clean the text
def clean_text(text):
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lower case
    text = text.lower()
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# This is to get the word frequency of the 10-k files and make a word cloud
# input: ticker - the stock ticker
# output: an array of the 25 words with frequency high to low
def get_word_frequency(ticker):
    main_directory = 'sec-edgar-filings/MSFT/10-K' 
    # Read all 10-k files
    content = read_and_combine_files(main_directory) 
    # Clean the combined text
    cleaned_content = clean_text(content)
    
    # Split text into words and count frequencies
    words = cleaned_content.split()
    word_freq = Counter(words)
    
    # Get the 25 most common words
    top_25_words = word_freq.most_common(25)
    
    return top_25_words





# code for ask question about all tables in 10-k files to openai
# main_directory = 'sec-edgar-filings/MSFT/10-K' 
#     # Read all 10-k files
#     content = read_and_combine_files(main_directory) 
#     tables = get_tables(content)
#     prompt = "I have some tables from Microsoft 10-k files. you should analyze the table to find some insights.you return the meta data of the graph so I can draw it using react."
#     content = prompt + "\n" + tables
#     client = OpenAI()

#     completion = client.chat.completions.create(
#     model="gpt-4-turbo",
#     messages=[
#         {"role": "system", "content": f"{content[:]}"},
#     ]
#     )

#     print(completion.choices[0].message)

