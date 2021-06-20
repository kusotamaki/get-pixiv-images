import time
import sys
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    TARGET_URL = sys.argv[1] + '/artworks'

    driver = webdriver.Chrome()
    driver.get('https://www.pixiv.net/')

    # ユーザ検索
    driver.get(TARGET_URL)

    # ページング
    # TODO ページに作品が含まれなくなったら終わる
    page = 1
    while page < 10:
        driver.get(TARGET_URL + "?p=" + str(page))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        page += 1


if __name__ == '__main__':
    main()
