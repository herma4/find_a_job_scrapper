import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm

q = input("검색어| 업종, 직무 및 회사명")# 검색어 입력
limit = 50 # 페이지 당 최대 검색결과 수 노출 수
INDEED_URL = "https://kr.indeed.com/jobs?q=" + str(q) + "&limit=" + str(limit)

def extract_indeed_page():
    url = INDEED_URL 
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    searchCountPages = soup.find("div", id="searchCountPages").text
    searchCountPages = searchCountPages.split("결과")[-1]
    searchCountPages = re.sub("[^0-9]", "", searchCountPages)
    searchCountPages = int(searchCountPages)

    max_indeed_page =  searchCountPages // limit
    return max_indeed_page

def extract_indeed_jobs(last_page):
    jobs = []
    for page in tqdm(range(last_page)):
        result = requests.get(INDEED_URL + "&start=" + str(page*limit))
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", class_="job_seen_beacon")
        for result in results:
            title = result.find("h2").text
            companyName = result.find("span", class_="companyName").text
            companyLocation = result.find("div", class_="companyLocation").text
            jobUrl = "https://kr.indeed.com" + result.find("a")["href"]
            jobs.append({"title": title, "companyName": companyName, "companyLocation": companyLocation, "jobUrl": jobUrl})
    return jobs