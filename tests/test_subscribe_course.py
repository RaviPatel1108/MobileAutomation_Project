from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that
from base.appium_listener import AppiumConfig


class TestAndroidDeviceLocal(AppiumConfig):
    def test_subscribe_python_basic(self):
        self.driver.find_element(AppiumBy.ID, "org.coursera.android:id/close_button").click()
        if self.driver.find_element(AppiumBy.ID, "org.coursera.android:id/search_src_text").is_displayed():
            self.driver.find_element(AppiumBy.ID, "org.coursera.android:id/search_src_text").send_keys("Python").click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="python, , item 1 of 20"]').click()
        size_dic = self.driver.get_window_size()
        x1 = size_dic['width'] * (50 / 100)
        y1 = size_dic['height'] * (75 / 100)

        x2 = size_dic['width'] * (50 / 100)
        y2 = size_dic['height'] * (25 / 100)

        # xpath = "//android.widget.TextView[contains(@text,'Python Basics for Online Research')]"
        ui_automator_path = 'UiSelector().text("Python Basics for Online Research")'

        self.driver.implicitly_wait(0)
        while len(self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, ui_automator_path)) == 0:
            self.driver.swipe(x1, y1, x2, y2, 1000)

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ui_automator_path).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.ID, "org.coursera.android:id/enroll_text").click()

