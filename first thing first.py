from selenium import webdriverfrom selenium.webdriver.common.by import Byfrom selenium.webdriver.support.ui import WebDriverWait as waitfrom selenium.webdriver.support import expected_conditions as ECfrom bs4 import BeautifulSoupdriver = webdriver.PhantomJS()driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')try:    element = wait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loadedButton')))finally:    print(driver.find_element_by_tag_name('div').text)driver.close()#beautifulsoup selector way#source = driver.page_source#soup = BeautifulSoup(source)#print(soup.find(id = 'content').get_text())