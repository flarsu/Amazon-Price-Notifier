from bs4 import BeautifulSoup
import requests
import smtplib


def scrape():
        lapi = 'https://www.amazon.in/UX333FA-A4116T-13-3-inch-i7-8565U-Integrated-Graphics/dp/B07MLVQDF2/ref=sr_1_1?keywords=asus+zenbook+13&qid=1577877964&sr=8-1'

        header = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }

        response = requests.get(lapi , headers=header)

        content = BeautifulSoup(response.content, 'html.parser')

        name = content.find(id="productTitle").get_text()

        price = content.find(id="priceblock_ourprice").get_text()
        
        char =[","]
        for i in char:
           price= price.replace(i,'')
        print(price[2:])    
        new_price = float(price[2:])

        if(new_price > 75000):
            notify()

def notify():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('from_emailid','password')##for password you need to complete the two step verification with your google account and need to get a app password for your windows computer(if error comes click on the link given in error) 

    subject = 'time to buy your new Laptop'

    body = 'GO to the link https://www.amazon.in/UX333FA-A4116T-13-3-inch-i7-8565U-Integrated-Graphics/dp/B07MLVQDF2/ref=sr_1_1?keywords=asus+zenbook+13&qid=1577877964&sr=8-1'

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail('from_emailid','to_emailid',message)

    print('Mail sent')

    server.quit()


scrape()
