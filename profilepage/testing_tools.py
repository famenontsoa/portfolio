from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        # options.binary_location = "/usr/bin/google-chrome"
        service = Service(f"{settings.BASE_DIR}/chromedriver")
        cls.driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()
