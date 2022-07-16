from IndeedCrawler import extract_indeed_page, extract_indeed_jobs

last_indeed_page = extract_indeed_page()
jobs = extract_indeed_jobs(last_indeed_page)
print(jobs)