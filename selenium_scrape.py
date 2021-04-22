from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

from time import sleep


options = Options()
options.headless = True
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.panel.shown", False)
fp.set_preference("browser.download.useDownloadDir", True)
fp.set_preference("browser.download.dir", ".")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

# need to install geckodriver if not already present
driver = webdriver.Firefox(firefox_profile=fp, options=options, executable_path='/Users/wimlds/Applications/geckodriver')

# list of tweet urls
for url in urls:
    print(url)
    driver.get(url)
    # this is important, otherwise results are going to be random
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    cards = driver.find_elements_by_xpath('//div[@data-testid="tweetPhoto"]')
    try:
        for card in cards:
            imgs = card.find_elements_by_xpath('.//img')
            for img in imgs:
                imgUrl = img.get_attribute('src')
                print(imgUrl)
                    
                imgName = re.sub(pattern, flNmGrp, imgUrl)
                response = requests.get(imgUrl, stream=True)
                with open(os.path.join("/Users/wimlds/twitter/imgfolder", imgName), 'wb') as f:
                        f.write(response.content)
                del response
        print("Done!")
    except Exception as e:
        print("Failed getting image for: " + url + e.message)
    
