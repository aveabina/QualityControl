import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/User/Downloads/chromedriver') 
driver.get('https://www.housebrand.com/ru/ru/') 

#принятие cookies
cook_button = driver.find_element(By.XPATH, '//*[@id="onetrust-button-group"]/div')
cook_button.click()

# TК-001	Поиск по сайту по определенному запросу
search_box = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[2]/div[1]')
search_box.send_keys('Рюкзак')
time.sleep(1)
search_button = driver.find_element(By.XPATH, '//*[@id="search_icon_button"]')
search_button.click()
answer = driver.find_element(By.XPATH, '//*[@id="title"]/h1/span[2]')
if answer.text != u'рюкзак':
    print(datetime.datetime.now(), "TК-001: Ожидаемый ответ верен =  %r" % answer.text)
else:
    print("Ожидаемый ответ ", answer.text, " не найден")
time.sleep(2)

# TК-002	Установка фильтров и их отображение
sort_button = driver.find_element(By.XPATH, '//*[@id="filtersBtn"]')
time.sleep(1)
sort_button.click()
time.sleep(1)
type_sort = driver.find_element(By.XPATH, '//*[@id="order"]/ul/li[2]')
type_sort.click()
time.sleep(1)
res_button = driver.find_element(By.XPATH, '//*[@id="stickyMenu"]/div[2]/div/div/button')
res_button.click()
print(datetime.datetime.now(), 'TК-002: Сортировка прошла успешно')

# TК-003	Добавление отфильтрованного товара в Избранное
fav = driver.find_element(By.XPATH, '//*[@id="product-key-id-17065770"]/div/div[1]')
fav.click()
print(datetime.datetime.now(), 'TК-003: Товар добавлен в "Избранное"')
time.sleep(1)

# TК-004	Добавление товара в корзину
sell_box = driver.find_element(By.XPATH, '//*[@id="product-key-id-17065770"]/a/div[2]/button')
sell_box.click()
time.sleep(0.5)
print(datetime.datetime.now(), 'TК-004: Товар успешно добавлен в корзину')

# ТК-005 Удаление товара из корзины
to_sell = driver.find_element(By.XPATH, '//*[@id="bolsa_any"]')
to_sell.click()
time.sleep(0.5)

del_button = driver.find_element(By.XPATH, '//*[@id="pageBagItems"]/div[2]/div/ul/li/button')
del_button.click()
time.sleep(0.5)
print(datetime.datetime.now(), 'TК-005: Товар успешно удален из корзины')

# TК-006	Переход в социальную сеть Pinterest из футтера сайта по кнопке

pinterest_button = driver.find_element(By.XPATH, '//*[@id="nav-socialnetwork"]/span[5]/span/a')
pinterest_button.click()
print(datetime.datetime.now(), 'TК-006: Переход по кнопке выполнен успешно')
time.sleep(5)

driver.quit()
