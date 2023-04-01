import pytest
from appium import webdriver
from utilities import read_utils


class AppiumConfig:

    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        json_dic = read_utils.get_dic_from_json("../testdata/config.json")

        if json_dic["device"] == "local":
            des_cap = {
                "platformName": "Android",
                "deviceName": "oneplus",
                "app": r"C:\App\org_coursera_android_v4.3.0.apk",
                # "noReset": True,
            }
        else:
            des_cap = {
                "app": "bs://6f1fd39e5beae18971921e3f06ddd40bac1ee9ba",
                "platformVersion": "9.0",
                "deviceName": "Google Pixel 3",
                "bstack:options": {
                    "projectName": "First Behave Android Project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    # Set your access credentials
                    "userName": "ravipatel_ImV4Bk",
                    "accessKey": "e5wyS7fEvx44kHQxJus3"
                }
            }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()
