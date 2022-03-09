from selenium import webdriver
import requests
import wget
import zipfile
import os


driver = webdriver.Chrome()
browser_version = driver.capabilities['browserVersion']
driver_version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
print("browser version",browser_version)
print("driver version",driver_version)

if browser_version[0:2] != driver_version[0:2]: 
    
    driver.close()
    driver.quit()

    os.remove(r'chromedriver.exe')
  
    # get the latest chrome driver version number
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    # build the donwload url
    download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

    # download the zip file using the url built above
    latest_driver_zip = wget.download(download_url,'chromedriver.zip')
    # extract the zip file
    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall() # you can specify the destination folder path here
    # delete the zip file downloaded above
    os.remove(latest_driver_zip)

else:
    print("rock and roll your are good to go")