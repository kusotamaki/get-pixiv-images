
import time
import sys
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    USER_NAME = sys.argv[1]
    PASSWORD = sys.argv[2]

    driver = webdriver.Chrome()
    driver.get('https://www.pixiv.net/')

    # ログイン情報入力
    driver.find_element_by_class_name('signup-form__submit--login').click()
    driver.find_element_by_xpath("//input[@autocomplete='username']").send_keys(USER_NAME)
    driver.find_element_by_xpath("//input[@autocomplete='current-password']").send_keys(PASSWORD)
    driver.find_element_by_id("LoginComponent").find_element(By.TAG_NAME, 'form').submit()
    
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()
