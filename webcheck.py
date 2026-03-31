import requests
from time import sleep

url = "https://www.sardinesclub.org"
new_content = ""
old_content = ""
url_home = f"{url}/Sardines%20Official%20Website%20About%20Us"
checkFrequency = 20
# noinspection PyRedeclaration
old_content = ""
# noinspection PyRedeclaration
new_content = ""
check_amount = 20

def fetch(address):
    try:
        try:
            output = requests.get(address)
            if output.status_code == 200:
                return output.text
            else:
                print("error")
        except requests.exceptions.ConnectionError:
            print("Sorry, The Website You Tried To Access Dose Not Exist!!")
    except requests.exceptions.MissingSchema:
        print("You are stupid to think that you can put a url with no https:// on it!")


def store(old):
    global new_content
    global old_content
    if not old:
        new_content = fetch(url_home)
        if new_content == "error":
            print("Error while connecting to site.\nCheck your internet connection.")
        else:
            print("Successfully connected to site.")
            ask = input("Type Y to see the page content, or N to continue.")
            if ask == "Y":
                print(new_content)
    else:
        old_content = fetch(url_home)
        if old_content == "error":
            print("Error while connecting to site.\nCheck your internet connection.")
        else:
            print("Successfully connected to site.")
            ask = input("Type Y to see the page content, or N to continue.\n")
            if ask == "Y":
                print(old_content)


def setup(command):
    global checkFrequency
    global url
    global url_home
    if command == "change-url":
        url = input("Enter new url\nsetup:")
    elif command == "change-check-frequency":
        checkFrequency = int(input("Enter new check frequency\nsetup:"))
    elif command == "change-home-directory":
        prompt = "Enter new home directory\nsetup:"
        url_home = f"{url}{input(prompt)}"
    else:
        print("cmd not valid")
def compare():
    global new_content
    global old_content
    if new_content == "" or old_content == "":
        print("Please fetch content first.")
    else:
        if new_content == old_content:
            print("Changes Have Been Made!!!!")
        else:
            print("No changes!!!!")
def check():
    global checkFrequency
    global check_amount
    for i in range(1, check_amount):
        print("checking...")
        compare()
        sleep(checkFrequency)

def interface():
    cmd = input()
    if cmd == "fetch-old":
        store(True)
        interface()
    if cmd == "fetch-new":
        store(False)
        interface()
    if cmd == "quit":
        exit()
    if cmd == "show-new":
        print()
        interface()
    if cmd == "bald":
        print("Thank You For Your Baldness\n")
        interface()
    if cmd == "setup":
        setup_cmd = input("What would you like to configure?\nsetup:")
        setup(setup_cmd)
        interface()
    if len(cmd) > 22:
        print("cmd not valid")
    if cmd == "check":
        check()
        interface()
    else:
        print("cmd not valid")
        interface()


print("welcome to the website checker")
interface()