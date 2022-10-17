from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

lang_select = driver.find_element(By.ID, "langSelect-EN")
lang_select.click()
driver.implicitly_wait(5)

cookie = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "bigCookie")))
cookie_count = driver.find_element(By.ID, "cookies")

items = [driver.find_element(By.ID, "productPrice" + str(i))
         for i in range(1, -1, -1)]

# actions = ActionChains(driver)

for i in range(5000):
    # actions.click(cookie).perform()
    cookie.click()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            # upgrade_actions = ActionChains(driver)
            # upgrade_actions.move_to_element(item)
            # upgrade_actions.click()
            # upgrade_actions.perform()

            item.find_element(By.XPATH, "../..").click()
