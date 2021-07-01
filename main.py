import time
import sys
import chromedriver_binary
from selenium import webdriver


def main():
    TARGET_URL = 'https://www.pixiv.net/users/' + sys.argv[1] + '/artworks'
    driver = webdriver.Chrome()

    # ユーザ検索
    driver.get(TARGET_URL)

    # ページング
    page = 1
    while True:
        driver.get(TARGET_URL + '?p=' + str(page))
        time.sleep(1)
        if len(driver.find_elements_by_xpath('//span[text()=\"作品がありません\"]')) > 0:
            break
        else:
            # イラストのリンクを取得してBeautifulSoupで画像保存する
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            page += 1


if __name__ == '__main__':
    main()
