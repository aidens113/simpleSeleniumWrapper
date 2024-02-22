---
description: >-
  On this page you'll learn about Action Chains, special keys, and special key
  combinations
---

# Action Chains & Special Keys

### Introduction

Selenium Action Chains allow you to simulate keyboard presses of any key on your keyboard, including "special keys" like ctrl, cmd, etc. Simple Selenium has an easy-to-use Action Chains class built into the WebDriver class, which you'll learn how to use on this page.

### Simple Selenium Action Chains

Using Simple Selenium Action Chains is easy, and similar to normal Selenium:

```python
#Start chrome webdriver with custom options
driver=SimpleSelenium("chrome",save_profile=True,profile_name="myAwesomeProfile",save_logs_in_file=True,maximized=True)

#Visit Google
driver.visit("https://google.com")

#Locate the main search bar
textArea=driver.by_tag("textarea")

#Use ActionChains to click the search bar
thisActionChain=driver.actionChains.click(textArea).press_key("t").press_key("e").press_key("s").press_key("t").press_key("enter")
thisActionChain.perform() #Executes all actions in the chain (click search bar, type "test", click enter). This is not the optimal way to type text in an input, but just an example for Action Chains
#You can add as many actions as you like onto an action chain, they get executed in order.
```

### Executing Special Key Commands (eg. ctrl-c, ctrl-v)

When building automation scripts, it's sometimes necessary to execute special key commands like ctrl-c, ctrl-v (cop & paste). In Simple Selenium, you can do this with:

```python
driver.special_key_combo(["ctrl","c"]) #Executes ctrl-c (copy clipboard)

driver.special_key_combo(["ctrl","v"]) #Executes ctrl-v (paste clipboard)
```

You can add as many keys as you would like to special\_key\_combo. Each key will be pressed one-by-one, then released one-by-one in order.

### List of Simple Selenium Action Chains Methods

Below, is a list of every Simple Selenium Action Chains method, with examples on how to use them.

#### Press Key

You can use press\_key to press & release any key on the keyboard. A list of all "special key" aliases can be found at the bottom of this page:

```python
#Presses & releases the enter key with Action Chains
chain=driver.actionChains.press_key("enter") #Create the action chain
chain.perform() #Execute action chain

#List of default options for this function:
use_random_delay=True #Whether there should be a randomized delay between key_down & key_up
min_delay=0.1 #Minimum delay (if use_random_delay=True)
max_delay=0.3 #Maximum delay (if use_random_delay=True)

chain=driver.actionChains.press_key("enter",use_random_delay=False) #Stops the randomized delay between key_down & key_up
chain.perform() #Execute action chain
```

#### Key Down

You can use key\_down to press but **not** release any key on the keyboard. A list of all "special key" aliases can be found at the bottom of this page:

```python
#Presses but doesn't release the enter key with Action Chains
chain=driver.actionChains.key_down("enter") #Create the action chain
chain.perform() #Execute action chain

#List of default options for this function:
on_element=None #The element to direct the key_down to (not required)

testElement=driver.by_id('testElement') #Get some element on the page
chain=driver.actionChains.key_down("enter",testElement) #Directs the key_down to specific element
chain.perform() #Execute action chain
```

#### Key Up

You can use key\_up to release any key on the keyboard that is currently being pressed by key\_down. A list of all "special key" aliases can be found at the bottom of this page:

```python
#Releases the enter key with Action Chains
chain=driver.actionChains.key_up("enter") #Create the action chain
chain.perform() #Execute action chain

#List of default options for this function:
on_element=None #The element to direct the key_up to (not required)

testElement=driver.by_id('testElement') #Get some element on the page
chain=driver.actionChains.key_up("enter",testElement) #Directs the key_up to specific element
chain.perform() #Execute action chain
```

#### Click

Performs a click, either on or not on a target element:

