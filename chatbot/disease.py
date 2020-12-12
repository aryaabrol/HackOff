from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import re, csv

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("window-size=1024,768")
options.add_argument("--no-sandbox")
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

d_names = []

links = []

def cleandata(data):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', data)
    cleantext = cleantext.replace("\t", "")
    cleantext = cleantext.replace("\n\n", "\n")
    cleantext = cleantext.replace("&nbsp;", "")
    ref = cleantext.find("Reference")
    text = cleantext[:ref]
    return text

url = "https://www.nhp.gov.in/disease-a-z/"

for i in range(len(alpha)):
    new_url = url + alpha[i]
    driver.get(new_url)

    body = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "all-disease")))
    dis_list = body.find_element_by_tag_name("ul")
    list_items = dis_list.find_elements_by_tag_name("a")
    for j in range(len(list_items)):
        link = list_items[j].get_attribute("href")
        name = list_items[j].find_element_by_tag_name("li").text
        links.append(link)
        d_names.append(name)

print("Found links")

columns = ["Disease Name", "Links", "Information", "Symptoms", "Causes", "Diagnosis", "Management"]

with open('diseases.csv', "a", encoding='utf-8') as fp:
    wr = csv.writer(fp, dialect='excel')
    wr.writerow(columns)

for k in range(len(links)):
    print(k)
    try:
        driver.get(links[k])
        a = []
        
        a.append(d_names[k])
        a.append(links[k])

        try:
            intro = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Introduction")))
            i_cont = intro.get_attribute('innerHTML')
            i_content = cleandata(i_cont)
            ficont = i_content.strip()
            if(ficont == ""):
                a.append("No Information.")
            else:
                a.append(ficont)
        except:
            print("Intro not found.")
            a.append("No Information.")
        
        try:
            symp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Symptoms")))
            s_cont = symp.get_attribute('innerHTML')
            s_content = cleandata(s_cont)
            fscont = s_content.strip()
            if(fscont == ""):
                a.append("No Symptoms.")
            else:
                a.append(fscont)
        except:
            print("Symptoms not found.")
            a.append("No Symptoms.")
        
        try:
            cause = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Causes")))
            c_cont = cause.get_attribute('innerHTML')
            c_content = cleandata(c_cont)
            fccont = c_content.strip()
            if(fccont == ""):
                a.append("No Causes.")
            else:
                a.append(fccont)
        except:
            print("Causes not found.")
            a.append("No Causes.")
        
        try:
            diag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Diagnosis")))
            d_cont = diag.get_attribute('innerHTML')
            d_content = cleandata(d_cont)
            fdcont = d_content.strip()
            if(fdcont == ""):
                a.append("No Diagnosis.")
            else:
                a.append(fdcont)
        except:
            print("Diagnosis not found.")
            a.append("No Diagnosis.")
        
        try:
            mgmt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Management")))
            m_cont = mgmt.get_attribute('innerHTML')
            m_content = cleandata(m_cont)
            fmcont = m_content.strip()
            if(fmcont == ""):
                a.append("No Management.")
            else:
                a.append(fmcont)
        except:
            print("Management not found.")
            a.append("No Management.")
        
        with open('diseases.csv', "a", encoding='utf-8') as fp:
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(a)
    except:
        print("Could not scrape " + name + ", Link: " + links[k])

driver.quit()