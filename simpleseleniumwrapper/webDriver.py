from .webdriverManager import WebdriverManager
from .baseImports import *
from .elementLocation import ElementLocation
from .webElement import WebElement
from .actionChains import ActionChains as SimpleSeleniumActionChains
from .alerts import Alerts as SimpleSeleniumAlerts
from .proxyAuth import ProxyAuth as SimpleSeleniumProxyAuth
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.remote.script_key import ScriptKey
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService

#Main Simple Selenium class
#@for_all_methods(stop_driver_on_error)
class WebDriver (ElementLocation):
    def __init__(
        self,
        webdriverName,
        headless=False,
        maximized=False,
        custom_chrome_options=False,
        custom_firefox_options=False,
        firefox_binary_location=False,
        save_profile=False,
        profile_directory=None,
        profile_name=None,
        show_selenium_cmd=False,
        use_proxy=False,
        proxy_host=None,
        proxy_port=None,
        proxy_username=None,
        proxy_password=None,
        verbose=False,
        enable_basic_logging=True,
        save_logs_in_file=False,
        logging_file_name=None
    ):

        #Set up logging
        if enable_basic_logging==True:
            logging_level=logging.INFO
        else:
            logging_level=logging.WARNING

        #Set filename
        if save_logs_in_file==True:
            #Check if logging folder exists already & create it if not
            loggingFolderDir="./simpleSeleniumLogs/"
            doesLoggingFolderExist=os.path.isdir(loggingFolderDir)
            if doesLoggingFolderExist==False:
                os.mkdir(loggingFolderDir)

            #Set default logging name if not defined
            if logging_file_name==None:
                logging_file_name_final=f"logs_{datetime.now().strftime('%m-%d-%Y.%H-%M-%S')}.log"
            else:
                logging_file_name_final=logging_file_name

            #Basic config logging with filename
            logging.basicConfig(level=logging_level,filename=f"{loggingFolderDir}{logging_file_name_final}")
        else:
            logging.basicConfig(level=logging_level)
        
        #Set webdriver name for class
        self.webdriverName=webdriverName
        
        #Get & set webdriver location through webdriver manager
        webdriverLocation=WebdriverManager().installWebdriverIfNeededAndGetDownloadLocation(webdriverName)
        self.webdriverExecutablePath=webdriverLocation

        #Set OS
        thisOS=str(platform.system()).lower()
        self.thisOS=thisOS

        #Set architecture
        if sys.maxsize>2147483647:
            thisOSArchitecture="64"
        else:
            thisOSArchitecture="32"
        self.thisOSArchitecture=thisOSArchitecture

        #Set startup options
        self.startupOptions={}
        self.startupOptions['headless']=headless
        self.startupOptions['maximized']=maximized
        self.startupOptions['custom_chrome_options']=custom_chrome_options
        self.startupOptions['custom_firefox_options']=custom_firefox_options
        self.startupOptions['firefox_binary_location']=firefox_binary_location
        self.startupOptions['save_profile']=save_profile
        self.startupOptions['profile_directory']=profile_directory
        self.startupOptions['profile_name']=profile_name
        self.startupOptions['show_selenium_cmd']=show_selenium_cmd
        self.startupOptions['use_proxy']=use_proxy
        self.startupOptions['proxy_host']=proxy_host
        self.startupOptions['proxy_port']=proxy_port
        self.startupOptions['proxy_username']=proxy_username
        self.startupOptions['proxy_password']=proxy_password
        self.startupOptions['verbose']=verbose

        #Start driver
        self.start()


    #--------------------SIMPLE SELENIUM CUSTOM FUNCTIONS-----------------------
    def start(self):
        #Get startup options
        startupOptions=self.startupOptions
        
        #init webdriver
        if self.webdriverName=="chrome":
            #Make sure user doesnt want to pass custom chrome options object
            if startupOptions['custom_chrome_options']==False:
                #Set chrome options
                chrome_options = chromeOptions()
             
                #Basic options
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--no-default-browser-check")
                chrome_options.add_argument("--no-first-run")
                
                #Set maximized window or not
                if startupOptions['maximized']==True:
                    chrome_options.add_argument("--start-maximized")

                #Anti-bot detection evasion part 1
                chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
                chrome_options.add_experimental_option('useAutomationExtension', False)
                chrome_options.add_argument("--disable-blink-features=AutomationControlled")
                chrome_options.add_argument("--disable-popup-blocking")
                #chrome_options.add_argument("--auto-open-devtools-for-tabs")
                #chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36");

                #Set language
                language=False
                try:
                    language = locale.getdefaultlocale()[0].replace("_", "-")
                except Exception:
                    pass
                if language==False:
                    language = "en-US"
                chrome_options.add_argument("--lang=%s" % language)

                #If user wants to save browser session as a profile
                if startupOptions['save_profile']==True:                
                    #Get profile name
                    profile_name=startupOptions['profile_name']

                    #See if user set custom user data directory
                    if startupOptions['profile_directory']!=None:
                        profile_directory=startupOptions['profile_directory']
                        if os.path.isdir(profile_directory)==False:
                            raise Exception("Profile directory is not valid! Please define a valid path (Eg. C:/path/to/profile/directory) or leave profile_directory blank and SimpleSelenium will automatically generate a profile directory folder")
                    else:
                        #Check if profile folder for exists
                        profile_directory=f"{os.getcwd()}\\chromeProfileData"
                        doesProfileDataFolderExist=os.path.isdir(profile_directory)
                        if doesProfileDataFolderExist==False:
                            os.mkdir(profile_directory)
                    
                    #Save profile data in profiles folder
                    chrome_options.add_argument(f'--user-data-dir={profile_directory}')
                    chrome_options.add_argument(f'--profile-directory={profile_name}')

                #Proxy authentication script
                if startupOptions['proxy_username']!=None:
                    #Init proxy auth
                    proxyAuthHere=SimpleSeleniumProxyAuth(startupOptions['proxy_host'],startupOptions['proxy_port'],startupOptions['proxy_username'],startupOptions['proxy_password'])
                
                    #Add to options
                    chrome_options=proxyAuthHere.addProxyAuthExtension(chrome_options,"chrome")
                else:
                    chrome_options.add_argument('--disable-extensions')
    
                #Toggle headless
                if startupOptions['headless']==True:
                    chrome_options.add_argument("--headless=new")
                else:
                    chrome_options.add_argument("--remote-allow-origins=*");
                    chrome_options.add_argument("--no-sandbox")
                    chrome_options.add_argument("--disable-dev-shm-usage");

                #Proxy toggle
                if startupOptions['use_proxy']!=False:
                    proxy_host=startupOptions['proxy_host']
                    proxy_port=startupOptions['proxy_port']
                    chrome_options.add_argument(f'--proxy-server={proxy_host}:{proxy_port}')
                else:
                    #Clear proxy if user is using persistent profile
                    chrome_options.add_argument(f'--no-proxy-server')
                    
            else:
                chrome_options=startupOptions['custom_chrome_options']
                
            #Init chromedriver
            service=Service(self.webdriverExecutablePath)
            if startupOptions['show_selenium_cmd']==True:
                service.creationflags = CREATE_NO_WINDOW #Hides cmd prompt that pops up
            driver=webdriver.Chrome(service=service,options=chrome_options)

            #Anti-bot detection evasion part 2
            driver.execute_script("""
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                window.key=undefined;
            """) 

            
        if self.webdriverName=="firefox":
            warnings.warn("SimpleSelenium FireFox is currently in experimental mode, it's recommended to use Chrome instead.")
            #Get the binary path of firefox executable
            if startupOptions['firefox_binary_location']==False:
                #Attempt to automatically find binary location of firefox
                if self.thisOS=="windows":
                    if os.path.isdir('C:/Program Files (x86)/Mozilla Firefox/')==True:
                        binaryLocation="C:/Program Files (x86)/Mozilla Firefox/firefox.exe"
                    if os.path.isdir('C:/Program Files/Mozilla Firefox/')==True:
                        binaryLocation="C:/Program Files/Mozilla Firefox/firefox.exe"
                else:
                    if os.path.isdir('/usr/bin/firefox/firefox-bin'):
                        binaryLocation="/usr/bin/firefox/firefox-bin"

                #If binary not found, err
                if binaryLocation=="":
                    raise Exception("Unable to find FireFox installed on your system. If you have installed FireFox and this error still appears, pass the firefox_binary_location parameter when initiating the SimpleSelenium class. Eg: webdriver=SimpleSelenium('firefox',{firefox_binary_location='path/to/your/firefox/binary'})")
            else:
                binaryLocation=startupOptions['firefox_binary_location']

            #Set FireFox options
            if startupOptions['save_profile']==True:
                #Check if profile folder for exists
                #profile_name=startupOptions['profile_name']
                #profile_directory=f"{os.getcwd()}\\firefoxProfileData\\{profile_name}"
                #doesProfileDataFolderExist=os.path.isdir(profile_directory)
                #if doesProfileDataFolderExist==False:
                #    os.mkdir(profile_directory)
                #options.set_capability("moz:firefoxOptions", {
                #    "args":["-profile", full_profile_directory]
                #})
                #profile = webdriver.FirefoxProfile(profile_directory)
                raise Exception('FireFox profiles are not available yet for SimpleSelenium. Use chrome instead')
            #else:
                #profile = webdriver.FirefoxProfile()
            if startupOptions['custom_firefox_options']==False:
                #Init firefox options
                options=firefoxOptions()

                #Add binary location for firefox
                options.binary_location=binaryLocation

                #Headless
                options.headless = startupOptions['headless']

                #Proxy
                if startupOptions['use_proxy']==True:
                    #Get proxy data
                    #proxy_host=startupOptions['proxy_host']
                    #proxy_port=startupOptions['proxy_port']

                    #Set proxy
                    #profile.set_preference("network.proxy.type", 1)
                    #profile.set_preference("network.proxy.http", proxy_host)
                    #profile.set_preference("network.proxy.http_port", int(proxy_port))
                    #profile.set_preference("network.proxy.ssl", proxy_host)
                    #profile.set_preference("network.proxy.ssl_port", int(proxy_port))
                    #profile.set_preference("network.proxy.no_proxies_on", "")
                    #profile.set_preference('browser.formfill.enable', False)

                    #Proxy authentication script
                    if startupOptions['proxy_username']!=None:
                        raise Exception("Proxy username:password authentication is not currently supported for FireFox, apologies for any inconvenience this causes. In the meantime you can use Chrome for proxy username:password authentication or configure your proxies to use IP authentication.")
                        #Init proxy auth
                        #proxyAuthHere=SimpleSeleniumProxyAuth(startupOptions['proxy_host'],startupOptions['proxy_port'],startupOptions['proxy_username'],startupOptions['proxy_password'])
                        
                        #Add to options
                        #profile=proxyAuthHere.addProxyAuthExtension(profile,"firefox")
                
            else:
                options=startupOptions['custom_firefox_options']

            #Update firefox profile prefs
            #profile.update_preferences()

            #Init FireFox
            thisService=FireFoxService(executable_path=self.webdriverExecutablePath)
            driver=webdriver.Firefox(service=thisService,options=options)#,firefox_profile=profile)
            self.driver=driver

            #Maximized
            if startupOptions['custom_firefox_options']==False:
                if startupOptions['maximized']==True:
                    driver.maximize_window()

            #Return true to indicate successful webdriver start
            return True

        #Set driver
        self.driver=driver

        #Init ElementLocation class
        super().__init__(driver,WebElement)

        #Set action chains for driver
        action=SimpleSeleniumActionChains(ActionChains(driver))
        self.actionChains=action

        #Set alerts for driver
        alerts=SimpleSeleniumAlerts(driver)
        self.alerts=alerts
            

    def close(self):
        #Close webdriver
        self.driver.close()
        self.driver.quit()

    def close_active_tab(self):
        self.driver.close()

    def visit(self,url,referrer=False,use_random_delay=True,min_delay=3.0,max_delay=3.5):
        driver=self.driver
        if referrer==False:
            driver.get(url)
        else:
            #Go to referrer site
            driver.get(referrer)

            #Execute script to open target page in new tab
            driver.execute_script(f"window.open('{url}','_blank')")

            #Wait for x seconds
            if use_random_delay==True:
                time.sleep(random.uniform(min_delay,max_delay))

            #Close old tab
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])


    #--------------------ACTION CHAINS SUBROUTINE----------------------
    def special_key_combo(self,keysList):
        #Get action chain 
        chain=SimpleSeleniumActionChains(self.actionChains)

        #Push down keys 
        for key in keysList:
            chain=chain.key_down(key)

        #Let go of keys
        for key in keysList:
            chain=chain.key_up(key)

        #Perform the key combo
        chain.perform()

    #--------------------OTHER BASIC SELENIUM FUNCTIONS WITH ALIASES------------------------
    def focus_document(self):
        return self.driver.switch_to.default_content()

    def focus_iframe(self,iframe):
        return self.driver.switch_to.frame(iframe)

    def focus_parent_iframe(self):
        return self.driver.switch_to.parent_frame()

    def application_cache(self):
        return self.driver.application_cache

    def capabilities(self):
        return self.driver.capabilities

    def desired_capabilities(self):
        return self.driver.desired_capabilities

    def page_source(self):
        return self.driver.page_source

    def name(self):
        return self.driver.name

    def timeouts(self):
        return self.driver.timeouts

    def file_detector(self):
        return self.driver.file_detector

    def virtual_authenticator_id(self):
        return self.driver.virtual_authenticator_id

    def window_handles(self):
        return self.driver.window_handles

    def orientation(self):
        return self.driver.orientation

    def current_window_handle(self):
        return self.driver.current_window_handle

    def title(self):
        return self.driver.title

    def mobile(self):
        return self.driver.mobile

    def log_types(self):
        return self.driver.log_types

    def current_url(self):
        return self.driver.current_url

    #--------------------SELENIUM BASIC FUNCTIONS-----------------------
    def screenshot_base64(self):
        return self.driver.get_screenshot_as_base64()

    def screenshot_png(self):
        return self.driver.get_screenshot_as_png()

    def screenshot(self,filename):
        return self.driver.get_screenshot_as_file(filename)
    
    def add_cookie(self,cookie_dict):
        return self.driver.add_cookie(cookie_dict)

    def add_credential(self,credential):
        return self.driver.add_credential(credential)

    def add_virtual_authenticator(self,virtual_credential):
        return self.driver.add_virtual_authenticator(virtual_credential)

    def back(self):
        return self.driver.back()

    def create_web_element(self,element_id):
        return self.driver.create_web_element(element_id)

    def delete_all_cookies(self):
        return self.driver.delete_all_cookies()

    def delete_cookie(self,cookie_name):
        return self.driver.delete_cookie(cookie_name)

    def delete_downloadable_files(self):
        return self.driver.delete_downloadable_files()

    def download_file(self,file_name,target_directory):
        return self.driver.download_file(file_name,target_directory)

    def execute(self,driver_command,params=None):
        return self.driver.execute(driver_command,params)

    def execute_async_script(self,script: str, *args):
        return self.driver.execute_async_script(script,args)

    def execute_script(self,script, *args):
        return self.driver.execute_script(script,args)

    def forward(self):
        return self.driver.forward()

    def fullscreen_window(self):
        return self.driver.fullscreen_window()

    def get_cookie(self,cookie_name):
        return self.driver.get_cookie(cookie_name)

    def get_cookies(self):
        return self.driver.get_cookies()

    def get_credentials(self):
        return self.driver.get_credentials()

    def get_downloadable_files(self):
        return self.driver.get_downloadable_files()

    def get_log(self,log):
        return self.driver.get_log(log)

    def get_pinned_scripts(self):
        return self.driver.get_pinned_scripts()

    def get_window_position(self,windowHandle='current'):
        return self.driver.get_window_position(windowHandle)

    def get_window_rect(self):
        return self.driver.get_window_rect()

    def get_window_size(self,windowHandle:str = 'current'):
        return self.driver.get_window_size(windowHandle)

    def implicitly_wait(self,time_to_wait: float):
        return self.driver.implicitly_wait(time_to_wait)

    def maximize_window(self):
        return self.driver.maximize_window()

    def minimize_window(self):
        return self.driver.minimize_window()

    def pin_script(self,script: str, script_key=None):
        return self.driver.pin_script(script,script_key)

    def print_page(self,print_options: PrintOptions | None = None):
        return self.driver.print_page(print_options)

    def refresh(self):
        return self.driver.refresh()

    def remove_all_credentials(self):
        return self.driver.remove_all_credentials()

    def remove_credential(self,credential_id: str | bytearray):
        return self.driver.remove_credential(credential_id)

    def remove_virtual_authenticator(self):
        return self.driver.remove_virtual_authenticator()

    def set_page_load_timeout(self,time_to_wait: float):
        return self.driver.set_page_load_timeout(time_to_wait)

    def set_script_timeout(self,time_to_wait: float):
        return self.driver.set_script_timeout(time_to_wait)

    def set_user_verified(self,verified: bool):
        return self.driver.set_user_verified(time_to_wait)

    def set_window_position(self,x,y,windowHandle: str = 'current'):
        return self.driver.set_window_position(x,y,windowHandle)

    def set_window_rect(self,x=None, y=None, width=None, height=None):
        return self.driver.set_window_rect(x,y,width,height)

    def set_window_size(self,width, height, windowHandle: str = 'current'):
        return self.driver.set_window_size(width, height, windowHandle)

    def start_client(self):
        return self.driver.start_client()

    def start_session(self,capabilities: dict):
        return self.driver.start_session(capabilities)

    def stop_client(self):
        return self.driver.stop_client()

    def unpin(self,script_key: ScriptKey):
        return self.driver.unpin(script_key)

    

        
