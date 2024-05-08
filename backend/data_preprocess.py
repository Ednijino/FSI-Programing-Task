import os
import re
import pandas as pd
# from openai import OpenAI

# Read and combine all xbrl files in a directory
# input: directory - the directory containing the files
# output: a string containing the combined content of all files
def read_and_combine_files(directory):
    all_content = ""  # Initialize an empty string to hold all combined content
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r') as file:
                content = file.read()
                all_content += content + "\n"  # Append content and a newline for separation
    return all_content




# Extract financial data from the 10-K files
# input: directory - the directory containing the 10-K files
# output: a list of strings, each string containing the financial data from one 10-K file
def extract_financial_data(directory):
    all_data = []
    # Read the file content
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r') as file:
                content = file.read()
                
    
                # Define the start and end markers for the table
                start_marker = "FINANCIAL HIGHLIGHTS"
                # end_marker = "ITEM 6. SELECTED FINANCIAL DATA"

                # Find the start and end of the table using the markers
                start_index = content.find(start_marker)
                end_index = start_index + 2500

                # Check if both markers were found
                if start_index == -1:
                    print("Table not found in the file.")
                    return ""

                # Extract the table text
                table_text = content[start_index:end_index]
                all_data.append(table_text)

    return all_data

# upload the 10-k files to openai embedding model and get the embedding of the files, saved the embedding to a local file for future use
# input: ticker - the stock ticker
# output: None
# def get_embedding_from_open_ai(ticker):
#     client = OpenAI()
#     # Change MSFT to ticker
#     main_directory = 'sec-edgar-filings/MSFT/10-K' 
#     # Read all 10-k files
#     text = read_and_combine_files(main_directory) 
#     text = text.replace("\n", " ")
#     return client.embeddings.create(input = [text], model=model).data[0].embedding
    

# # get embedding for the ticker from the local saved file
# # input: ticker - the stock ticker
# # output: a pandas dataframe containing the embedding
# def get_embedding(ticker):
#     if os.path.exists(f"{ticker}_embedding.csv"):
#         return pd.read_csv(f"{ticker}_embedding.csv")
#     else:
#         get_embedding_from_open_ai(ticker)
#         return pd.read_csv(f"{ticker}_embedding.csv")

# Deprecated
# def get_tables(content):
#     tables = ""
#     start_tag = "<TABLE>"
#     end_tag = "</TABLE>"
    
#     # Starting index for search
#     start_index = 0
    
#     while True:
#         # Find the start of the table
#         start_loc = content.find(start_tag, start_index)
#         if start_loc == -1:
#             break  # No more tables found
        
#         # Find the end of the table
#         end_loc = content.find(end_tag, start_loc)
#         if end_loc == -1:
#             break  # No end tag found, should not happen if HTML is well-formed
        
#         # append the table
#         tables+=content[start_loc:end_loc + len(end_tag)]
        
#         # Update start_index to look for next table
#         start_index = end_loc + len(end_tag)
    
#     return tables