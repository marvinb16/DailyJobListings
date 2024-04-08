# Job Listings Scraper
This is a Python script that scrapes job listings from a specified website and prints out the job title and location. It can also detect new job listings by comparing the current job listings with the previous ones.

## Installation
1. Clone this repository.
2. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```
## Usage
You can run the script from the command line with the following options:

--all: Print all current job listings. <br>
--url: Specify a URL to scrape job listings from.

## Environment Variables
The script uses the following environment variables:

## URL 
The default URL to scrape job listings from. This can be overridden with the --url command line option.
You can specify the environment variables in a .env file in the same directory as the script. Here's an example .env file:
Replace https://website.com with the actual URL you want to use.

## How It Works
The script uses the BeautifulSoup library to scrape job listings from the specified website. It then compares the current job listings with the previous ones, which are stored in a file named job_listings.pkl. If there are any new job listings, it prints them out and updates the job_listings.pkl file.
