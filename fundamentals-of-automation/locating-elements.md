---
description: >-
  Learn all about how you can reliably locate elements on a webpage for
  automation/data scraping
---

# Locating Elements

### Introduction

On this page, you'll learn about all of the methods available for reliably locating elements on any webpage with Simple Selenium.

### List Of All Element Locators

#### By Element ID

Locate an element on a webpage by using the "id" attribute:

```python
my_element=driver.by_id("idValueOfElement") #Tries to locate element with id="idValueOfElement"
#Returns False if unable to find element

#Default options for by_id:
retry_if_fail=True #Whether or not driver should retry (max_retries) number of times before returning False
max_retries=5 #Max number of retries before returning False
delay_for_each_retry=1 #Delay in seconds between each attempt

#by_id with custom options
my_element=driver.by_id("idValueOfElement",retry_if_fail=False) #Stops driver from trying to locate element multiple times
```

#### By Element Name

Locate an element on a webpage by using the "name" attribute:

```python
my_element=driver.by_name("nameValueOfElement") #Tries to locate element with name="nameValueOfElement"
#Returns False if unable to find element

#Default options for by_name:
retry_if_fail=True #Whether or not driver should retry (max_retries) number of times before returning False
max_retries=5 #Max number of retries before returning False
delay_for_each_retry=1 #Delay in seconds between each attempt

#by_name with custom options
my_element=driver.by_name("nameValueOfElement",retry_if_fail=False) #Stops driver from trying to locate element multiple times
```

#### By Element XPath

Locate an element on a webpage by using an element's XPath:

```python
my_element=driver.by_xpath("/html/body/div/main/targetElement") #Tries to locate element by XPath
#Returns False if unable to find element

#Default options for by_xpath:
multiple_elements=False #Whether driver should return all elements found, or just the first one
retry_if_fail=True #Whether or not driver should retry (max_retries) number of times before returning False
max_retries=5 #Max number of retries before returning False
delay_for_each_retry=1 #Delay in seconds between each attempt

#by_xpath with custom options
my_element=driver.by_xpath("/html/body/div/main/targetElement",retry_if_fail=False) #Stops driver from trying to locate element multiple times
```

#### By Element Tag Name

Locate an element on a webpage by using an element's tag name:

```python
my_element=driver.by_tag("tagName") #Tries to locate element by element tag name (eg p, textarea, button, etc.)
#Returns False if unable to find element

#Default options for by_tag:
multiple_elements=False #Whether driver should return all elements found, or just the first one
retry_if_fail=True #Whether or not driver should retry (max_retries) number of times before returning False
max_retries=5 #Max number of retries before returning False
delay_for_each_retry=1 #Delay in seconds between each attempt

#by_tag with custom options
my_element=driver.by_tag("tagName",multiple_elements=True) #Finds & returns all elements that have the "tagName" tag name
```

#### By Element Class Name

Locate an element on a webpage by using an element's class name:

```python
my_element=driver.by_class("className") #Tries to locate element with class="className" attribute
#Returns False if unable to find element

#Default options for by_class:
multiple_elements=False #Whether driver should return all elements found, or just the first one
retry_if_fail=True #Whether or not driver should retry (max_retries) number of times before returning False
max_retries=5 #Max number of retries before returning False
delay_for_each_retry=1 #Delay in seconds between each attempt

#by_class with custom options
my_element=driver.by_class("className",multiple_elements=True) #Finds & returns all elements where class="className"
```

#### By Element Query Selector

Locate an element on a webpage by using an element's query selector:

```python
my_element=driver.by_selector("#__next > main > div:nth-child(1) > targetElement") #Tries to locate element with the target query selector
#Returns False if unable to find element

#Default options for by_selector:
multiple_elements=False #Whether driver should return all elements found, or just the first one
retry_if_fail=True #Whether or not driver should retry (max_retries) number of times before returning False
max_retries=5 #Max number of retries before returning False
delay_for_each_retry=1 #Delay in seconds between each attempt

#by_selector with custom options
my_element=driver.by_selector("#__next > main > div:nth-child(1) > targetElement",multiple_elements=True) #Finds & returns all elements where their query selector=the target selector
```

#### By Any Element Attribute

Locate an element on a webpage by using any one of an element's attributes:

```python
my_element=driver.by_attr("aria-label","targetAriaLabel") #Tries to locate element where aria-label="targetAriaLabel"
#Returns False if unable to find element

my_element=driver.by_attr("value","targetValue") #Tries to locate element where value="targetValue"
#Returns False if unable to find element

#Default options for by_attr:
multiple_elements=False #Whether driver should return all elements found, or just the first one
retry_if_fail=True #Whether or not driver should retry (max_retries) number of times before returning False
max_retries=5 #Max number of retries before returning False
delay_for_each_retry=1 #Delay in seconds between each attempt

#by_attr with custom options
my_element=driver.by_attr("aria-label","targetAriaLabel",multiple_elements=True) #Tries to locate all elements where aria-label="targetAriaLabel" 
```

#### By Element Text

Locate an element on a webpage by using an element's visible text:

```python
my_element=driver.by_text("Test Button") #Tries to locate element where the visible text="Test Button"
#Returns False if unable to find element

#Default options for by_text:
multiple_elements=False #Whether driver should return all elements found, or just the first one
retry_if_fail=True #Whether or not driver should retry (max_retries) number of times before returning False
max_retries=5 #Max number of retries before returning False
delay_for_each_retry=1 #Delay in seconds between each attempt

#by_text with custom options
my_element=driver.by_text("Test Button",multiple_elements=True) #Finds & returns all elements where their visible text="Test Button"
```
