from otp import get_otp


class AMZLogin():

    def __init__(self, amz, email, passwd):
        self.driver = amz.driver
        self._email = email
        self._passwd = passwd

    def login(self):

        href = self.driver.find_element_by_id('nav-link-accountList').get_attribute("href")
        self.driver.get(href)
        self.driver.find_element_by_id('ap_email').send_keys(self._email)
        self.driver.find_element_by_id('ap_password').send_keys(self._passwd)
        self.driver.find_element_by_id('signInSubmit').click()


        while True:
            if self._check_captcha() != True:
                break

        otp = get_otp()

        self.driver.find_element_by_id('auth-mfa-otpcode').send_keys(otp)
        self.driver.find_element_by_id('auth-signin-button').click()


    def _check_captcha(self) -> bool:
        try:
            self.driver.find_element_by_id('auth-captcha-image').click()

            #
            self.driver.find_element_by_id('ap_email').clear()
            self.driver.find_element_by_id('ap_email').send_keys(self._email)
            self.driver.find_element_by_id('ap_password').send_keys(self._passwd)
            captcha = input("キャプチャを入力したらyを押してください: ")
            #self.driver.find_element_by_id('auth-captcha-guess').send_keys(captcha)
            self.driver.find_element_by_id('signInSubmit').click()

            return True
        except:
            return False
