from .baseImports import *
from .elementLocation import ElementLocation

#@for_all_methods(stop_driver_on_error)
class WebElement(ElementLocation):
    def __init__(self,webElement):
        #Set webelem
        self.webElement=webElement

        #Set driver
        self.driver=webElement.parent

        #Init ElementLocation class
        super().__init__(webElement,WebElement)

        #Set basic selenium webelement attributes
        self.accessible_name=webElement.accessible_name
        self.aria_role=webElement.aria_role
        self.id=webElement.id
        self.parent=webElement.parent


    #------------------WRAPPED ATTRIBUTES--------------------
    def location(self):
        return self.webElement.location

    def location_once_scrolled_into_view(self):
        return self.webElement.location_once_scrolled_into_view

    def rect(self):
        return self.webElement.rect

    def size(self):
        return self.webElement.size

    def text(self):
        return self.webElement.text

    def innerHTML(self):
        return self.webElement.get_attribute('innerHTML')
        

    #------------------BASIC SELENIUM WEBELEMENT FUNCTIONS-------------------
    def clear(self):
        return self.webElement.clear()

    def click(self,use_javascript=False):
        if use_javascript==False:
            try:
                return self.webElement.click()
            except:
                #Do js version if normal version fails
                return self.driver.execute_script("arguments[0].click();",self.webElement)
        else:
            return self.driver.execute_script("arguments[0].click();",self.webElement)

    def screenshot(self,filename):
        return self.webElement.screenshot(filename)

    def screenshot_as_base64(self):
        return self.webElement.screenshot_as_base64

    def screenshot_as_png(self):
        return self.webElement.screenshot_as_png

    def submit(self):
        return self.webElement.submit()

    def displayed(self):
        return self.webElement.is_displayed()

    def enabled(self):
        return self.webElement.is_enabled()

    def selected(self):
        return self.webElement.is_selected()

    def dom_attr(self,dom_attr):
        return self.webElement.get_dom_attribute(dom_attr)

    def property(self,this_property):
        return self.webElement.get_property(this_property)

    def css_property(self,property_name):
        return self.webElement.value_of_css_property(property_name)

    #------------------CUSTOM SIMPLE SIMPLE SELENIUM FUNCTIONS--------------------
    def attr(self,attr):
        return self.webElement.get_attribute(attr)

    def all_attributes(self):
        return self.driver.execute_script('var finalAttrs={};var attrNames=arguments[0].getAttributeNames();for(var vv=0;vv<attrNames.length;vv++){var attrNameHere=attrNames[vv];finalAttrs[attrNameHere]=arguments[0].getAttribute(attrNameHere);}return finalAttrs;',self.webElement)

    def parent(self):
        return WebElement(self.driver.execute_script('return arguments[0].parentElement;',self.webElement))

    #------------------CUSTOM COMPLEX SIMPLE SELENIUM FUNCTIONS--------------------
    def write(self,string_to_type,use_random_delay=True,min_delay=0.1,max_delay=0.3):
        if use_random_delay==True:
            for letter in string_to_type:
                self.webElement.send_keys(letter)
                time.sleep(random.uniform(min_delay,max_delay))
        else:
            self.webElement.send_keys(string_to_type)




    
