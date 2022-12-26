import time

from appium import webdriver

driver = {
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:appPackage": "com.upax.zeusgeneric",
  "appium:appActivity": ".uimodules.splash.ZGSplashActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)
time.sleep(2)
driver.find_element("id", 'com.upax.zeusgeneric:id/zlo_button_guest').click()
time.sleep(2)
driver.find_element("xpath", '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText').send_keys("Alejandro Hernandez")
time.sleep(2)
driver.find_element("xpath", '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText').send_keys("alex.hdez0611")
time.sleep(2)
driver.find_element("xpath", '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.EditText').send_keys("2812847Wt%")
time.sleep(2)
driver.find_element("id", 'com.upax.zeusgeneric:id/zlo_button_login_guest').click()

