# 봇으로 인식해서 request할 수 없을 경우 => 셀레니움 설치(브라우저 자동화)!!
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# python에서 html 읽을 수있도록 => Beautifulsoup 설치!!
from bs4 import BeautifulSoup
# 다른 폴더에있는 파일을 main파일로 가져옴
from extractors.wwr import extract_wwr_job

Options = Options()
browser = webdriver.Chrome(options=Options)

base_url = "https://kr.indeed.com/job?q="
search_term = "python"
browser.get(f"{base_url}{search_term}")
results = []
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
# recursive=False => 한단계 깊이까지의 li만!!
jobs = job_list.find_all("li", recursive=False)
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        anchor = job.select_one("a")
        title = anchor['aria-label']
        link = anchor["href"]
        company = job.find("span", class_="comapanyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
            "link": f"https://kr.indeed.com{link}",
                    "company": company.string,
                    "location": location.string,
                    "position": title
        }
        results.append(job_data)

for result in results:
    print(result, "/////\n")
