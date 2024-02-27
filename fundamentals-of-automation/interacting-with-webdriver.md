---
description: >-
  On this page you'll learn about all of the different methods that the Simple
  Selenium WebDriver class has to offer
---

# Interacting With WebDriver

### Introduction

The WebDriver class contains all of the Simple Selenium functionality wrapped into an easy-to-use class. On this page, you'll learn how to use the WebDriver class in your web-scraping & general automation projects.

### List of All Simple Selenium WebDriver Functions

#### Unwrap Driver

You can get the unwrapped Selenium webdriver object with:

```python
seleniumDriver=driver.driver #Returns unwrapped Selenium webdriver object
```

#### Close Driver

You can do a clean shutdown of the webdriver web browser with:

```python
driver.close() #Closes the webdriver & web browser cleanly
```

#### Close Active Tab

Close just the active tab:

```python
driver.close_active_tab() #Closes the current active tab or the entire web browser if only one tab is open
```

#### Visit a Web Page

Visiting a webpage:

```python
driver.visit("https://google.com") #Visits google.com

#Default options:
referrer=False #Whether webdriver should use a referrer before visiting the target page
use_random_delay=True #Delay between visiting referrer website & target website (if referrer!=False)
min_delay=3.0 #Minimum delay between visiting referrer website & target website (if referrer!=False)
max_delay=3.5 #Maximum delay between visiting referrer website & target website (if referrer!=False)

driver.visit("https://domain.com",referrer="https://google.com") #Visits google.com before domain.com, which sets the referrer as google.com
```

#### Focus Document

Focuses the main document:

```python
driver.focus_document() #Focuses the main top-level document
```

#### Focus IFrame

Focuses a target IFrame:

```python
iframeTest=driver.by_id("myTestIframe") #Get some iframe from the page
driver.focus_iframe(iframeTest) #Focuses the main top-level document
```

#### Focus Parent IFrame

Focuses the parent document/iframe:

```python
driver.focus_parent_iframe() #Focuses parent frame
```

#### Get Application Cache

Get application cache:

```python
driver.application_cache() #Returns the application cache
```

#### Get Browser Capabilities

Get browser capabilities:

```python
driver.capabilities() #Returns browser capabilities
```

#### Get Desired Browser Capabilities

Get desired browser capabilities:

```python
driver.desired_capabilities() #Returns desired browser capabilities
```

#### Get Page Source

Get the current active page's source code:

```python
driver.page_source() #Returns active page's source code
```

#### Get Browser Name

Gets the browser name:

```python
driver.name() #Returns browser name
```

#### Get Timeouts

Gets driver timeouts:

```python
driver.timeouts() #Returns timeouts
```

#### Get File Detector

Gets file detector:

```python
driver.file_detector() #Returns file detector
```

#### Get Virtual Auth ID

Gets virtual authenticator ID:

```python
driver.virtual_authenticator_id() #Returns virtual auth id
```

#### Get Window Handles

Gets active window handles:

```python
driver.window_handles() #Returns window handles
```

#### Get Device Orientation

Gets device orientation:

```python
driver.orientation() #Returns device orientation
```

#### Get Current Active Window Handle

Gets active window handle:

```python
driver.current_window_handle() #Returns active window handle
```

#### Get Web Page Title

Gets the title of the current active webpage:

```python
driver.title() #Returns webpage title
```

#### Get Mobile Object

Gets the driver's mobile object:

```python
driver.mobile() #Returns driver mobile obj
```

#### Get Log Types

Gets log types:

```python
driver.log_types() #Returns all log types
```

#### Get Current URL

Gets the current active page URL:

```python
driver.current_url() #Returns current active page URL
```

#### Get Base64 Screenshot

Gets a base64 encoded string of screenshot img file:

```python
driver.screenshot_base64() #Returns string with base64 encoded img file
```

#### Get PNG Screenshot

Gets a bytes encoded string of screenshot png file:

```python
driver.screenshot_png() #Returns string with bytes encoded png file
```

#### Save File Screenshot

Screenshots & saves as a file in target directory:

```python
driver.screenshot("imgs/test.png") #Saves screenshot file in target directory with target filename
```

#### Add Browser Cookie

Adds a cookie dict to browser:

```python
driver.add_cookie({"cookieKey":"cookieValue"}) #Adds cookie to browser
```

#### Add Credential

Adds authentication credentials:

```python
driver.add_credential(authenticationObj) #Injects credential to authenticator
```

#### Add Virtual Authenticator

Adds virtual authenticator:

```python
driver.add_virtual_authenticator(authenticationObj) #Injects credential to authenticator
```

#### Previous Page

Go back to previous page:

```python
driver.back() #Goes to the previous webpage
```

#### Delete All Cookies

Delete all browser cookies:

```python
driver.delete_all_cookies() #Deletes all cookies
```

#### Delete Cookie By Name

Delete browser cookie by name:

```python
driver.delete_cookie("cookieName") #Deletes cookie by name
```

