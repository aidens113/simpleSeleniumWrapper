from .baseImports import *

#@for_all_methods(stop_driver_on_error)
class ElementLocation:
    def __init__(self,elementSelectorRootObj,WebElement):
        #Set element selector root (driver or webelem)
        self.elementSelectorRootObj=elementSelectorRootObj
        self.WebElement=WebElement

        #Set driver
        if "WebDriver" in str(type(elementSelectorRootObj)):
            self.driver=elementSelectorRootObj
        else:
            self.driver=elementSelectorRootObj.parent

    def find_elem_or_elems_main(self,method,selector,multiple_elements):
        try:
            if multiple_elements==False:
                return self.WebElement(self.elementSelectorRootObj.find_element(method,selector))
            else:
                allElemsFound=self.elementSelectorRootObj.find_elements(method,selector)
                allWrappedWebElems=[]
                for webElem in allElemsFound:
                    allWrappedWebElems.append(self.WebElement(webElem))
                return allWrappedWebElems
        except Exception as err:
            logging.error(err)
            return False
    
    def find_elem_or_elems(self,method,selector,multiple_elements,retry_if_fail,max_retries,delay_for_each_retry):
        if retry_if_fail==True:
            for _ in range(max_retries):
                result=self.find_elem_or_elems_main(method,selector,multiple_elements)
                if multiple_elements==False:
                    if result!=False:
                        return result
                else:
                    if result!=False and len(result)>0:
                        return result
                time.sleep(delay_for_each_retry)
        else:
            return self.find_elem_or_elems_main(method,selector,multiple_elements)
        return False

    def find_elems_by_js_script(self,scriptToExecute,multiple_elements,retry_if_fail,max_retries,delay_for_each_retry):
        #Retry if user selected it
        try:
            if retry_if_fail==True:
                for _ in range(max_retries):
                    try:
                        result=self.driver.execute_script(scriptToExecute)
                        if multiple_elements==False:
                            if result!=False:
                                return self.WebElement(result[0])
                        else:
                            if result!=False and len(result)>0:
                                theseResults=[]
                                for webElem in result:
                                    theseResults.append(self.WebElement(webElem))
                                return theseResults
                    except Exception as err:
                        print(err)
                        pass
                    time.sleep(delay_for_each_retry)
            else:
                result=self.driver.execute_script(scriptToExecute)
                if multiple_elements==False:
                    if result!=False:
                        return self.WebElement(result[0])
                else:
                    if result!=False and len(result)>0:
                        theseResults=[]
                        for webElem in result:
                            theseResults.append(self.WebElement(webElem))
                        return theseResults
                
        except Exception as err:
            logging.error(err)
        return False
            
    def by_id(self,element_id,retry_if_fail=True,max_retries=5,delay_for_each_retry=1):
        return self.find_elem_or_elems(By.ID,element_id,False,retry_if_fail,max_retries,delay_for_each_retry)

    def by_name(self,element_name,retry_if_fail=True,max_retries=5,delay_for_each_retry=1):
        return self.find_elem_or_elems(By.NAME,element_name,False,retry_if_fail,max_retries,delay_for_each_retry)

    def by_xpath(self,element_xpath,multiple_elements=False,retry_if_fail=True,max_retries=5,delay_for_each_retry=1):
        return self.find_elem_or_elems(By.XPATH,element_xpath,multiple_elements,retry_if_fail,max_retries,delay_for_each_retry)

    def by_tag(self,element_tag_name,multiple_elements=False,retry_if_fail=True,max_retries=5,delay_for_each_retry=1):
        return self.find_elem_or_elems(By.TAG_NAME,element_tag_name,multiple_elements,retry_if_fail,max_retries,delay_for_each_retry)

    def by_class(self,element_class_name,multiple_elements=False,retry_if_fail=True,max_retries=5,delay_for_each_retry=1):
        return self.find_elem_or_elems(By.CLASS_NAME,element_class_name,multiple_elements,retry_if_fail,max_retries,delay_for_each_retry)

    def by_selector(self,element_css_selector,multiple_elements=False,retry_if_fail=True,max_retries=5,delay_for_each_retry=1):
        return self.find_elem_or_elems(By.CSS_SELECTOR,element_css_selector,multiple_elements,retry_if_fail,max_retries,delay_for_each_retry)

    def by_attr(self,attribute_key,attribute_value,multiple_elements=False,retry_if_fail=True,max_retries=5,delay_for_each_retry=1):
        #Make script string to execute
        scriptToExecute=f"""return self.document.querySelectorAll('[{attribute_key}="{attribute_value}"]');"""

        #Execute script & get results
        return self.find_elems_by_js_script(scriptToExecute,multiple_elements,retry_if_fail,max_retries,delay_for_each_retry)
        

    def by_text(self,text,multiple_elements=False,retry_if_fail=True,max_retries=5,delay_for_each_retry=1):
        return self.find_elem_or_elems(By.XPATH,f"//*[text()='{text}']",multiple_elements,retry_if_fail,max_retries,delay_for_each_retry)
        
