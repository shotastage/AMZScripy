import urllib.request
import sys


class Setup():

    def install_chromedriver(self):
        URL = "https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_mac64.zip"
        urllib.request.urlretrieve(URL, "{0}".format("chromedriver_mac64.zip"))
