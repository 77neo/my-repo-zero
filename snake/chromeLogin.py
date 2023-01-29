from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches", ["enable-automation"])

options.add_experimental_option('useAutomationExtension', False)

options.add_argument('--disable-blink-features=AutomationControlled')

options.add_argument("user-data-dir=C:\\Users\\srcgo\\Desktop\\0\\selenium") 

driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com")
sleep(5)
b = driver.find_element(By.CLASS_NAME, "style-scope ytd-topbar-menu-button-renderer")
b.click()
sleep(3)
b = driver.find_element(By.CLASS_NAME, "style-scope ytd-compact-link-renderer")
b.click()
sleep(5)
JS_DROP_FILE = """
    var target = arguments[0],
        offsetX = arguments[1],
        offsetY = arguments[2],
        document = target.ownerDocument || document,
        window = document.defaultView || window;

    var input = document.createElement('INPUT');
    input.type = 'file';
    input.onchange = function () {
      var rect = target.getBoundingClientRect(),
          x = rect.left + (offsetX || (rect.width >> 1)),
          y = rect.top + (offsetY || (rect.height >> 1)),
          dataTransfer = { files: this.files };

      ['dragenter', 'dragover', 'drop'].forEach(function (name) {
        var evt = document.createEvent('MouseEvent');
        evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
        evt.dataTransfer = dataTransfer;
        target.dispatchEvent(evt);
      });

      setTimeout(function () { document.body.removeChild(input); }, 25);
    };
    document.body.appendChild(input);
    return input;
"""

def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
    file_input.send_keys(path)

driver.get_screenshot_as_file("screenshot.png")
drag_and_drop_file(driver.find_element(By.ID, "content"), 'C:\\Users\\srcgo\\Desktop\\0\\video.mp4')
sleep(3)

title = driver.find_element(By.ID, "title-textarea")
title.send_keys('philosophy #fiii ')
sleep(8)
driver.find_element(By.ID, "step-badge-3").click()
sleep(5)
driver.find_element(By.ID, "done-button").click()


sleep(5)
