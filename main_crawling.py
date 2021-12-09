import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--start-maximized")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
url = "https://search.musinsa.com/ranking/best"
# url = "https://naver.com"
result = []
driver = webdriver.Chrome(executable_path='./driver/chromedriver', chrome_options=options)
driver.get(url)
# driver.find_elements_by_css_selector("div.gnb.wrapper.clearfix > ul > li")[2].click()
#wrapper > div.bottom-column.column.clearfix > div.sidebar > div.pcLeft.sectionLayer-store > section > div > div.g-tab-medium > ul > li.g-active
# print(driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[2]/div[2]/section/div/div[1]/ul/li[1]'))
# time.sleep(3)
allRankings = driver.find_element_by_id('goodsRankList')
allRankCloths = allRankings.find_elements_by_css_selector('.li_box')


for clothInfo in allRankCloths[:5]:
    result.append(
        {
            "brand": clothInfo.find_element_by_css_selector('p.item_title').text,
            "title": clothInfo.find_element_by_css_selector('p.list_info > a').get_attribute('title'),
            "price": clothInfo.find_element_by_css_selector('p.price').text.split()[1] if len(clothInfo.find_element_by_css_selector('p.price').text.split()) == 2 else clothInfo.find_element_by_css_selector('p.price').text,
            "urls": clothInfo.find_element_by_css_selector('p.list_info > a').get_attribute('href')
        }
    )
rankingData = pd.DataFrame(result)
rankingData.to_csv('rankingData.csv', encoding='cp949', index=0)
print('Data Success')