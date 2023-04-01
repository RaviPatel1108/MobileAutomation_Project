from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that
from base.appium_listener import AppiumConfig


class TestAndroidDeviceLocal(AppiumConfig):

    def test_invalid_signin_process(self):
        self.driver.find_element(AppiumBy.ID, "org.coursera.android:id/login").click()
        self.driver.find_element(AppiumBy.ID, "org.coursera.android:id/email").send_keys("RaviPatel@123.com")
        self.driver.find_element(AppiumBy.ID, "org.coursera.android:id/password").send_keys("Ravi123")
        self.driver.find_element(AppiumBy.ID, "org.coursera.android:id/create_account").click()
        error_message = self.driver.find_element(AppiumBy.ID, "android:id/message").text
        assert_that(error_message).is_equal_to("There was an error logging in, please try again.")
        self.driver.find_element(AppiumBy.ID, "android:id/button3").click()
