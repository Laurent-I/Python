from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com')

assert 'Learn Selenium with Best Practices and Examples | Selenium Easy' in chrome_browser.title
content = chrome_browser.find_element_by_class_name('content')
print(content)

