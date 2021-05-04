from selenium import webdriver


def config_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-web-security')
    options.add_argument('--window-size=1920,1080')  
    options.add_argument('headless')
    return options