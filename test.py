from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


def get_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


# -----------------------------
# TEST 1: Homepage loads
# -----------------------------
def test_homepage():
    driver = get_driver()
    driver.get("http://172.31.31.8:5000")

    try:
        heading = driver.find_element(By.TAG_NAME, "h1").text

        if heading == "All Users":
            print("[✓] Homepage Loaded Successfully")
        else:
            print("[✗] Homepage loaded but heading mismatch")

    except Exception as e:
        print("[✗] Homepage Test Failed:", e)

    driver.quit()


# -----------------------------
# TEST 2: Add User
# -----------------------------
def test_add_user():
    driver = get_driver()
    driver.get("http://localhost:5000")

    try:
        driver.find_element(By.LINK_TEXT, "Add New User").click()
        time.sleep(1)

        driver.find_element(By.NAME, "name").send_keys("Test User")
        driver.find_element(By.NAME, "email").send_keys("test@example.com")

        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        time.sleep(1)

        page = driver.page_source

        if "Test User" in page and "test@example.com" in page:
            print("[✓] Add User Test Passed")
        else:
            print("[✗] User not found after adding")

    except Exception as e:
        print("[✗] Add User Test Failed:", e)

    driver.quit()


# -----------------------------
# RUN TESTS
# -----------------------------
if __name__ == "__main__":
    test_homepage()
    test_add_user()