#### Delete Downloadable Files

Delete downloadable files:

```python
driver.delete_downloadable_files() #Deletes downloadable files
```

#### Download File

Download file by file name & directory:

```python
driver.download_file() #Downloads file
```

#### Execute Async Script

Executes JS async script:

```python
driver.execute_async_script("async js script to execute") #Executes JS script async

testElem=driver.by_id("testElement")
driver.execute_async_script("testElem=arguments[0];console.log(testElem);",testElem,testElem2,etc) #Executes async script with webelement(s) 
```

#### Execute Script

Executes JS script:

```python
driver.execute_async_script("js script to execute") #Executes JS script 

testElem=driver.by_id("testElement")
testElem2=driver.by_id("testElement2")
driver.execute_async_script("testElem=arguments[0];console.log(testElem);",testElem,testElem2,etc) #Executes script with webelement(s) 
```

#### Forward Page

Go forward a page:

```python
driver.forward() #Goes forward one page
```

#### Full-Screen Window

Turn browser into full-screen mode:

```python
driver.fullscreen_window() #Turns browser to fullscreen mode
```

#### Get Cookie By Name

Get cookie by name:

```python
driver.get_cookie("cookieName") #Returns cookie by name
```

#### Get All Cookies

Get all cookies from browser:

```python
driver.get_cookies() #Returns all cookies
```

#### Get All Credentials

Get all credentials:

```python
driver.get_credentials() #Returns all credentials
```

#### Get Downloadable Files

Get downloadable file:

```python
driver.get_downloadable_files() #Returns downloadable files
```

#### Get Log By Type

Get log from storage by type:

```python
driver.get_log("logType") #Returns log 
```

#### Get Pinned Scripts

Get pinned scripts:

```python
driver.get_pinned_scripts() #Returns pinned scripts
```

#### Get Window Position

Get window position:

```python
driver.get_window_position() #Returns window position of active window handle

#Default options:
windowHandle="current"

driver.get_window_position(anotherWindowHandle) #Returns window position of another window handle
```

#### Get Window Rect

Gets window rect:

```python
driver.get_window_rect() #Returns window rect
```

#### Get Window Size

Gets window size:

```python
driver.get_window_size() #Returns window size of active window handle

#Default options:
windowHandle="current"

driver.get_window_size(anotherWindowHandle) #Returns window size of another window handle
```

#### Implicitly Wait

Wait for x seconds:

```python
driver.implicitly_wait(5) #Waits for 5 seconds
```

#### Maximize Window

Maximizes the browser window:

```python
driver.maximize_window() #Puts browser into maximized mode
```

#### Minimize Window

Minimizes the browser window:

```python
driver.minimize_window() #Puts browser into minimized mode
```

#### Pin Script

Pins a script:

```python
driver.pin_script("Script to pin") #Pins a script

#Default options:
script_key=None 
```

#### Print Page

Prints the page:

```python
driver.print_page() #Prints the page

#Default options:
print_options=None
```

#### Refresh Page

Refreshes the webpage:

```python
driver.refresh() #Refreshes the active webpage
```

#### Remove All Credentials

Removes all credentials:

```python
driver.remove_all_credentials() #Removes all credentials
```

#### Remove Credential

Removes credential by ID:

```python
driver.remove_credential("credentialID") #Removes credential by id
```

#### Remove Virtual Authenticator

Removes virtual authenticator:

```python
driver.remove_virtual_authenticator() #Removes virtual authenticator
```

#### Set Page Load Time

Sets max page load time in seconds:

```python
driver.set_page_load_timeout(5) #Sets the max page load timeout to 5 seconds
```

#### Set Script Load Time

Sets max script load time in seconds:

```python
driver.set_script_timeout(5) #Sets the max script load timeout to 5 seconds
```

#### Set User Verified

Sets user verified:

```python
driver.set_user_verified(True) #Sets whether the authenticator will simulate success or fail on user verification
```

#### Set Window Position

Sets window position in pixels:

```python
driver.set_window_position(0,0) #Puts top left corner of browser to top left corner of screen with active window handle

#Default options:
windowHandle="current"

driver.set_window_position(0,0,otherWindowHandle) #Puts top left corner of browser to top left corner of screen with any window handle
```

#### Set Window Size

Sets window size:

```python
driver.set_window_size(1920,1080) #Sets window size to 9020px * 1080px on current window handle

#Default options:
windowHandle="current" 

driver.set_window_size(1920,1080,otherWindowHandle) #Sets window size to 9020px * 1080px on other window handle
```

#### Start Client

Starts client:

```python
driver.start_client() #Starts client
```

#### Start Session

Starts session:

```python
driver.start_session(browserCapabilities) #Starts session with browser capabilities
```

#### Stop Client

Stops client:

```python
driver.stop_client() #Stops client
```

#### Unpin Script By Key

Unpins script key:

```python
driver.unpin("scriptKey") #Unpins script by key
```
