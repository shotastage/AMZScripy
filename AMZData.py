
class AMZData():

    def __init__(self, amz):
        self.driver = amz.driver
        self._products = []
        self._prices = []

    def update(self):
        self._price_update()
        self._product_names_update()

    def _product_names_update(self):

        elms = self.driver.find_elements_by_css_selector('.a-size-base-plus.a-color-base.a-text-normal')

        for elm in elms:
            self._products.append(elm.text)

    def _price_update(self):

        elms = self.driver.find_elements_by_class_name('a-price-whole')

        for elm in elms:
            self._prices.append(elm.text.replace(',', ''))


    def get_product_names(self) -> list:

        return self._products

    def get_prices(self) -> list:

        return self._prices
