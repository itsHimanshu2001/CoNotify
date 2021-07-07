from plyer import notification
import requests
from bs4 import BeautifulSoup
import json
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r'D:\records\Desktop Notifier\icon_new.ico',
        timeout = 10
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    # notifyMe('me','hello')
    myHtmlData = getData('https://prsindia.org/covid-19/cases')
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())

    myData = []
    cnt = 0
    
    for tr in soup.find_all('tbody')[0].find_all('td'):
        
        myData.append(tr.get_text().split('\n\n'))
    finalData = []
    cnt = 1
    for x in range(len(myData)):
        if(myData[x][0] == str(cnt)):
            x+=1
            cnt+=1
            l = []
            while(myData[x][0] != str(cnt)):
                l.append(myData[x][0])
                x+=1
                
            finalData.append(l)
            cnt+=1
    # print(finalData)     #finalData stores the complete states covid-19 data
         
    states = ['Delhi', 'Maharashtra', 'Uttarakhand']
    for item in finalData:
        # dataList = item.split('\n')
        if item[0] in states:
            print(item)
            nTitle = 'Covid-19 Update'
            nText = f"State : {item[0]}\nConfirmed Cases : {item[1]}\nActive Cases : {item[2]}\nRecovered : {item[3]}\nDeath : {item[4]}"
            notifyMe(nTitle,nText)
            time.sleep(2)










    