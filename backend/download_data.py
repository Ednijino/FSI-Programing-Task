from sec_edgar_downloader import Downloader
# Download 10-K filings for ticker, saved in the current working directory
# Input: ticker - the stock ticker
# Output: None
def download_10_k(ticker):
    # Download filings to the current working directory
    dl = Downloader("aa", "aa@gmail.com", "/workspace/backend")

    # Get all 10-K filings for Microsoft without the filing details
    count = dl.get("10-K", ticker, download_details=False, limit = 2)
    if count == 0:
        print("No 10-K filings found the ticker check if the ticker is correct")