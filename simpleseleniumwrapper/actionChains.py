from .baseImports import *
from .webElement import WebElement

#@for_all_methods(stop_driver_on_error)
class ActionChains:
    def __init__(self,actionChains):
        #Set actionchains root selenium object
        self.actionChains=actionChains

        #Set action chains key aliases
        allKeyAliases={
            'ADD':Keys.ADD,
            'ALT':Keys.ALT,
            'ARROW_DOWN':Keys.ARROW_DOWN,
            'ARROW_LEFT':Keys.ARROW_LEFT,
            'ARROW_RIGHT':Keys.ARROW_RIGHT,
            'ARROW_UP':Keys.ARROW_UP,
            'BACKSPACE':Keys.BACKSPACE,
            'BACK_SPACE':Keys.BACK_SPACE,
            'CANCEL':Keys.CANCEL,
            'CLEAR':Keys.CLEAR,
            'COMMAND':Keys.COMMAND,
            'CONTROL':Keys.CONTROL,
            'DECIMAL':Keys.DECIMAL,
            'DELETE':Keys.DELETE,
            'DIVIDE':Keys.DIVIDE,
            'DOWN':Keys.DOWN,
            'END':Keys.END,
            'ENTER':Keys.ENTER,
            'EQUALS':Keys.EQUALS,
            'ESCAPE':Keys.ESCAPE,
            'F1':Keys.F1,
            'F10':Keys.F10,
            'F11':Keys.F11,
            'F12':Keys.F12,
            'F2':Keys.F2,
            'F3':Keys.F3,
            'F4':Keys.F4,
            'F5':Keys.F5,
            'F6':Keys.F6,
            'F7':Keys.F7,
            'F8':Keys.F8,
            'F9':Keys.F9,
            'HELP':Keys.HELP,
            'HOME':Keys.HOME,
            'INSERT':Keys.INSERT,
            'LEFT':Keys.LEFT,
            'LEFT_ALT':Keys.LEFT_ALT,
            'LEFT_CONTROL':Keys.LEFT_CONTROL,
            'LEFT_SHIFT':Keys.LEFT_SHIFT,
            'META':Keys.META,
            'MULTIPLY':Keys.MULTIPLY,
            'NULL':Keys.NULL,
            'NUMPAD0':Keys.NUMPAD0,
            'NUMPAD1':Keys.NUMPAD1,
            'NUMPAD2':Keys.NUMPAD2,
            'NUMPAD3':Keys.NUMPAD3,
            'NUMPAD4':Keys.NUMPAD4,
            'NUMPAD5':Keys.NUMPAD5,
            'NUMPAD6':Keys.NUMPAD6,
            'NUMPAD7':Keys.NUMPAD7,
            'NUMPAD8':Keys.NUMPAD8,
            'NUMPAD9':Keys.NUMPAD9,
            'PAGE_DOWN':Keys.PAGE_DOWN,
            'PAGE_UP':Keys.PAGE_UP,
            'PAUSE':Keys.PAUSE,
            'RETURN':Keys.RETURN,
            'RIGHT':Keys.RIGHT,
            'SEMICOLON':Keys.SEMICOLON,
            'SEPARATOR':Keys.SEPARATOR,
            'SHIFT':Keys.SHIFT,
            'SPACE':Keys.SPACE,
            'SUBTRACT':Keys.SUBTRACT,
            'TAB':Keys.TAB
        }
        
        #Turn dict keys to lowercase
        allKeyAliasesLower={k.lower():v for k,v in allKeyAliases.items()}

        #Set key aliases
        self.allKeyAliases=allKeyAliasesLower

    
    #--------------------ACTIONCHAINS--------------------------
    def press_key(self,key_alias,use_random_delay=True,min_delay=0.1,max_delay=0.3):
        #Get key to use
        if key_alias.lower() in self.allKeyAliases:
            keyToUse=self.allKeyAliases[key_alias.lower()]
        else:
            keyToUse=key_alias.lower()

        #Key down
        thisChain=self.actionChains.key_down(keyToUse)

        #random delay
        if use_random_delay==True:
            time.sleep(random.uniform(min_delay,max_delay))

        #Key up
        thisChain.key_up(keyToUse)

        #Return chain
        return ActionChains(thisChain)

    def click(self,on_element: WebElement | None = None):
        if on_element!=None:
            return ActionChains(self.actionChains.click(on_element.webElement))
        else:
            return ActionChains(self.actionChains.click())

    def click_and_hold(self,on_element: WebElement | None = None):
        if on_element!=None:
            return ActionChains(self.actionChains.click_and_hold(on_element.webElement))
        else:
            return ActionChains(self.actionChains.click_and_hold())

    def context_click(self,on_element: WebElement | None = None):
        if on_element!=None:
            return ActionChains(self.actionChains.context_click(on_element.webElement))
        else:
            return ActionChains(self.actionChains.context_click())

    def double_click(self,on_element: WebElement | None = None):
        if on_element!=None:
            return ActionChains(self.actionChains.double_click(on_element.webElement))
        else:
            return ActionChains(self.actionChains.double_click())

    def drag_and_drop(self,source: WebElement, target: WebElement):
        return ActionChains(self.actionChains.drag_and_drop(source.webElement,target.webElement))

    def drag_and_drop_by_offset(self,source: WebElement, xoffset: int, yoffset: int):
        return ActionChains(self.actionChains.drag_and_drop_by_offset(source.webElement,xoffset,yoffset))

    def key_down(self,key_alias, element: WebElement | None = None):
        #Get key to use
        if key_alias.lower() in self.allKeyAliases:
            keyToUse=self.allKeyAliases[key_alias.lower()]
        else:
            keyToUse=key_alias.lower()

        #Return key down
        if element!=None:
            return ActionChains(self.actionChains.key_down(keyToUse,element.webElement))
        else:
            return ActionChains(self.actionChains.key_down(keyToUse))

    def key_up(self,key_alias, element: WebElement | None = None):
        #Get key to use
        if key_alias.lower() in self.allKeyAliases:
            keyToUse=self.allKeyAliases[key_alias.lower()]
        else:
            keyToUse=key_alias.lower()

        #Return key down
        if element!=None:
            return ActionChains(self.actionChains.key_up(keyToUse,element.webElement))
        else:
            return ActionChains(self.actionChains.key_up(keyToUse))

    def move_by_offset(self,xoffset: int, yoffset: int):
        return ActionChains(self.actionChains.move_by_offset(xoffset,yoffset))

    def move_to_element(self,to_element: WebElement):
        return ActionChains(self.actionChains.move_to_element(to_element.webElement))

    def move_to_element_with_offset(self,to_element: WebElement, xoffset: int, yoffset: int):
        return ActionChains(self.actionChains.move_to_element_with_offset(to_element.webElement,xoffset,yoffset))

    def release(self,on_element: WebElement | None = None):
        if on_element!=None:
            return ActionChains(self.actionChains.release(on_element.webElement))
        else:
            return ActionChains(self.actionChains.release())

    def reset_actions(self):
        return ActionChains(self.actionChains.reset_actions())

    def scroll_by_amount(self,delta_x: int, delta_y: int):
        return ActionChains(self.actionChains.scroll_by_amount(delta_x,delta_y))

    def scroll_to_element(self,element: WebElement):
        return ActionChains(self.actionChains.scroll_to_element(element.webElement))

    #Not needed since it has same functionality as press_key
    #def send_keys(self,*keys_to_send: str):
    #    return ActionChains(self.actionChains.send_keys(keys_to_send))

    #def send_keys_to_element(self,element: WebElement, *keys_to_send: str):
    #    return ActionChains(self.actionChains.send_keys_to_element(element.webElement,keys_to_send))

    def pause(self,seconds: float | int):
        return ActionChains(self.actionChains.pause(seconds))

    def perform(self):
        return self.actionChains.perform()


        
