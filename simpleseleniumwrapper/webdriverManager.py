from .baseImports import *

#Automated webdriver installer
#@for_all_methods(stop_driver_on_error)
class WebdriverManager:
    #This function is from: https://gist.github.com/primaryobjects/d5346bf7a173dbded1a70375ff7461b4 
    def extract_version_registry(self,output):
        try:
            google_version = ''
            for letter in output[output.rindex('DisplayVersion    REG_SZ') + 24:]:
                if letter != '\n':
                    google_version += letter
                else:
                    break
            return(google_version.strip())
        except TypeError:
            logging.error(err)
            return

    #This function is from: https://gist.github.com/primaryobjects/d5346bf7a173dbded1a70375ff7461b4 
    def extract_version_folder(self):
        # Check if the Chrome folder exists in the x32 or x64 Program Files folders.
        for i in range(2):
            path = 'C:\\Program Files' + (' (x86)' if i else '') +'\\Google\\Chrome\\Application'
            if os.path.isdir(path):
                paths = [f.path for f in os.scandir(path) if f.is_dir()]
                for path in paths:
                    filename = os.path.basename(path)
                    pattern = '\d+\.\d+\.\d+\.\d+'
                    match = re.search(pattern, filename)
                    if match and match.group():
                        # Found a Chrome version.
                        return match.group(0)
        return None

    #This function is from: https://gist.github.com/primaryobjects/d5346bf7a173dbded1a70375ff7461b4 
    def get_chrome_version(self):
        version = None
        install_path = None
        try:
            if sys.platform == "linux" or platform == "linux2":
                # linux
                install_path = "/usr/bin/google-chrome"
            elif sys.platform == "darwin":
                # OS X
                install_path = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
            elif sys.platform == "win32":
                # Windows...
                try:
                    # Try registry key.
                    stream = os.popen('reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome"')
                    output = stream.read()
                    version = self.extract_version_registry(output)
                except Exception as ex:
                    # Try folder path.
                    version = self.extract_version_folder()
        except Exception as err:
            logging.error(err)
        version = os.popen(f"{install_path} --version").read().strip('Google Chrome ').strip() if install_path else version
        return version
    
    def patchChromedriverForAntiDetection(self,chromedriverPath):
        #Code from https://github.com/ultrafunkamsterdam/undetected-chromedriver/blob/master/undetected_chromedriver/patcher.py
        with io.open(chromedriverPath, "r+b") as fh:
            content = fh.read()
            match_injected_codeblock = re.search(rb"\{window\.cdc.*?;\}", content)
            if match_injected_codeblock:
                target_bytes = match_injected_codeblock[0]
                new_target_bytes = (
                    b'{console.log("")}'.ljust(
                        len(target_bytes), b" "
                    )
                )
                new_content = content.replace(target_bytes, new_target_bytes)
                if new_content == content:
                    logging.error("Unable to patch ChromeDriver")
                else:
                    logging.info("Patched ChromeDriver successfully")
                fh.seek(0)
                fh.write(new_content)
        

    def downloadChromedriverFile(self,downloadPath,chromedriverVersion,OSAndArchitectureShortName,fileExtension):
        #Get latest versions of chromedriver
        response=requests.get("https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json")
        responseJSON=response.json()

        #Iterate all versions and get closest one to this chrome version
        thisChromedriverURL=""
        for versionData in responseJSON['versions']:
            thisVersionHerePre=versionData['version'].split('.')
            thisVersionHere=f"{thisVersionHerePre[0]}.{thisVersionHerePre[1]}."
            if thisVersionHere in chromedriverVersion:
                theseDownloads=versionData['downloads']['chromedriver']
                for thisDownloadData in theseDownloads:
                    if thisDownloadData['platform']==OSAndArchitectureShortName:
                        thisChromedriverURL=thisDownloadData['url']
                        break
                if thisChromedriverURL!="":
                    break
        
        #Get the correct chromedriver file from URL
        if "://" not in thisChromedriverURL:
            logging.exception('Unable to find matching chromedriver version for your version of Chrome. Please try updating chrome')
            raise Exception('Unable to find matching chromedriver version for your version of Chrome. Please try updating chrome')

        zipFileResponse=requests.get(thisChromedriverURL)

        #Write file content
        downloadFilePath=f"{downloadPath}/chromedriverData.zip"
        open(downloadFilePath,'wb').write(zipFileResponse.content)

        #Extract chromedriver from zip and put in webdriverManager folder
        finalChromedriverPath=f'{downloadPath}/chromedriver_{chromedriverVersion}{fileExtension}'
        with zipfile.ZipFile(downloadFilePath) as z:
            with open(finalChromedriverPath, 'wb') as f:
                f.write(z.read(f'chromedriver-{OSAndArchitectureShortName}/chromedriver{fileExtension}'))

        #Delete the zip file
        os.remove(downloadFilePath)

        #Patch the chromedriver to remove cdc_ var that gets browser detected
        self.patchChromedriverForAntiDetection(finalChromedriverPath)
        

    def downloadGeckodriverFile(self,downloadPath,OSAndArchitectureShortName,thisURL,fileExtension):
        #Get the correct chromedriver file from URL
        zipFileResponse=requests.get(thisURL)

        #Write file content
        downloadFilePath=f"{downloadPath}/geckodriverData.zip"
        open(downloadFilePath,'wb').write(zipFileResponse.content)

        #Extract chromedriver from zip and put in webdriverManager folder
        timeToPutInGeckodriverFilename=int(time.time()+(86400))
        with zipfile.ZipFile(downloadFilePath) as z:
            with open(f'{downloadPath}/geckodriver_{OSAndArchitectureShortName}_{timeToPutInGeckodriverFilename}{fileExtension}', 'wb') as f:
                f.write(z.read(f'geckodriver{fileExtension}'))

        #Delete the zip file
        os.remove(downloadFilePath)
        
        
    def getCurrentVersionOfBrowser(self,webdriverName,webdriverFolderDir):
        if webdriverName=="chrome":
            #Get current version of chrome running on this system (creator of function linked above)
            chromedriverVersion=self.get_chrome_version()
            
            #Return version
            return chromedriverVersion
            
        if webdriverName=="firefox":
            #Check if we need to recheck version
            recheckVersion=True
            allFilesInWebdriverFolder=os.listdir(webdriverFolderDir)
            if len(allFilesInWebdriverFolder)>0:
                for thisWebdriverFile in allFilesInWebdriverFolder:
                    if "geckodriver_" in thisWebdriverFile:
                        #Get split filename
                        splitFilename=thisWebdriverFile.split("_")[2]

                        #Get unix number from filename
                        lastUpdatedGeckoDriver=int(splitFilename.strip(string.ascii_letters).replace('.',''))
                                
                        #If the current unix time isnt past old unix + 24 hrs, dont refresh version
                        if time.time()<lastUpdatedGeckoDriver:
                            recheckVersion=False
                            break

            #Return recheck version
            return recheckVersion
                        
        if webdriverName=="edge":
            pass            

    def installWebdriverIfNeededAndGetDownloadLocation(self,webdriverName):
        #Set base vars
        locationOfWebdriver="";
        downloadNewVersion=False
        
        #Check if webdriver folder & chromedriver already exist
        webdriverFolderDir="./webdriverManager"
        doesDownloadFolderExist=os.path.isdir(webdriverFolderDir)
        if doesDownloadFolderExist==False:
            os.mkdir(webdriverFolderDir)
            downloadNewVersion=True

        #Turn webdriver name to lowercase
        webdriverName=webdriverName.lower()
        
        #Get OS
        thisOS=str(platform.system()).lower()

        #Get architecture
        if thisOS!="windows":
            if sys.maxsize>2147483647:
                thisOSArchitecture="64"
            else:
                thisOSArchitecture="32"
        else:
            thisOSArchitecture="32"

        #Make sure this webdriver name is allowed
        allowedWebdriverNames=[
            'chrome',
            'firefox'
        ]
        if webdriverName in allowedWebdriverNames:
            webdriverVersion=self.getCurrentVersionOfBrowser(webdriverName,webdriverFolderDir)
        else:
            raise Exception(f"WebDriver name is not recognized. Supported WebDriver names: {allowedWebdriverNames}")

        #Get short name for os
        shortOSNames={
            'windows':'win',
            'linux':'linux'
        }
        shortOSName=shortOSNames[thisOS]

        #Platform & architecture short name for downloading files
        platformArchitectureShort=f"{shortOSName}{thisOSArchitecture}"

        #Get correct file extension to write
        if "win" in platformArchitectureShort:
            fileExtension=".exe"
        else:
            fileExtension=""

        if webdriverName=="chrome":
            #Get all files in webdriver folder & check if we have latest version of chromedriver
            allFilesInWebdriverFolder=os.listdir(webdriverFolderDir)
            if len(allFilesInWebdriverFolder)>0 and "chromedriver_" in str(os.listdir(webdriverFolderDir)):
                for chromedriverFile in allFilesInWebdriverFolder:
                    #Make sure file is actually a chromedriver file
                    if "chromedriver_" in chromedriverFile:
                        #Get version of this chromedriver file
                        if thisOS=="windows":
                            thisVersionOfFile=chromedriverFile.split("_")[1].split(".exe")[0]
                        else:
                            thisVersionOfFile=chromedriverFile.split("_")[1]

                        #If version is not latest, delete that chromedriver & replace with new one
                        if thisVersionOfFile!=webdriverVersion:
                            os.remove(f"{webdriverFolderDir}/chromedriver_{thisVersionOfFile}{fileExtension}")
                            downloadNewVersion=True
                    else:
                        #Delete compressed files from webdriver downloads
                        if ".zip" in chromedriverFile or ".tar" in chromedriverFile:
                            os.remove(f"{webdriverFolderDir}/chromedriver_{thisVersionOfFile}{fileExtension}")
                        
            else:
                downloadNewVersion=True
                
            #Download the driver file
            if downloadNewVersion==True:
                logging.info("Downloading latest version of ChromeDriver")
                self.downloadChromedriverFile(webdriverFolderDir,webdriverVersion,platformArchitectureShort,fileExtension)

            #Get location of final webdriver file
            locationOfWebdriver=f"{webdriverFolderDir}/chromedriver_{webdriverVersion}{fileExtension}"

        if webdriverName=="firefox":
            #Recheck version if needed
            if webdriverVersion==True:
                logging.info("Downloading latest version of GeckoDriver")
                
                #Get latest geckodriver version data from github
                response=requests.get('https://api.github.com/repos/mozilla/geckodriver/releases/latest')
                responseJSON=response.json()

                #Iterate all downloads & find correct one for os & architecture
                for assetData in responseJSON['assets']:
                    #Get geckodriver url
                    thisURL=assetData['browser_download_url']

                    #Check os & architecture
                    filenameDataSplit=thisURL.split('-')
                    filenameData=f"{filenameDataSplit[1]}{filenameDataSplit[2]}"

                    #If this version is compatible, download
                    if shortOSName in filenameData and thisOSArchitecture in filenameData:
                        #Download this version of geckodriver
                        self.downloadGeckodriverFile(webdriverFolderDir,platformArchitectureShort,thisURL,fileExtension)

                        break
                        
            #Get location of final webdriver file
            allFilesInWebdriverFolder=os.listdir(webdriverFolderDir)
            for file in allFilesInWebdriverFolder:
                if "geckodriver" in file:
                    locationOfWebdriver=f"{webdriverFolderDir}/{file}"
                    break
                

        #Return location of webdriver file
        return locationOfWebdriver;
