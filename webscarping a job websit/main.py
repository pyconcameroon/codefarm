from bs4 import BeautifulSoup
import requests
import lxml
import time

print('Put skills u dont want :')
unfamiliar_skills = input('>')
print(f"filtering out : {unfamiliar_skills}")

def find_jobs():
    html_text =  requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')

    soup = BeautifulSoup(html_text.content, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for job in jobs:
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:

            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','' )
            if unfamiliar_skills not in skill:
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ', ' ')
                more_info = job.header.h2.a['href']

            #results = (f'''
            #   Company name: {company_name}
            #   Required Skills: {skills}
            #   Published Date: {published_date}
            #   ''')
            #print(results)

                print(f"Company_name : {company_name.strip()}")#use strip to get rid of the blank spaces
                print(f"Required Skiles : {skills.strip()}")
                print(f"More Info : {more_info}")
                print('')



if __name__ == __main__:
    while True:
        find_jobs()
        time_wait = 30
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 20)