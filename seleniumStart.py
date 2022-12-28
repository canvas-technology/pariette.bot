from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from main import sendData as getData
from main import sendDataToApi as sdta

class SeleniumStarter:

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    def __init__(self):
        self.datas = getData()
        self.starter()

    def starter(self):
        for self.data in self.datas:
            try:
                self.dataType = By.CLASS_NAME
                if self.data[1].split(",")[2] == "ID":
                    self.dataType = By.ID
                self.driver.get(self.data[0].split(",")[2])
                self.driver.implicitly_wait(15)
                self.siteName = self.data[1].split(",")[0]

                if self.siteName == "parkmatik":
                    self.price = self.driver.find_element(self.dataType, self.data[1].split(",")[3]).text
                    if "." in self.price:
                        self.price = self.price.replace(".","").replace(",",".").strip()
                    else:
                        self.price = self.price.replace(",",".").strip()
                if self.siteName == "otomatikkapiniz":
                    self.price = (self.driver.find_elements(self.dataType, self.data[1].split(",")[3]))[10].text
                    if self.price.count("₺") > 1:
                        self.price = self.price.split("₺")[2].replace(".","").replace(",",".").strip()
                    else:
                        self.price = self.price.replace(".","").replace(",",".").strip()
                if self.siteName == "bft-kapi":
                    self.price = (self.driver.find_elements(self.dataType, self.data[1].split(",")[3]))[0].text
                    if self.price.count("₺") > 1:
                        self.price = self.price.split("₺")[2].replace(",","").strip()
                    else:
                        self.price = self.price.replace(",","").strip()
                if self.siteName == "motodoor":
                    self.price = (self.driver.find_elements(self.dataType, self.data[1].split(",")[3]))[0].text 
                    if self.price.count("TL") > 1:
                        self.price = self.price.split("TL")[1].replace("\n","").replace(".","").replace(",",".").strip()
                    else:
                        self.price = self.price[0].replace(".","").replace(",",".").strip()
                if self.siteName == "ases":
                    self.price = (self.driver.find_elements(self.dataType, self.data[1].split(",")[3]))[0].text
                    self.price = self.price.split("KDV Dahil")[1].split("₺")[0].replace(".","").replace(",",".").strip()
                if self.siteName == "hdtotomatikkapi":
                    self.price = (self.driver.find_elements(By.CSS_SELECTOR, '[itemprop="offers"]'))[0].text 
                    if self.price.count("₺") > 1:
                        self.price = self.price.split("₺")[2].replace(".","").replace(",",".").strip()
                    else:
                        self.price = self.price.split("₺")[1].replace(".","").replace(",",".").strip()
                if self.siteName == "gulerguvenlik":
                    self.price = self.driver.find_element(self.dataType, self.data[1].split(",")[3]).text.replace(".","").replace(",",".").replace("TL","").strip()
                if self.siteName == "kapimotoru":
                    self.price = self.driver.find_elements(self.dataType, self.data[1].split(",")[3])[0].text.replace("TL","").replace(".","").replace(",",".").strip()
                if self.siteName == "asroyal":
                    self.price = self.driver.find_elements(self.dataType, self.data[1].split(",")[3])[0].text.split(" ")[0].replace(".","").replace(",",".").strip()
                if self.siteName == "nota.ist":
                    self.price = self.driver.find_elements(self.dataType, self.data[1].split(",")[3])[16].text.split(" ")[0].replace(".","").replace(",",".").strip()
                if self.siteName == "uzmankapi":
                    self.price = self.driver.find_elements(self.dataType, self.data[1].split(",")[3])[0].text.split(" ")[0].replace(".","").replace(",",".").strip()
                sdta(self.data[0].split(",")[0],int(self.data[0].split(",")[1]),float(self.price))
            except:
                sdta(self.data[0].split(",")[0],int(self.data[0].split(",")[1]),0,2)

SeleniumStarter()