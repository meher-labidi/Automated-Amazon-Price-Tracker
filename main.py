import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = "your email"
MY_PASSWORD = "your password"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
url="https://www.amazon.com/ASUS-ROG-Three-Layer-Hot-Swappable-PBT/dp/B0CLF3WYGC/ref=sr_1_12_sspa?dib=eyJ2IjoiMSJ9.R8S3hPZYQHddcgNhieVzSjJ_5_HbLJNFvcpcNua-7vfEea-zzOw1gzo9EpkgszIPfrQDq95asjGVzM926c5ozz0LmlLWbx_Qt0BU0OW3HqablmyrqpF1Y07TW6Dx16PzTBfFdJ9ge6C94CdHXp-OXVwnD-ezuA8xDICnwtH0dWrWY899Ee5PbiMjAIdfE3_DKOP46eAdIiyMZKAZIBaOA76FbRcdvDut89ko9eRVhGE.taozhXVj7dfp3PlBLcyeFctvN-5YTEc1tsB_OYLFUTU&dib_tag=se&keywords=keyboard&qid=1724597500&sr=8-12-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&th=1"
response=requests.get(url, headers=header)

soup = BeautifulSoup(response.text, "lxml")
# print(soup.prettify())
prices = soup.find_all(name="span", class_="a-price-whole")
price = [price.getText() for price in prices]
price_as_float = float(price[1])
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 250

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price} "

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
