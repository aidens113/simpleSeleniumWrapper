from .baseImports import *
from selenium.webdriver.common.alert import Alert

#@for_all_methods(stop_driver_on_error)
class Alerts:
    def __init__(self,driver):
        self.driver=driver
        self.alert=Alert(driver)

    def accept(self,retry_if_fail=True,max_retries=5,delay_for_each_retry=1):
        if retry_if_fail==True:
            for _ in range(max_retries):
                try:
                    return self.alert.accept()
                except:
                    pass
                time.sleep(delay_for_each_retry)
        else:
            return self.alert.accept()

    def dismiss(self,retry_if_fail=True,max_retries=5,delay_for_each_retry=1):
        if retry_if_fail==True:
            for _ in range(max_retries):
                try:
                    return self.alert.dismiss()
                except:
                    pass
                time.sleep(delay_for_each_retry)
        else:
            return self.alert.dismiss()

    def write(self,string_to_type):
        self.alert.send_keys(string_to_type)
