import requests
from bs4 import BeautifulSoup

JobPlannet_URL = "https://www.jobplanet.co.kr/contents"

def extract_jobplannet_header():
    result = requests.get(JobPlannet_URL)

    soup = BeautifulSoup(result.text, "html.parser")
    #print(job_soup)

    grid_main_banner_A = soup.find('ul', {"class" : "grid_main_banner_A"})

    links = grid_main_banner_A.find_all('h2') #h2 tag인 것만 pages에 저장
    pages = []

    for link in links:
        pages.append(link.string)

    max_header = pages[-1]
    return max_header