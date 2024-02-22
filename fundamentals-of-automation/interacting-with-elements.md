---
description: >-
  On this page, you'll learn all about interacting with elements once you've
  located them
---

# Interacting With Elements

### Introduction

Once you've located elements, you'll most likely want to interact with them. On this page we'll cover all the ways you can interact with elements while using Simple Selenium.

### Unwrapping WebElement

You can get the unwrapped Selenium WebElement with:

```python
myElem=driver.by_tag('someTagName') #Gets some element on the page
baseSeleniumWebElement=myElem.webElement #Returns unwrapped Selenium web element
```

### Locating Child Elements

Let's say you've located an element on the page and want to find one of the element's child elements:

```python
#Page HTML looks like this:
#<div id="testElement"><p>text we want to grab</p></div>

testElement=driver.by_id("testElement") #Finds some element on the page
```

Simple Selenium web elements inherit all of the functions from [locating elements](https://tesseractcoder.gitbook.io/simple-selenium-wrapper-python/the-basics-of-automation/locating-elements) for finding child elements.

Grabbing the child element's text is simple:

```python
testElement.by_tag("p").text() #Returns "text we want to grab"
```

### Getting Element Attributes

Below are all of the methods for grabbing attributes of elements.

#### Get Any Attribute

Gets any attribute of element:

```python
#Page HTML looks like this:
#<div id="testElement" value="test">test</div>

testElement=driver.by_id("testElement") #Grab some element on the page
testElement.attr("value") #Returns "test"
```

#### Get All Attributes

Gets all attributes of element:

```python
#Page HTML looks like this:
#<div id="testElement" value="test">test</div>

testElement=driver.by_id("testElement") #Grab some element on the page
testElement.all_attributes() #Returns {"id":"testElement","value":"test"} 
```

#### Accessible Name

Gets aria level of element:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.accessible_name() #Returns aria level of element
```

#### Accessible Role

Gets aria role of element:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.aria_role() #Returns aria role of element
```

#### ID

Gets "id" attribute of element:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.id() #Returns id of element
```

#### Parent

Gets parent of element:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.parent() #Returns unwrapped Selenium webdriver
```

#### Tag Name

Gets tag name of element:

```python
#Page HTML looks like this:
#<div id="testElement">test</div>

testElement=driver.by_id("testElement") #Grab some element on the page
testElement.tag_name() #Returns "div"
```

#### Location

Get the location in pixels of an element:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.location() #Returns location in pixels of element on webpage
```

#### Location Once Scrolled Into View

Get the location in pixels of an element once it's scrolled into view:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.location_once_scrolled_into_view() #Returns location in pixels of element on webpage once it's scrolled into view
```

#### Rect

Gets the size & position of element in pixels:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.rect() #Returns size & location of element in pixels
```

#### Size

Gets the size of an element in pixels:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.size() #Returns size of element in pixels 
```

#### Text

Gets the current inner text of an element:

```python
#Given this HTML:
#<p id="testElement">test</p>

testElement=driver.by_id("testElement") #Grab some element on the page
testElement.text() #Returns "test" 
```

#### Inner HTML

Gets the current inner HTML of an element:

```python
#Given this HTML:
#<div id="testElement"><p>test</p></div>

testElement=driver.by_id("testElement") #Grab some element on the page
testElement.innerHTMl() #Returns "<p>test</p>" 
```

#### Is Displayed

Checks if element is displayed or not:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.displayed() #Returns True if element is displayed
```

#### Is Enabled

Checks if element is enabled or not:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.enabled() #Returns True if element is enabled
```

#### Is Selected

Checks if element is enabled or not:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.selected() #Returns True if element is selected
```

### List Of Methods

Below, are is a list of all methods available for interacting with web elements.

#### Clear

Clears the value of any input/textarea:

```python
#Given this HTML:
#<div id="testElement" value="test"><p>test</p></div>

testElement=driver.by_id("testElement") #Grab some element on the page
testElement.clear() #Clears value
testElement.attr("value") #Returns ""
```

#### Click

Clicks an element:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.click() #Clicks element

#Default options:
use_javascript=False #Whether Simple Selenium should use JS version of .click instead of built-in Selenium .click
#Notice: if .click with Selenium fails, Simple Selenium will attempt to use JS .click automatically

testElement.click(True) #Uses JS version of .click
```

#### Parent Element

Gets the current parent element of an element:

```python
#Given this HTML:
#<div id="testElementParent"><p id="testElement">test</p></div>

testElement=driver.by_id("testElement") #Grab some element on the page
testElement.parentElement().id() #Returns "testElementParent" 
```

#### Screenshot

Grabs a screenshot of the target element:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.screenshot("imgs/test.png") #Screenshots the element & saves it in path with file name 
```

#### Screenshot As Base64 String

Grabs a screenshot of the target element as a base64 string:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.screenshot_as_base64() #Returns a base64 encoded string with screenshot file data
```

#### Screenshot As PNG String

Grabs a screenshot of the target element as a .png encoded string:

```python
testElement=driver.by_id("testElement") #Grab some element on the page
testElement.screenshot_as_png() #Returns a png bytes encoded string with screenshot file data
```

#### Submit Form

Submits a form:

```python
testElement=driver.by_id("passwordElement") #Grab some input element on the page
testElement.submit() #Submits the form that input is attached to
```

#### Get DOM Attribute

Gets a DOM attribute of an element:

```python
testElement=driver.by_id("passwordElement") #Grab some input element on the page
testElement.dom_attr("attributeName") #Returns value of dom attribute
```

#### Get Property

Gets a property of an element:

```python
testElement=driver.by_id("passwordElement") #Grab some input element on the page
testElement.property("propertyName") #Returns value of property
```

#### Get CSS Property

Gets a CSS property of an element:

```python
testElement=driver.by_id("passwordElement") #Grab some input element on the page
testElement.css_property("CSSPropertyName") #Returns value of CSS property
```

#### Write

Send text input to any element like a human would:

```python
testElement=driver.by_id("passwordElement") #Grab some input element on the page
testElement.write("text to write") #Writes to element

#Default options:
use_random_delay=True #Whether or not to use a randomized delay between each keystroke
min_delay=0.1 #Minimum delay for randomized delay (if use_randomized_delay=True)
max_delay=0.3 #Maximum delay for randomized delay (if use_randomized_delay=True)

testElement.write("text to write",use_random_delay=False) #Writes to element instantly instead of with randomized delay
```