```python
#Clicks with Action Chains
chain=driver.actionChains.click() #Create the action chain
chain.perform() #Execute action chain

#List of default options for this function:
on_element=None #The element to direct the click to (not required)

testElement=driver.by_id('testElement') #Get some element on the page
chain=driver.actionChains.click(testElement) #Directs the click to specific element
chain.perform() #Execute action chain
```

#### Click & Hold

Performs a click but doesn't release the mouse button, either on or not on a target element:

```python
#Clicks but doesn't release mouse btn with Action Chains
chain=driver.actionChains.click_and_hold() #Create the action chain
chain.perform() #Execute action chain

#List of default options for this function:
on_element=None #The element to direct the click & hold to (not required)

testElement=driver.by_id('testElement') #Get some element on the page
chain=driver.actionChains.click_and_hold(testElement) #Directs the click & hold to specific element
chain.perform() #Execute action chain
```

#### Release Click Hold

Releases click hold, either on or not on a target element:

```python
#Releases mouse click hold with Action Chains
chain=driver.actionChains.release() #Create the action chain
chain.perform() #Execute action chain

#List of default options for this function:
on_element=None #The element to direct the click hold release to (not required)

testElement=driver.by_id('testElement') #Get some element on the page
chain=driver.actionChains.release(testElement) #Directs the click hold release to specific element
chain.perform() #Execute action chain
```

#### Context/Right Click

Performs a right click, either on or not on a target element:

```python
#Performs right-click with Action Chains
chain=driver.actionChains.context_click() #Create the action chain
chain.perform() #Execute action chain

#List of default options for this function:
on_element=None #The element to direct the right-click to (not required)

testElement=driver.by_id('testElement') #Get some element on the page
chain=driver.actionChains.context_click(testElement) #Directs the right-click to specific element
chain.perform() #Execute action chain
```

#### Double Click

Performs a double click, either on or not on a target element:

```python
#Performs double-click with Action Chains
chain=driver.actionChains.double_click() #Create the action chain
chain.perform() #Execute action chain

#List of default options for this function:
on_element=None #The element to direct the double-click to (not required)

testElement=driver.by_id('testElement') #Get some element on the page
chain=driver.actionChains.double_click(testElement) #Directs the double-click to specific element
chain.perform() #Execute action chain
```

#### Drag & Drop

Performs a drag & drop:

```python
#Performs drag & drop by Action Chains
chain=driver.actionChains.drag_and_drop(driver.by_id('elemToStartDrag'),driver.by_id('elemToDropAt'))  #Create the action chain
chain.perform() #Execute action chain
```

#### Drag & Drop By Offset

Performs a drag & drop but uses an offset in pixels away from starting position instead of a target "drop-on" element:

```python
#Performs drag & drop by offset with Action Chains (drags elemToStartDrag & drops it 10 pixels to the right)
chain=driver.actionChains.drag_and_drop_by_offset(driver.by_id('elemToStartDrag'),10,0)  #Create the action chain
chain.perform() #Execute action chain
```

#### Move Mouse By Offset

Moves the mouse by x, y pixels offset:

```python
#Moves mouse by offset with Action Chains (moves mouse 10 pixels to the right)
chain=driver.actionChains.move_by_offset(10,0)  #Create the action chain
chain.perform() #Execute action chain
```

#### Move Mouse To Element

Moves the mouse to an element:

```python
#Moves mouse to target element with Action Chains
testElement=driver.by_id("testElement") #Get some element on the page
chain=driver.actionChains.move_to_element(testElement)  #Create the action chain
chain.perform() #Execute action chain
```

#### Move Mouse To Element With Offset

Moves the mouse to an element with x, y offset in pixels:&#x20;

```python
#Moves mouse to target element with offset with Action Chains (moves mouse 10 pixels to the right of testElement)
testElement=driver.by_id("testElement") #Get some element on the page
chain=driver.actionChains.move_to_element_with_offset(testElement,10,0)  #Create the action chain
chain.perform() #Execute action chain
```

#### Reset Actions

