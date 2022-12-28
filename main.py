from requests import get
from requests import post

typesOfData = {"parkmatik":"ID",
               "otomatikkapiniz":"CLASS",
               "bft-kapi":"CLASS",
               "ases":"CLASS",
               "motodoor":"CLASS",
               "hdtotomatikkapi":"CLASS",
               "gulerguvenlik":"CLASS",
               "kapimotoru":"CLASS",
               "asroyal":"CLASS",
               "nota.ist":"CLASS",
               "uzmankapi":"CLASS"
}

dataOfWebsites = {"parkmatik":"satis",
                  "otomatikkapiniz":"price",
                  "bft-kapi":"price",
                  "ases":"urunDetayFiyatContainer",
                  "motodoor":"product-price-item",
                  "hdtotomatikkapi":"price-large",
                  "gulerguvenlik":"urun_fiyati",
                  "kapimotoru":"updated-price",
                  "asroyal":"price-wrapper",
                  "nota.ist":"price-wrapper",
                  "uzmankapi":"price-wrapper"
}

URL = 'https://us-live.pariette.link/api/Products-compare-items'

HEADERS = {
    "CompanyToken": 'ptPSBmCI',
    "TeamToken": 'XN8ebtIj',
    "SiteToken": 'bGIAIJgV'
}

r = get(url=URL, headers=HEADERS)
data = r.json()
i = -1
dataTotal = list()
dataTotal2 = list()

for key,value in data.items():
    if type(value) != list:
        continue
    else:
        for _ in range(len(value)):
            try:
                i+=1
                for key, val in typesOfData.items():
                    if key in value[i]["target"].split("/")[2]: 
                        dataText = value[i]["product"]+","+str(value[i]["id"])+","+value[i]["target"]
                        dataTotal.append(dataText)
                        dataText = key+","+value[i]["title"]+","+typesOfData[key]+","+dataOfWebsites[key]
                        dataTotal2.append(dataText)
            except:
                continue

def sendData():
    return list(zip(dataTotal,dataTotal2))


def sendDataToApi(productString,itemID,priceFloat,status=1):
    bodyData = {
        "product":productString,
        "item":itemID,
        "price":priceFloat,
        "status": status
    }
    HEADERS2 = {
        "CompanyToken": 'ptPSBmCI',
        "TeamToken": 'XN8ebtIj',
        "SiteToken": 'bGIAIJgV'
    }
    URL2 = "https://us-live.pariette.link/api/Products-compare"
    sendResponse = post(url=URL2, headers=HEADERS2, data=bodyData) 
    statusForResponse = sendResponse.text
    print(statusForResponse)
