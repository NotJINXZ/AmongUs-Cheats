# Skid = Bad :(
# Don't bully me for this code. ik it's bad

import os, time, sys, hashlib
from auth import api

try:
    from colorama import Fore
except ModuleNotFoundError:
    os.system("pip install colorama")
    from colorama import Fore
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests


os.system("title JINXZ WARE - Installer")
app_version = "1.1"
URL = "https://cdn.discordapp.com/attachments/******************/******************/JINXZWARE.zip"
downloaddir = f"C:\\Users\\{os.getlogin()}\\Desktop\\JINXZWARE.zip"
password = ""

def getchecksum():
	path = os.path.basename(__file__)
	if not os.path.exists(path):
		path = path[:-2] + "exe"
	md5_hash = hashlib.md5()
	a_file = open(path,"rb")
	content = a_file.read()
	md5_hash.update(content)
	digest = md5_hash.hexdigest()
	return digest

keyauthapp = api(
	name = "",
	ownerid = "",
	secret = "",
	version = app_version,
    hash_to_check = getchecksum()
)

os.system("cls")
key = input('Enter your license: ')
keyauthapp.license(key)
def main():
    pythondir = os.path.exists(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\Programs\\Python")
    old = os.path.exists(f"C:\\Users\\{os.getlogin()}\\Desktop\\JINXZWARE")
    if pythondir == True:
        input("\nPress ENTER to download JINXZWARE.\n")
        with open (downloaddir, "wb") as f:
            f.write(requests.get(URL).content)
        if old == True:
            print("Deleting old JINXZWARE folder...")
            os.system(f"rmdir /s /q C:\\Users\\{os.getlogin()}\\Desktop\\JINXZWARE")
            os.system("echo.")
        if old == False:
            pass
        print(f"Downloaded JINXZWARE to: {Fore.CYAN}{downloaddir}{Fore.RESET}")
        print(f"Password for JINXZWARE = {Fore.GREEN}{password}{Fore.RESET}")
        os.system("timeout /t 120")


    if pythondir == False:
            downloadchoice = input(f"Python is required to use this cheat. Would you like to download it now? [{Fore.GREEN}y{Fore.RESET}/{Fore.RED}n{Fore.RESET}]:  ")
            if downloadchoice == "y":
                os.system("start www.python.org/download")
                input("Press ENTER once you have finished installing python.\n")
                main()
            if downloadchoice == "n":
                print("Exiting...")
                time.sleep(3)
                sys.exit
            else:
                print("That was an invalid option.")
                time.sleep(2)
                main()
            sys.exit

main()
