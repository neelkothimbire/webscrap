# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import time

# Ask the user for an unfamiliar skill
print('Enter an unfamiliar skill:')
unfamiliar_skill = input('> ')
print(f'Filtering out jobs that require {unfamiliar_skill}')

# Function to find jobs related to Data Science
def find_jobs():
    # Get HTML content from TimesJobs website
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Science&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # Iterate through each job
    for index, job in enumerate(jobs):
        job_published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in job_published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')  # Remove white spaces
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            
            # Check if the unfamiliar skill is not required for the job
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'a') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required skills: {skills.strip()}\n")
                    f.write(f"Link: {more_info.strip()}\n")
                print(f'File Saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} min...')
        time.sleep(time_wait * 60)


