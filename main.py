from IndeedCrawler import get_jobs as get_indeed_jobs
from save import to_csv

indeed_jobs = get_indeed_jobs()
to_csv(indeed_jobs)