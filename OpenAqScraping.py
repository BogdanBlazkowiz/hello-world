from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Firefox()


def get_ammount_country(url, what_to_find):
    dictionary = {}
    for f in range(15):
        driver.get(url)
        time.sleep(4)
        click_place = driver.find_elements_by_class_name("cfa-go")
        print(len(click_place), f)
        click_place[f].click()
        time.sleep(7)
        try:
            html = driver.find_element_by_tag_name('html')\
                        .get_attribute('innerHTML')
            soup = BeautifulSoup(html, 'html.parser')
            O3 = soup.find("dt", text=what_to_find).next_sibling
            lol = driver.find_element_by_class_name("inpage__title").text
            country = lol[lol.find(",")+2:]
            quantity = O3.get_text()
            if "ppm" in quantity:
                quantity = int(quantity[:quantity.find("p")]) / 0.000467
            else:
                quantity = int(quantity[:quantity.find("µ")])
        except:
            continue
        if country:
            try:
                dictionary[country].append(quantity)
            except:
                dictionary[country] = [quantity]
        print(dictionary)
    return dictionary


print(get_ammount_country("https://openaq.org/#/locations?page=1&parameters=o3&\
        _k=fabcaf", "O3"))
