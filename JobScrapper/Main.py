import requests
from bs4 import BeautifulSoup
job_result = requests.get("https://www.jobplanet.co.kr/contents")

job_soup = BeautifulSoup(job_result.text, "html.parser")
#print(job_soup)

grid_main_banner_A = job_soup.find('ul', {"class" : "grid_main_banner_A"})

links = grid_main_banner_A.find_all('h2') #h2 tag인 것만 pages에 저장
pages = []

for link in links:
    pages.append(link.string)

pages = pages[0:-1]
print(pages)