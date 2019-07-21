from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverUtils(object):
    def __init__(self, driver):
        self.driver = driver

    def focus_frame(self, explicit_wait_time, element):
        WebDriverWait(self.driver, explicit_wait_time).until(EC.frame_to_be_available_and_switch_to_it(element))
