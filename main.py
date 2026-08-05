from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
import pyperclip


def get_number_from_share(count_num):
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.minimize_window()

    is_special = False

    try:
        driver.get('https://rngdle.com')
        wait = WebDriverWait(driver, 10)

        generate_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Generate a new number']"))
        )
        generate_btn.click()

        time.sleep(0.1)
        driver.refresh()

        share_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Copy to clipboard']"))
        )
        share_btn.click()

        time.sleep(0.1)
        share_content = pyperclip.paste()

        if share_content:
            print(f"第{count_num}次:\n {share_content}")
            if "MYTHIC" in share_content or "ANOMALY" in share_content or "EPIC" in share_content:
                is_special = True
                print(">>> 检测到特殊结果！请手动关闭浏览器窗口以继续...")

    except WebDriverException:
        pass 
    except Exception as e:
        print(f"第{count_num}次 错误: {e}")

    finally:
        if is_special:
            driver.set_window_position(0, 0)
            driver.maximize_window()
            while True:
                try:
                    _ = driver.title
                    time.sleep(0.5)
                except WebDriverException:
                    break
        else:
            driver.quit()


if __name__ == "__main__":
    counter = 0
    while True:
        counter += 1
        get_number_from_share(counter)
