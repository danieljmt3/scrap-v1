from bs4 import BeautifulSoup
import requests
import pandas
import time

URL = "https://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=New+York&start=10"
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

def extract_job_title_from_result(soup): 
  jobs = []
  for div in soup.find_all(name="div", attrs={"class":"row"}):
    for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
      jobs.append(a["title"])
  return(jobs)
extract_job_title_from_result(soup)