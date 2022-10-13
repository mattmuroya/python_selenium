# Python Selenium tutorial
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://techwithtim.net/")
print(driver.title)

# search = driver.find_element(By.NAME, "s")
# search.clear()
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )

#     articles = main.find_elements(By.TAG_NAME, "article")

#     for article in articles:
#         header = article.find_element(By.CLASS_NAME, "entry-summary")
#         print(header.text)
# finally:
#     driver.quit()

link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "sow-button-19310003"))
    )
    element.click()

    driver.back()
    driver.back()
    driver.back()
    # driver.forward()
    # driver.forward()

except:
    driver.quit()
