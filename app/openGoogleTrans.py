from app import clickOnLink
from app.browserStatus import BrowserStatus
import time
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import webbrowser as web_browser_

web_driver_ = BrowserStatus.wbd_


def open_google_trans():
    from app.clickOnLink import visit_links
    try:
        web_driver_.switch_to.window(web_driver_.window_handles[-1])
        time.sleep(2)
        # web_browser_.open_new("https://translate.google.co.il/?hl=en")
        web_driver_.execute_script('window.open("https://translate.google.co.il/?hl=en"), "_self"')
        # web_driver_.get("https://translate.google.co.il/?hl=en")
        time.sleep(0.2)

    except ((WebDriverException, NoSuchElementException)):
        web_driver_.quit()
        print(WebDriverException, NoSuchElementException)
