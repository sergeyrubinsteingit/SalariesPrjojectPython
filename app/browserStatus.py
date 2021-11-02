class BrowserStatus:
    from selenium import webdriver
    from selenium.webdriver.chrome.webdriver import WebDriver
    import os

    wbd_: WebDriver

    # os.chdir('../drivers')
    # abs_path_driver_ = os.path.abspath('chromedriver.exe')
    # wbd_ = webdriver.Chrome(abs_path_driver_)

    drv_path_ = 'C:/Users/user/PycharmProjects/SalariesPrjPython/drivers/chromedriver.exe'
    drv_path_ = drv_path_.replace('/', os.path.sep)

    # wbd_ = webdriver.Chrome('C:/Users/user/PycharmProjects/SalariesPrjPython/drivers/chromedriver.exe')
    wbd_ = webdriver.Chrome(drv_path_)
    get_url_: str = "https://www.techjob.co.il/salary-survey"
