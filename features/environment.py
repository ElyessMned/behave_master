from selenium import webdriver

from pages.draganddrop import draganddrop


def before_scenario(context,scenario):
    context.browser = webdriver.Chrome(executable_path=r"C:\webdriver\chromedriver_win32_93\chromedriver.exe")
    browser = context.browser
    context.browser.maximize_window()
    context.dd = draganddrop(context.browser)

def after_scenario(context,scenario):
    context.browser.quit()