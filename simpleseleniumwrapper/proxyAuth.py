from .baseImports import *

#@for_all_methods(stop_driver_on_error)
class ProxyAuth:
    def __init__(self,proxy_host,proxy_port,proxy_username,proxy_password):
        self.PROXY_HOST=proxy_host
        self.PROXY_PORT=proxy_port
        self.PROXY_USER=proxy_username
        self.PROXY_PASS=proxy_password


    def addProxyAuthExtension(self,options,browser):
        #Create proxy auth folder if not there already
        proxyAuthFolder="./proxyAuth"
        doesFolderExist=os.path.isdir(proxyAuthFolder)
        if doesFolderExist==False:
            os.mkdir(proxyAuthFolder)

        if browser=="chrome":
            pluginfile = f'{os.getcwd()}/proxyAuth/proxy_auth_plugin{self.PROXY_HOST}.{self.PROXY_PORT}.zip'.replace('\\','/')
        #if browser=="firefox":
        #    pluginfile = f'{os.getcwd()}/proxyAuth/proxy_auth_plugin{self.PROXY_HOST}.{self.PROXY_PORT}.xpi'.replace('\\','/')

        if os.path.isfile(pluginfile)==False:
            #Auto-auth extension code from accepted answer: https://stackoverflow.com/questions/55582136/how-to-set-proxy-with-authentication-in-selenium-chromedriver-python - thx :) 
            manifest_json = """
            {
                "version": "1.0.0",
                "manifest_version": 2,
                "name": "Chrome Proxy",
                "permissions": [
                    "proxy",
                    "tabs",
                    "unlimitedStorage",
                    "storage",
                    "<all_urls>",
                    "webRequest",
                    "webRequestBlocking"
                ],
                "background": {
                    "scripts": ["background.js"]
                },
                "minimum_chrome_version":"22.0.0"
            }
            """

            background_js = """
            var config = {
                    mode: "fixed_servers",
                    rules: {
                    singleProxy: {
                        scheme: "http",
                        host: "%s",
                        port: parseInt(%s)
                    },
                    bypassList: ["localhost"]
                    }
                };

            chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

            function callbackFn(details) {
                return {
                    authCredentials: {
                        username: "%s",
                        password: "%s"
                    }
                };
            }

            chrome.webRequest.onAuthRequired.addListener(
                        callbackFn,
                        {urls: ["<all_urls>"]},
                        ['blocking']
            );
            """ % (self.PROXY_HOST, self.PROXY_PORT, self.PROXY_USER, self.PROXY_PASS)

            with zipfile.ZipFile(pluginfile, 'w') as zp:
                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js)

        if browser=="chrome":
            options.add_extension(pluginfile)
            return options

        #Coming soon (hopefully)
        #if browser=="firefox":
        #    options.add_extension(extension=pluginfile)
        #    return options
