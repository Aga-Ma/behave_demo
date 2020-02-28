from selenium import webdriver


def before_scenario(context, scenario):
    # Initialize ChromeDriver
    context.driver = webdriver.Chrome("C:/drivers/chromedriver.exe")
    # Wait implicitly for elements to be ready before attempting interactions
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    context.driver.quit()


