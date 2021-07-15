import os
import time
import sys
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By


class Main:

    def __init__(self, target, user_name, password):
        self.user_name = user_name
        self.password = password
        self.target_url = 'https://www.pixiv.net/users/' + target + '/artworks'

    def process(self):
        # set options
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=./Chrome')
        driver = webdriver.Chrome(options=options)
        driver.get('https://www.pixiv.net/')

        # login
        if len(driver.find_elements_by_class_name('signup-form__submit--login')):
            driver.find_element_by_class_name('signup-form__submit--login').click()
            driver.find_element_by_xpath("//input[@autocomplete='username']").send_keys(self.user_name)
            driver.find_element_by_xpath("//input[@autocomplete='current-password']").send_keys(self.password)
            driver.find_element_by_id("LoginComponent").find_element(By.TAG_NAME, 'form').submit()
            time.sleep(5)

        # Crawling pixiv and save image urls.
        page, url_list = 1, []
        while True:
            driver.get(self.target_url + '?p=' + str(page))
            time.sleep(1)

            if len(driver.find_elements_by_xpath('//span[text()=\"作品がありません\"]')) > 0:
                break
            else:
                # TODO refactor.
                elements = driver.find_elements_by_xpath("//a[contains(@href,'/artworks/')]")
                for element in elements:
                    url = element.get_attribute("href")
                    if 'users' not in url and url not in url_list:
                        url_list.append(url)

                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                page += 1

        # Access image url.
        img_src_list = []
        for url in url_list:
            print(url)
            driver.get(url)
            src_list = driver.find_elements_by_tag_name("img")
            for src in src_list:
                img_src_list.append(src.get_attribute("src"))
        # TODO fix 403
        print(img_src_list)


if __name__ == '__main__':
    main = Main(sys.argv[1], sys.argv[2], sys.argv[3])
    main.process()