Resets all Action Chains actions:

```python
#Resets all actions with Action Chains
chain=driver.actionChains.reset_actions()  #Reset actions
```

#### Scroll By Amount

Scrolls focused window by x, y pixels:

```python
#Scroll down/up page with Action Chains (scrolls down the page 1000 pixels)
chain=driver.actionChains.scroll_by_amount(0,1000)  #Create the action chain
chain.perform() #Execute action chain
```

#### Scroll To Element

Scrolls focused window until target element is in view:

```python
#Scroll until element is in view with Action Chains
chain=driver.actionChains.scroll_to_element(testElem)  #Create the action chain
chain.perform() #Execute action chain
```

#### Pause

Pause in the middle of action chain for x seconds:

```python
#Pause with Action Chains (waits for 2 seconds before continuing action chain)
chain=driver.actionChains.pause(2)  #Create the action chain
chain.perform() #Execute action chain
```

#### Perform

Perform the entire action chain from first action -> last action:

```python
chain.perform() #Execute action chain
```

### Special Key Aliases

Below, is a list of all "special key" aliases you can use while executing functions like .press\_key():

```python
#Aliases are case insensitive (enter==ENTER)
'ADD':Keys.ADD
'ALT':Keys.ALT
'ARROW_DOWN':Keys.ARROW_DOWN
'ARROW_LEFT':Keys.ARROW_LEFT
'ARROW_RIGHT':Keys.ARROW_RIGHT
'ARROW_UP':Keys.ARROW_UP
'BACKSPACE':Keys.BACKSPACE
'BACK_SPACE':Keys.BACK_SPACE
'CANCEL':Keys.CANCEL
'CLEAR':Keys.CLEAR
'COMMAND':Keys.COMMAND
'CONTROL':Keys.CONTROL
'DECIMAL':Keys.DECIMAL
'DELETE':Keys.DELETE
'DIVIDE':Keys.DIVIDE
'DOWN':Keys.DOWN
'END':Keys.END
'ENTER':Keys.ENTER
'EQUALS':Keys.EQUALS
'ESCAPE':Keys.ESCAPE
'F1':Keys.F1
'F10':Keys.F10
'F11':Keys.F11
'F12':Keys.F12
'F2':Keys.F2
'F3':Keys.F3
'F4':Keys.F4
'F5':Keys.F5
'F6':Keys.F6
'F7':Keys.F7
'F8':Keys.F8
'F9':Keys.F9
'HELP':Keys.HELP
'HOME':Keys.HOME
'INSERT':Keys.INSERT
'LEFT':Keys.LEFT
'LEFT_ALT':Keys.LEFT_ALT
'LEFT_CONTROL':Keys.LEFT_CONTROL
'LEFT_SHIFT':Keys.LEFT_SHIFT
'META':Keys.META
'MULTIPLY':Keys.MULTIPLY
'NULL':Keys.NULL
'NUMPAD0':Keys.NUMPAD0
'NUMPAD1':Keys.NUMPAD1
'NUMPAD2':Keys.NUMPAD2
'NUMPAD3':Keys.NUMPAD3
'NUMPAD4':Keys.NUMPAD4
'NUMPAD5':Keys.NUMPAD5
'NUMPAD6':Keys.NUMPAD6
'NUMPAD7':Keys.NUMPAD7
'NUMPAD8':Keys.NUMPAD8
'NUMPAD9':Keys.NUMPAD9
'PAGE_DOWN':Keys.PAGE_DOWN
'PAGE_UP':Keys.PAGE_UP
'PAUSE':Keys.PAUSE
'RETURN':Keys.RETURN
'RIGHT':Keys.RIGHT
'SEMICOLON':Keys.SEMICOLON
'SEPARATOR':Keys.SEPARATOR
'SHIFT':Keys.SHIFT
'SPACE':Keys.SPACE
'SUBTRACT':Keys.SUBTRACT
'TAB':Keys.TAB
```

