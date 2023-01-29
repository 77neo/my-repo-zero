from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches", ["enable-automation"])

options.add_experimental_option('useAutomationExtension', False)

options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument('--enable-popup-blocking')

options.add_argument("user-data-dir=C:\\Users\\srcgo\\Desktop\\0\\selenium") 

driver = webdriver.Chrome(options=options)
driver.get("https://www.tiktok.com")
sleep(5)
driver.find_element(By.CLASS_NAME, "tiktok-y3rt08-SpanUploadText e18d3d945").click()
# jsx-2404389384 upload
# jsx-2404389384 
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

drag_and_drop_file(driver.find_element(By.CLASS_NAME, "jsx-2404389384"), 'C:\\Users\\srcgo\\Desktop\\0\\video.mp4')
sleep(7)