import requests
from bs4 import BeautifulSoup
import pickle
import os
import argparse
from dotenv import load_dotenv

class Job:
    def __init__(self, title, location):
        self.title = title
        self.location = location

    def __eq__(self, other):
        return self.title == other.title and self.location == other.location

    def __hash__(self):
        return hash((self.title, self.location))

def get_html_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def extract_job_details(soup):
    job_listings = set()
    departments = soup.find_all('div', class_='opening')
    for department in departments:
        title = department.find('a').text.strip()
        location = department.find('span', class_='location').text.strip()
        job_listings.add(Job(title, location))
    return job_listings

def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument('--all', action='store_true', help='Print all current jobs')
    parser.add_argument('--url', type=str, help='URL to scrape job listings from')
    args = parser.parse_args()

    url = args.url if args.url else os.getenv('URL')
    if url is None:
        print("Error: No URL provided. Please set the URL environment variable or use the --url option.")
        return
    soup = get_html_content(url)
    current_job_listings = extract_job_details(soup)

    if args.all:
        for job in current_job_listings:
            print(f"Title: {job.title}, Location: {job.location}")
    else:
        previous_job_listings = set()
        if os.path.exists('job_listings.pkl'):
            with open('job_listings.pkl', 'rb') as f:
                previous_job_listings = pickle.load(f)

        new_job_listings = current_job_listings - previous_job_listings
        for job in new_job_listings:
            print(f"New job listing - Title: {job.title}, Location: {job.location}")

        with open('job_listings.pkl', 'wb') as f:
            pickle.dump(current_job_listings, f)

if __name__ == "__main__":
    main()