import time
import pytest
from appium import webdriver


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "Android",
            "deviceName": "oneplus",
            "app": r"C:\App\org_coursera_android_v4.3.0.apk",
            # "appPackage": "com.tutorialspoint.onlineviewer",
            # "appActivity": "com.tutorialspoint.flutter_tutorialspoint.MainActivity"

        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


