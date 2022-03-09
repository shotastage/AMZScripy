import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from AMZ import AMZ
from AMZData import AMZData
from AMZLogin import AMZLogin

from df import DataFrame


if __name__ == "__main__":

    # Amazon Handler Instance
    amz = AMZ()

    # Amazon Login
    login = AMZLogin(amz, os.environ['AMZ_LOGIN_EMAIL'], os.environ['AMZ_LOGIN_PASSWD'])
    login.login()


    # Main
    amz.search("ワイヤレス充電器")


    # Fetch Data
    amz_data = AMZData(amz)


    while amz.next_page():
        amz_data.update()

    # Save Data
    df = DataFrame()
    df.add_col("商品名", amz_data.get_product_names())
    df.add_col("値段", amz_data.get_prices())

    df.save_excel("test.xlsx")

    amz.complete()
