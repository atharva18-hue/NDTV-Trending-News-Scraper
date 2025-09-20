from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--ignore-certificate-errors")  # SSL issues fix
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.ndtv.com")

driver.find_element(By.CSS_SELECTOR, "a[href*='latest']").click()
driver.find_elements(By.CSS_SELECTOR, "h2 a")[0].click()

headline = driver.find_element(By.TAG_NAME, "h1").text
paragraph = driver.find_elements(By.TAG_NAME, "p")[0].text

print("\n📰 Trending News:")
print(headline)
print(paragraph)

driver.quit()

