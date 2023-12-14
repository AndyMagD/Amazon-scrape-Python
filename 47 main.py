import requests
import smtplib
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

#setup
r = requests.get(url, header)
soup = BeautifulSoup(r.content, "lxml")
#print(soup.prettify())

#Scraping for price
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

def sendmail():
    MY_MAIL = "test@gmail.com"
    PYTHON_PSW = "*******"
    subject = "Instant Pot Duo Plus Price drop"
    if price_as_float < 80.0:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=PYTHON_PSW)
            connection.sendmail(
                from_addr=MY_MAIL,
                to_addrs="test@hotmail.com",
                msg=f"{subject}\n\n Instant Pot Duo Plus price has dropped to {[price_as_float]}."
            )
            print("mail sent")

sendmail()
