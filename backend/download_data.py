from sec_edgar_downloader import Downloader

# Download filings to the current working directory
dl = Downloader("aa", "aa@gmail.com", "/workspace/backend")

# Get all 10-K filings for Microsoft without the filing details
dl.get("10-K", "MSFT", download_details=False)